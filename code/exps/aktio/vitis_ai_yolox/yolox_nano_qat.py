import os
from yolox.exp import ExpDeployQat as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.33
        self.width = 0.25
        self.depthwise = True
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
        self.max_epoch = 1
        # self.max_epoch = 60
        self.data_num_workers = 4
        self.is_qat = True
        self.float_ckpt = "YOLOX_outputs/vitis_ai_yolox_nano_float/best_ckpt.pth"
        self.eval_interval = 1
        self.calib_dir = "quantized_vitis_ai_yolox_nano"
