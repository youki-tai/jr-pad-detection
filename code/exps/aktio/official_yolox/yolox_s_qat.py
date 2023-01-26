import os

from yolox.exp import ExpDeployQat as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.33
        self.width = 0.50
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]

        # Define yourself dataset path
        # datasize
        self.input_size = (480, 640)  # (height, width)
        self.test_size = (480, 640)  # (height, width)
        # path
        self.data_dir = "aktio_datasets/AKTIO_1202_alldata_COCO_format"
        self.train_ann = "instances_train2017.json"
        self.val_ann = "instances_val2017.json"

        self.num_classes = 1

        self.warmup_epochs = 1
        # self.max_epoch = 1
        self.max_epoch = 60
        self.data_num_workers = 4
        self.is_qat = True
        self.float_ckpt = "YOLOX_outputs/yolox_s_aktio_float/best_ckpt.pth"
        self.eval_interval = 1
        self.calib_dir = "quantized"

    def get_model(self):
        from yolox.models import YOLOX, YOLOXHead

        # 1st conv: in-channel=12
        from yolox.models.yolo_pafpn import YOLOPAFPN

        # 1st conv: in-channel=3
        # from yolox.models.yolo_pafpn_deploy import YOLOPAFPN

        def init_yolo(M):
            for m in M.modules():
                import torch.nn as nn

                if isinstance(m, nn.BatchNorm2d):
                    m.eps = 1e-3
                    m.momentum = 0.03

        if getattr(self, "model", None) is None:
            in_channels = [256, 512, 1024]
            backbone = YOLOPAFPN(
                self.depth, self.width, in_channels=in_channels, act=self.act
            )
            head = YOLOXHead(
                self.num_classes, self.width, in_channels=in_channels, act=self.act
            )
            self.model = YOLOX(backbone, head)

        self.model.apply(init_yolo)
        self.model.head.initialize_biases(1e-2)

        if self.is_qat:
            import torch
            from pytorch_nndct import QatProcessor

            if self.float_ckpt:
                ckpt = torch.load(self.float_ckpt)
                print(
                    "Loading float model weight for QAT from {}".format(self.float_ckpt)
                )
                self.model.load_state_dict(ckpt["model"])
            dummy_input = torch.randn([1, 3, 640, 640], dtype=torch.float32).cuda()
            self.qat_processor = QatProcessor(
                self.model, dummy_input, bitwidth=8, mix_bit=False
            )
            self.model = self.qat_processor.trainable_model(calib_dir=self.calib_dir)

        return self.model
