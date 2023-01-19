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
