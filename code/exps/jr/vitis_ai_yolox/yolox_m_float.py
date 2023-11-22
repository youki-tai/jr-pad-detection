import os
from yolox.exp import ExpDeploy as MyExp

class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.67
        self.width = 0.75
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]

        # datasize
        self.input_size = (224, 384)  # (height, width)
        self.test_size = (448, 384)  # (height, width)
        # path
        self.data_dir = "jr_dataset"
        self.train_ann = "instances_train2017.json"
        self.val_ann = "instances_val2017.json"

        self.num_classes = 2

        # --------------- transform config ----------------- #
        # self.mosaic_prob = 0.6929421828750495
        # self.mosaic_scale = (1.536446217383411, 1.2399716683782294)
        # self.translate = 0.2464943132842582
        # self.shear = 1.3177385982562617
        #self.mosaic_prob = 0.5
        #self.degrees = 5.0
        #self.no_aug_epochs = 1000
        self.mosaic_prob = 0

        # --------------  training config --------------------- #
        self.warmup_epochs = 5
        # self.min_lr_ratio = 0.25422789344672647
        self.basic_lr_per_img = 1e-4
        self.max_epoch = 150
        self.data_num_workers = 4
        #self.data_num_workers = 0
        self.eval_interval = 10

        self.act = "lrelu"
