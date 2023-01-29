import os
import torch.nn as nn
from yolox.exp import ExpDeploy as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.33
        self.width = 0.25
        self.depthwise = True

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
