import os

from yolox.exp import ExpDeploy as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.33
        self.width = 0.50
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]

        # Define yourself dataset path
        self.data_dir = "datasets/data/tt100k"
        self.train_ann = "tt100k_in_coco_format_train.json"
        self.val_ann = "tt100k_in_coco_format_test.json"

        self.num_classes = 1

        self.warmup_epochs = 5
        self.max_epoch = 1
        # self.max_epoch = 300
        self.data_num_workers = 4
        self.eval_interval = 1


    def get_model(self):
        # print("Hello WOrld########################")
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
            backbone = YOLOPAFPN(self.depth, self.width, in_channels=in_channels, act=self.act)
            head = YOLOXHead(self.num_classes, self.width, in_channels=in_channels, act=self.act)
            self.model = YOLOX(backbone, head)

        self.model.apply(init_yolo)
        self.model.head.initialize_biases(1e-2)
        return self.model



