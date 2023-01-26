import os
import torch.nn as nn
from yolox.exp import ExpDeploy as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.33
        self.width = 0.25
        self.input_size = (480, 640)
        self.test_size = (480, 640)
        self.mosaic_scale = (0.5, 1.5)
        self.random_size = (10, 20)
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]
        self.enable_mixup = False

        # Define yourself dataset path
        self.data_dir = "aktio_datasets/AKTIO_1202_alldata_COCO_format"
        self.train_ann = "instances_train2017.json"
        self.val_ann = "instances_val2017.json"

        self.num_classes = 1
        self.warmup_epochs = 5
        self.max_epoch = 1
        # self.max_epoch = 300
        self.data_num_workers = 4
        self.eval_interval = 1


    def get_model(self, sublinear=False):
        def init_yolo(M):
            for m in M.modules():
                if isinstance(m, nn.BatchNorm2d):
                    m.eps = 1e-3
                    m.momentum = 0.03

        if "model" not in self.__dict__:
            from yolox.models import YOLOX, YOLOXHead
            from yolox.models.yolo_pafpn_deploy import YOLOPAFPN

            in_channels = [256, 512, 1024]
            backbone = YOLOPAFPN(
                self.depth, self.width, in_channels=in_channels, depthwise=True
            )
            head = YOLOXHead(
                self.num_classes, self.width, in_channels=in_channels, depthwise=True
            )
            self.model = YOLOX(backbone, head)

        self.model.apply(init_yolo)
        self.model.head.initialize_biases(1e-2)
        return self.model
