# GENETARED BY NNDCT, DO NOT EDIT!

import torch
import pytorch_nndct as py_nndct
class YOLOX(torch.nn.Module):
    def __init__(self):
        super(YOLOX, self).__init__()
        self.module_0 = py_nndct.nn.Input() #YOLOX::input_0
        self.module_1 = py_nndct.nn.quant_input() #YOLOX::YOLOX/QuantStub[quant_in]/input.1
        self.module_2 = py_nndct.nn.Conv2d(in_channels=3, out_channels=16, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/FocusDeploy[stem]/BaseConv[conv]/Conv2d[conv]/input.2
        self.module_4 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/FocusDeploy[stem]/BaseConv[conv]/SiLU[act]/input.4
        self.module_5 = py_nndct.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=16, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/DWConv[0]/BaseConv[dconv]/Conv2d[conv]/input.5
        self.module_7 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/DWConv[0]/BaseConv[dconv]/SiLU[act]/input.7
        self.module_8 = py_nndct.nn.Conv2d(in_channels=16, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/DWConv[0]/BaseConv[pconv]/Conv2d[conv]/input.8
        self.module_10 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/DWConv[0]/BaseConv[pconv]/SiLU[act]/input.10
        self.module_11 = py_nndct.nn.Conv2d(in_channels=32, out_channels=16, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/BaseConv[conv1]/Conv2d[conv]/input.11
        self.module_13 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/BaseConv[conv1]/SiLU[act]/input.15
        self.module_14 = py_nndct.nn.Conv2d(in_channels=32, out_channels=16, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/BaseConv[conv2]/Conv2d[conv]/input.13
        self.module_16 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/BaseConv[conv2]/SiLU[act]/22682
        self.module_17 = py_nndct.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.16
        self.module_19 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/SiLU[act]/input.18
        self.module_20 = py_nndct.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=16, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[dconv]/Conv2d[conv]/input.19
        self.module_22 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[dconv]/SiLU[act]/input.21
        self.module_23 = py_nndct.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[pconv]/Conv2d[conv]/input.22
        self.module_25 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[pconv]/SiLU[act]/22760
        self.module_26 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/Add[sc_add]/22762
        self.module_27 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/Cat[cat]/input.24
        self.module_28 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/BaseConv[conv3]/Conv2d[conv]/input.25
        self.module_30 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/Q_CSPLayer[1]/BaseConv[conv3]/SiLU[act]/input.27
        self.module_31 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=32, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/DWConv[0]/BaseConv[dconv]/Conv2d[conv]/input.28
        self.module_33 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/DWConv[0]/BaseConv[dconv]/SiLU[act]/input.30
        self.module_34 = py_nndct.nn.Conv2d(in_channels=32, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/DWConv[0]/BaseConv[pconv]/Conv2d[conv]/input.31
        self.module_36 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/DWConv[0]/BaseConv[pconv]/SiLU[act]/input.33
        self.module_37 = py_nndct.nn.Conv2d(in_channels=64, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/BaseConv[conv1]/Conv2d[conv]/input.34
        self.module_39 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/BaseConv[conv1]/SiLU[act]/input.38
        self.module_40 = py_nndct.nn.Conv2d(in_channels=64, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/BaseConv[conv2]/Conv2d[conv]/input.36
        self.module_42 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/BaseConv[conv2]/SiLU[act]/22895
        self.module_43 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.39
        self.module_45 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/SiLU[act]/input.41
        self.module_46 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=32, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[dconv]/Conv2d[conv]/input.42
        self.module_48 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[dconv]/SiLU[act]/input.44
        self.module_49 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[pconv]/Conv2d[conv]/input.45
        self.module_51 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[pconv]/SiLU[act]/22973
        self.module_52 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/Add[sc_add]/input.47
        self.module_53 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv1]/Conv2d[conv]/input.48
        self.module_55 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv1]/SiLU[act]/input.50
        self.module_56 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=32, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/DWConv[conv2]/BaseConv[dconv]/Conv2d[conv]/input.51
        self.module_58 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/DWConv[conv2]/BaseConv[dconv]/SiLU[act]/input.53
        self.module_59 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/DWConv[conv2]/BaseConv[pconv]/Conv2d[conv]/input.54
        self.module_61 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/DWConv[conv2]/BaseConv[pconv]/SiLU[act]/23053
        self.module_62 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/Add[sc_add]/input.56
        self.module_63 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[2]/BaseConv[conv1]/Conv2d[conv]/input.57
        self.module_65 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[2]/BaseConv[conv1]/SiLU[act]/input.59
        self.module_66 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=32, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[2]/DWConv[conv2]/BaseConv[dconv]/Conv2d[conv]/input.60
        self.module_68 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[2]/DWConv[conv2]/BaseConv[dconv]/SiLU[act]/input.62
        self.module_69 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[2]/DWConv[conv2]/BaseConv[pconv]/Conv2d[conv]/input.63
        self.module_71 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[2]/DWConv[conv2]/BaseConv[pconv]/SiLU[act]/23133
        self.module_72 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[2]/Add[sc_add]/23135
        self.module_73 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/Cat[cat]/input.65
        self.module_74 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/BaseConv[conv3]/Conv2d[conv]/input.66
        self.module_76 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/Q_CSPLayer[1]/BaseConv[conv3]/SiLU[act]/input.68
        self.module_77 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/DWConv[0]/BaseConv[dconv]/Conv2d[conv]/input.69
        self.module_79 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/DWConv[0]/BaseConv[dconv]/SiLU[act]/input.71
        self.module_80 = py_nndct.nn.Conv2d(in_channels=64, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/DWConv[0]/BaseConv[pconv]/Conv2d[conv]/input.72
        self.module_82 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/DWConv[0]/BaseConv[pconv]/SiLU[act]/input.74
        self.module_83 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/BaseConv[conv1]/Conv2d[conv]/input.75
        self.module_85 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/BaseConv[conv1]/SiLU[act]/input.79
        self.module_86 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/BaseConv[conv2]/Conv2d[conv]/input.77
        self.module_88 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/BaseConv[conv2]/SiLU[act]/23268
        self.module_89 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.80
        self.module_91 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/SiLU[act]/input.82
        self.module_92 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[dconv]/Conv2d[conv]/input.83
        self.module_94 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[dconv]/SiLU[act]/input.85
        self.module_95 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[pconv]/Conv2d[conv]/input.86
        self.module_97 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[pconv]/SiLU[act]/23346
        self.module_98 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[0]/Add[sc_add]/input.88
        self.module_99 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv1]/Conv2d[conv]/input.89
        self.module_101 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/BaseConv[conv1]/SiLU[act]/input.91
        self.module_102 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/DWConv[conv2]/BaseConv[dconv]/Conv2d[conv]/input.92
        self.module_104 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/DWConv[conv2]/BaseConv[dconv]/SiLU[act]/input.94
        self.module_105 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/DWConv[conv2]/BaseConv[pconv]/Conv2d[conv]/input.95
        self.module_107 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/DWConv[conv2]/BaseConv[pconv]/SiLU[act]/23426
        self.module_108 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[1]/Add[sc_add]/input.97
        self.module_109 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[2]/BaseConv[conv1]/Conv2d[conv]/input.98
        self.module_111 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[2]/BaseConv[conv1]/SiLU[act]/input.100
        self.module_112 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[2]/DWConv[conv2]/BaseConv[dconv]/Conv2d[conv]/input.101
        self.module_114 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[2]/DWConv[conv2]/BaseConv[dconv]/SiLU[act]/input.103
        self.module_115 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[2]/DWConv[conv2]/BaseConv[pconv]/Conv2d[conv]/input.104
        self.module_117 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[2]/DWConv[conv2]/BaseConv[pconv]/SiLU[act]/23506
        self.module_118 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Sequential[m]/Q_Bottleneck[2]/Add[sc_add]/23508
        self.module_119 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/Cat[cat]/input.106
        self.module_120 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/BaseConv[conv3]/Conv2d[conv]/input.107
        self.module_122 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/Q_CSPLayer[1]/BaseConv[conv3]/SiLU[act]/input.109
        self.module_123 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=128, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/DWConv[0]/BaseConv[dconv]/Conv2d[conv]/input.110
        self.module_125 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/DWConv[0]/BaseConv[dconv]/SiLU[act]/input.112
        self.module_126 = py_nndct.nn.Conv2d(in_channels=128, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/DWConv[0]/BaseConv[pconv]/Conv2d[conv]/input.113
        self.module_128 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/DWConv[0]/BaseConv[pconv]/SiLU[act]/input.115
        self.module_129 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_SPPBottleneck[1]/BaseConv[conv1]/Conv2d[conv]/input.116
        self.module_131 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_SPPBottleneck[1]/BaseConv[conv1]/SiLU[act]/23615
        self.module_132 = py_nndct.nn.MaxPool2d(kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], ceil_mode=False) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_SPPBottleneck[1]/MaxPool2d[m]/ModuleList[0]/23629
        self.module_133 = py_nndct.nn.MaxPool2d(kernel_size=[5, 5], stride=[1, 1], padding=[2, 2], dilation=[1, 1], ceil_mode=False) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_SPPBottleneck[1]/MaxPool2d[m]/ModuleList[1]/23643
        self.module_134 = py_nndct.nn.MaxPool2d(kernel_size=[7, 7], stride=[1, 1], padding=[3, 3], dilation=[1, 1], ceil_mode=False) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_SPPBottleneck[1]/MaxPool2d[m]/ModuleList[2]/23657
        self.module_135 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_SPPBottleneck[1]/Cat[cat]/input.118
        self.module_136 = py_nndct.nn.Conv2d(in_channels=512, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_SPPBottleneck[1]/BaseConv[conv2]/Conv2d[conv]/input.119
        self.module_138 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_SPPBottleneck[1]/BaseConv[conv2]/SiLU[act]/input.121
        self.module_139 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/BaseConv[conv1]/Conv2d[conv]/input.122
        self.module_141 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/BaseConv[conv1]/SiLU[act]/input.126
        self.module_142 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/BaseConv[conv2]/Conv2d[conv]/input.124
        self.module_144 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/BaseConv[conv2]/SiLU[act]/23738
        self.module_145 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.127
        self.module_147 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/SiLU[act]/input.129
        self.module_148 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=128, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[dconv]/Conv2d[conv]/input.130
        self.module_150 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[dconv]/SiLU[act]/input.132
        self.module_151 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[pconv]/Conv2d[conv]/input.133
        self.module_153 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[pconv]/SiLU[act]/23816
        self.module_154 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/Cat[cat]/input.135
        self.module_155 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/BaseConv[conv3]/Conv2d[conv]/input.136
        self.module_157 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/Q_CSPLayer[2]/BaseConv[conv3]/SiLU[act]/input.138
        self.module_158 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/BaseConv[lateral_conv0]/Conv2d[conv]/input.139
        self.module_160 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/BaseConv[lateral_conv0]/SiLU[act]/input.141
        self.module_161 = py_nndct.nn.Interpolate() #YOLOX::YOLOX/YOLOPAFPN[backbone]/Upsample[upsample]/23880
        self.module_162 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/Cat[cat_f0]/input.142
        self.module_163 = py_nndct.nn.Conv2d(in_channels=256, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/BaseConv[conv1]/Conv2d[conv]/input.143
        self.module_165 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/BaseConv[conv1]/SiLU[act]/input.147
        self.module_166 = py_nndct.nn.Conv2d(in_channels=256, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/BaseConv[conv2]/Conv2d[conv]/input.145
        self.module_168 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/BaseConv[conv2]/SiLU[act]/23935
        self.module_169 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.148
        self.module_171 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/SiLU[act]/input.150
        self.module_172 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[dconv]/Conv2d[conv]/input.151
        self.module_174 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[dconv]/SiLU[act]/input.153
        self.module_175 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[pconv]/Conv2d[conv]/input.154
        self.module_177 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[pconv]/SiLU[act]/24013
        self.module_178 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/Cat[cat]/input.156
        self.module_179 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/BaseConv[conv3]/Conv2d[conv]/input.157
        self.module_181 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p4]/BaseConv[conv3]/SiLU[act]/input.159
        self.module_182 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/BaseConv[reduce_conv1]/Conv2d[conv]/input.160
        self.module_184 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/BaseConv[reduce_conv1]/SiLU[act]/input.162
        self.module_185 = py_nndct.nn.Interpolate() #YOLOX::YOLOX/YOLOPAFPN[backbone]/Upsample[upsample]/24073
        self.module_186 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/Cat[cat_f1]/input.163
        self.module_187 = py_nndct.nn.Conv2d(in_channels=128, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/BaseConv[conv1]/Conv2d[conv]/input.164
        self.module_189 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/BaseConv[conv1]/SiLU[act]/input.168
        self.module_190 = py_nndct.nn.Conv2d(in_channels=128, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/BaseConv[conv2]/Conv2d[conv]/input.166
        self.module_192 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/BaseConv[conv2]/SiLU[act]/24128
        self.module_193 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.169
        self.module_195 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/SiLU[act]/input.171
        self.module_196 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=32, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[dconv]/Conv2d[conv]/input.172
        self.module_198 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[dconv]/SiLU[act]/input.174
        self.module_199 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[pconv]/Conv2d[conv]/input.175
        self.module_201 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[pconv]/SiLU[act]/24206
        self.module_202 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/Cat[cat]/input.177
        self.module_203 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/BaseConv[conv3]/Conv2d[conv]/input.178
        self.module_205 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_p3]/BaseConv[conv3]/SiLU[act]/input.180
        self.module_206 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/DWConv[bu_conv2]/BaseConv[dconv]/Conv2d[conv]/input.181
        self.module_208 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/DWConv[bu_conv2]/BaseConv[dconv]/SiLU[act]/input.183
        self.module_209 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/DWConv[bu_conv2]/BaseConv[pconv]/Conv2d[conv]/input.184
        self.module_211 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/DWConv[bu_conv2]/BaseConv[pconv]/SiLU[act]/24287
        self.module_212 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/Cat[cat_p1]/input.186
        self.module_213 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/BaseConv[conv1]/Conv2d[conv]/input.187
        self.module_215 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/BaseConv[conv1]/SiLU[act]/input.191
        self.module_216 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/BaseConv[conv2]/Conv2d[conv]/input.189
        self.module_218 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/BaseConv[conv2]/SiLU[act]/24342
        self.module_219 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.192
        self.module_221 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/SiLU[act]/input.194
        self.module_222 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[dconv]/Conv2d[conv]/input.195
        self.module_224 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[dconv]/SiLU[act]/input.197
        self.module_225 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[pconv]/Conv2d[conv]/input.198
        self.module_227 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[pconv]/SiLU[act]/24420
        self.module_228 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/Cat[cat]/input.200
        self.module_229 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/BaseConv[conv3]/Conv2d[conv]/input.201
        self.module_231 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n3]/BaseConv[conv3]/SiLU[act]/input.203
        self.module_232 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=128, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/DWConv[bu_conv1]/BaseConv[dconv]/Conv2d[conv]/input.204
        self.module_234 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/DWConv[bu_conv1]/BaseConv[dconv]/SiLU[act]/input.206
        self.module_235 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/DWConv[bu_conv1]/BaseConv[pconv]/Conv2d[conv]/input.207
        self.module_237 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/DWConv[bu_conv1]/BaseConv[pconv]/SiLU[act]/24501
        self.module_238 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/Cat[cat_p0]/input.209
        self.module_239 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/BaseConv[conv1]/Conv2d[conv]/input.210
        self.module_241 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/BaseConv[conv1]/SiLU[act]/input.214
        self.module_242 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/BaseConv[conv2]/Conv2d[conv]/input.212
        self.module_244 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/BaseConv[conv2]/SiLU[act]/24556
        self.module_245 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.215
        self.module_247 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/Sequential[m]/Q_Bottleneck[0]/BaseConv[conv1]/SiLU[act]/input.217
        self.module_248 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=128, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[dconv]/Conv2d[conv]/input.218
        self.module_250 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[dconv]/SiLU[act]/input.220
        self.module_251 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[pconv]/Conv2d[conv]/input.221
        self.module_253 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/Sequential[m]/Q_Bottleneck[0]/DWConv[conv2]/BaseConv[pconv]/SiLU[act]/24634
        self.module_254 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/Cat[cat]/input.223
        self.module_255 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/BaseConv[conv3]/Conv2d[conv]/input.224
        self.module_257 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOPAFPN[backbone]/Q_CSPLayer[C3_n4]/BaseConv[conv3]/SiLU[act]/input.280
        self.module_258 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/BaseConv[stems]/ModuleList[0]/Conv2d[conv]/input.226
        self.module_260 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/BaseConv[stems]/ModuleList[0]/SiLU[act]/input.228
        self.module_261 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[0]/DWConv[0]/BaseConv[dconv]/Conv2d[conv]/input.229
        self.module_263 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[0]/DWConv[0]/BaseConv[dconv]/SiLU[act]/input.231
        self.module_264 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[0]/DWConv[0]/BaseConv[pconv]/Conv2d[conv]/input.232
        self.module_266 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[0]/DWConv[0]/BaseConv[pconv]/SiLU[act]/input.234
        self.module_267 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[0]/DWConv[1]/BaseConv[dconv]/Conv2d[conv]/input.235
        self.module_269 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[0]/DWConv[1]/BaseConv[dconv]/SiLU[act]/input.237
        self.module_270 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[0]/DWConv[1]/BaseConv[pconv]/Conv2d[conv]/input.238
        self.module_272 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[0]/DWConv[1]/BaseConv[pconv]/SiLU[act]/input.240
        self.module_273 = py_nndct.nn.Conv2d(in_channels=64, out_channels=1, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[cls_preds]/ModuleList[0]/24816
        self.module_274 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[0]/DWConv[0]/BaseConv[dconv]/Conv2d[conv]/input.241
        self.module_276 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[0]/DWConv[0]/BaseConv[dconv]/SiLU[act]/input.243
        self.module_277 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[0]/DWConv[0]/BaseConv[pconv]/Conv2d[conv]/input.244
        self.module_279 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[0]/DWConv[0]/BaseConv[pconv]/SiLU[act]/input.246
        self.module_280 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[0]/DWConv[1]/BaseConv[dconv]/Conv2d[conv]/input.247
        self.module_282 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[0]/DWConv[1]/BaseConv[dconv]/SiLU[act]/input.249
        self.module_283 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[0]/DWConv[1]/BaseConv[pconv]/Conv2d[conv]/input.250
        self.module_285 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[0]/DWConv[1]/BaseConv[pconv]/SiLU[act]/input.252
        self.module_286 = py_nndct.nn.Conv2d(in_channels=64, out_channels=4, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[reg_preds]/ModuleList[0]/24939
        self.module_287 = py_nndct.nn.Conv2d(in_channels=64, out_channels=1, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[obj_preds]/ModuleList[0]/24958
        self.module_288 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOXHead[head]/Cat[cat_list]/ModuleList[0]/24961
        self.module_289 = py_nndct.nn.dequant_output() #YOLOX::YOLOX/YOLOXHead[head]/DeQuantStub[quant_outs]/ModuleList[0]/24962
        self.module_290 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/BaseConv[stems]/ModuleList[1]/Conv2d[conv]/input.253
        self.module_292 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/BaseConv[stems]/ModuleList[1]/SiLU[act]/input.255
        self.module_293 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[1]/DWConv[0]/BaseConv[dconv]/Conv2d[conv]/input.256
        self.module_295 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[1]/DWConv[0]/BaseConv[dconv]/SiLU[act]/input.258
        self.module_296 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[1]/DWConv[0]/BaseConv[pconv]/Conv2d[conv]/input.259
        self.module_298 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[1]/DWConv[0]/BaseConv[pconv]/SiLU[act]/input.261
        self.module_299 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[1]/DWConv[1]/BaseConv[dconv]/Conv2d[conv]/input.262
        self.module_301 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[1]/DWConv[1]/BaseConv[dconv]/SiLU[act]/input.264
        self.module_302 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[1]/DWConv[1]/BaseConv[pconv]/Conv2d[conv]/input.265
        self.module_304 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[1]/DWConv[1]/BaseConv[pconv]/SiLU[act]/input.267
        self.module_305 = py_nndct.nn.Conv2d(in_channels=64, out_channels=1, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[cls_preds]/ModuleList[1]/25112
        self.module_306 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[1]/DWConv[0]/BaseConv[dconv]/Conv2d[conv]/input.268
        self.module_308 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[1]/DWConv[0]/BaseConv[dconv]/SiLU[act]/input.270
        self.module_309 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[1]/DWConv[0]/BaseConv[pconv]/Conv2d[conv]/input.271
        self.module_311 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[1]/DWConv[0]/BaseConv[pconv]/SiLU[act]/input.273
        self.module_312 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[1]/DWConv[1]/BaseConv[dconv]/Conv2d[conv]/input.274
        self.module_314 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[1]/DWConv[1]/BaseConv[dconv]/SiLU[act]/input.276
        self.module_315 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[1]/DWConv[1]/BaseConv[pconv]/Conv2d[conv]/input.277
        self.module_317 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[1]/DWConv[1]/BaseConv[pconv]/SiLU[act]/input.279
        self.module_318 = py_nndct.nn.Conv2d(in_channels=64, out_channels=4, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[reg_preds]/ModuleList[1]/25235
        self.module_319 = py_nndct.nn.Conv2d(in_channels=64, out_channels=1, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[obj_preds]/ModuleList[1]/25254
        self.module_320 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOXHead[head]/Cat[cat_list]/ModuleList[1]/25257
        self.module_321 = py_nndct.nn.dequant_output() #YOLOX::YOLOX/YOLOXHead[head]/DeQuantStub[quant_outs]/ModuleList[1]/25258
        self.module_322 = py_nndct.nn.Conv2d(in_channels=256, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/BaseConv[stems]/ModuleList[2]/Conv2d[conv]/input.281
        self.module_324 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/BaseConv[stems]/ModuleList[2]/SiLU[act]/input.283
        self.module_325 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[2]/DWConv[0]/BaseConv[dconv]/Conv2d[conv]/input.284
        self.module_327 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[2]/DWConv[0]/BaseConv[dconv]/SiLU[act]/input.286
        self.module_328 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[2]/DWConv[0]/BaseConv[pconv]/Conv2d[conv]/input.287
        self.module_330 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[2]/DWConv[0]/BaseConv[pconv]/SiLU[act]/input.289
        self.module_331 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[2]/DWConv[1]/BaseConv[dconv]/Conv2d[conv]/input.290
        self.module_333 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[2]/DWConv[1]/BaseConv[dconv]/SiLU[act]/input.292
        self.module_334 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[2]/DWConv[1]/BaseConv[pconv]/Conv2d[conv]/input.293
        self.module_336 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[2]/DWConv[1]/BaseConv[pconv]/SiLU[act]/input.295
        self.module_337 = py_nndct.nn.Conv2d(in_channels=64, out_channels=1, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[cls_preds]/ModuleList[2]/25408
        self.module_338 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[2]/DWConv[0]/BaseConv[dconv]/Conv2d[conv]/input.296
        self.module_340 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[2]/DWConv[0]/BaseConv[dconv]/SiLU[act]/input.298
        self.module_341 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[2]/DWConv[0]/BaseConv[pconv]/Conv2d[conv]/input.299
        self.module_343 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[2]/DWConv[0]/BaseConv[pconv]/SiLU[act]/input.301
        self.module_344 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=64, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[2]/DWConv[1]/BaseConv[dconv]/Conv2d[conv]/input.302
        self.module_346 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[2]/DWConv[1]/BaseConv[dconv]/SiLU[act]/input.304
        self.module_347 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[2]/DWConv[1]/BaseConv[pconv]/Conv2d[conv]/input.305
        self.module_349 = py_nndct.nn.Module('aten::silu_') #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[2]/DWConv[1]/BaseConv[pconv]/SiLU[act]/input
        self.module_350 = py_nndct.nn.Conv2d(in_channels=64, out_channels=4, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[reg_preds]/ModuleList[2]/25531
        self.module_351 = py_nndct.nn.Conv2d(in_channels=64, out_channels=1, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[obj_preds]/ModuleList[2]/25550
        self.module_352 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOXHead[head]/Cat[cat_list]/ModuleList[2]/25553
        self.module_353 = py_nndct.nn.dequant_output() #YOLOX::YOLOX/YOLOXHead[head]/DeQuantStub[quant_outs]/ModuleList[2]/25554

    def forward(self, *args):
        output_module_0 = self.module_0(input=args[0])
        output_module_0 = self.module_1(input=output_module_0)
        output_module_0 = self.module_2(output_module_0)
        output_module_0 = self.module_4(output_module_0)
        output_module_0 = self.module_5(output_module_0)
        output_module_0 = self.module_7(output_module_0)
        output_module_0 = self.module_8(output_module_0)
        output_module_0 = self.module_10(output_module_0)
        output_module_11 = self.module_11(output_module_0)
        output_module_11 = self.module_13(output_module_11)
        output_module_14 = self.module_14(output_module_0)
        output_module_14 = self.module_16(output_module_14)
        output_module_17 = self.module_17(output_module_11)
        output_module_17 = self.module_19(output_module_17)
        output_module_17 = self.module_20(output_module_17)
        output_module_17 = self.module_22(output_module_17)
        output_module_17 = self.module_23(output_module_17)
        output_module_17 = self.module_25(output_module_17)
        output_module_17 = self.module_26(input=output_module_17, other=output_module_11, alpha=1)
        output_module_17 = self.module_27(dim=1, tensors=[output_module_17,output_module_14])
        output_module_17 = self.module_28(output_module_17)
        output_module_17 = self.module_30(output_module_17)
        output_module_17 = self.module_31(output_module_17)
        output_module_17 = self.module_33(output_module_17)
        output_module_17 = self.module_34(output_module_17)
        output_module_17 = self.module_36(output_module_17)
        output_module_37 = self.module_37(output_module_17)
        output_module_37 = self.module_39(output_module_37)
        output_module_40 = self.module_40(output_module_17)
        output_module_40 = self.module_42(output_module_40)
        output_module_43 = self.module_43(output_module_37)
        output_module_43 = self.module_45(output_module_43)
        output_module_43 = self.module_46(output_module_43)
        output_module_43 = self.module_48(output_module_43)
        output_module_43 = self.module_49(output_module_43)
        output_module_43 = self.module_51(output_module_43)
        output_module_43 = self.module_52(input=output_module_43, other=output_module_37, alpha=1)
        output_module_53 = self.module_53(output_module_43)
        output_module_53 = self.module_55(output_module_53)
        output_module_53 = self.module_56(output_module_53)
        output_module_53 = self.module_58(output_module_53)
        output_module_53 = self.module_59(output_module_53)
        output_module_53 = self.module_61(output_module_53)
        output_module_53 = self.module_62(input=output_module_53, other=output_module_43, alpha=1)
        output_module_63 = self.module_63(output_module_53)
        output_module_63 = self.module_65(output_module_63)
        output_module_63 = self.module_66(output_module_63)
        output_module_63 = self.module_68(output_module_63)
        output_module_63 = self.module_69(output_module_63)
        output_module_63 = self.module_71(output_module_63)
        output_module_63 = self.module_72(input=output_module_63, other=output_module_53, alpha=1)
        output_module_63 = self.module_73(dim=1, tensors=[output_module_63,output_module_40])
        output_module_63 = self.module_74(output_module_63)
        output_module_63 = self.module_76(output_module_63)
        output_module_77 = self.module_77(output_module_63)
        output_module_77 = self.module_79(output_module_77)
        output_module_77 = self.module_80(output_module_77)
        output_module_77 = self.module_82(output_module_77)
        output_module_83 = self.module_83(output_module_77)
        output_module_83 = self.module_85(output_module_83)
        output_module_86 = self.module_86(output_module_77)
        output_module_86 = self.module_88(output_module_86)
        output_module_89 = self.module_89(output_module_83)
        output_module_89 = self.module_91(output_module_89)
        output_module_89 = self.module_92(output_module_89)
        output_module_89 = self.module_94(output_module_89)
        output_module_89 = self.module_95(output_module_89)
        output_module_89 = self.module_97(output_module_89)
        output_module_89 = self.module_98(input=output_module_89, other=output_module_83, alpha=1)
        output_module_99 = self.module_99(output_module_89)
        output_module_99 = self.module_101(output_module_99)
        output_module_99 = self.module_102(output_module_99)
        output_module_99 = self.module_104(output_module_99)
        output_module_99 = self.module_105(output_module_99)
        output_module_99 = self.module_107(output_module_99)
        output_module_99 = self.module_108(input=output_module_99, other=output_module_89, alpha=1)
        output_module_109 = self.module_109(output_module_99)
        output_module_109 = self.module_111(output_module_109)
        output_module_109 = self.module_112(output_module_109)
        output_module_109 = self.module_114(output_module_109)
        output_module_109 = self.module_115(output_module_109)
        output_module_109 = self.module_117(output_module_109)
        output_module_109 = self.module_118(input=output_module_109, other=output_module_99, alpha=1)
        output_module_109 = self.module_119(dim=1, tensors=[output_module_109,output_module_86])
        output_module_109 = self.module_120(output_module_109)
        output_module_109 = self.module_122(output_module_109)
        output_module_123 = self.module_123(output_module_109)
        output_module_123 = self.module_125(output_module_123)
        output_module_123 = self.module_126(output_module_123)
        output_module_123 = self.module_128(output_module_123)
        output_module_123 = self.module_129(output_module_123)
        output_module_123 = self.module_131(output_module_123)
        output_module_132 = self.module_132(output_module_123)
        output_module_133 = self.module_133(output_module_123)
        output_module_134 = self.module_134(output_module_123)
        output_module_135 = self.module_135(dim=1, tensors=[output_module_123,output_module_132,output_module_133,output_module_134])
        output_module_135 = self.module_136(output_module_135)
        output_module_135 = self.module_138(output_module_135)
        output_module_139 = self.module_139(output_module_135)
        output_module_139 = self.module_141(output_module_139)
        output_module_142 = self.module_142(output_module_135)
        output_module_142 = self.module_144(output_module_142)
        output_module_139 = self.module_145(output_module_139)
        output_module_139 = self.module_147(output_module_139)
        output_module_139 = self.module_148(output_module_139)
        output_module_139 = self.module_150(output_module_139)
        output_module_139 = self.module_151(output_module_139)
        output_module_139 = self.module_153(output_module_139)
        output_module_139 = self.module_154(dim=1, tensors=[output_module_139,output_module_142])
        output_module_139 = self.module_155(output_module_139)
        output_module_139 = self.module_157(output_module_139)
        output_module_139 = self.module_158(output_module_139)
        output_module_139 = self.module_160(output_module_139)
        output_module_161 = self.module_161(input=output_module_139, size=None, scale_factor=[2.0,2.0], mode='nearest')
        output_module_161 = self.module_162(dim=1, tensors=[output_module_161,output_module_109])
        output_module_163 = self.module_163(output_module_161)
        output_module_163 = self.module_165(output_module_163)
        output_module_166 = self.module_166(output_module_161)
        output_module_166 = self.module_168(output_module_166)
        output_module_163 = self.module_169(output_module_163)
        output_module_163 = self.module_171(output_module_163)
        output_module_163 = self.module_172(output_module_163)
        output_module_163 = self.module_174(output_module_163)
        output_module_163 = self.module_175(output_module_163)
        output_module_163 = self.module_177(output_module_163)
        output_module_163 = self.module_178(dim=1, tensors=[output_module_163,output_module_166])
        output_module_163 = self.module_179(output_module_163)
        output_module_163 = self.module_181(output_module_163)
        output_module_163 = self.module_182(output_module_163)
        output_module_163 = self.module_184(output_module_163)
        output_module_185 = self.module_185(input=output_module_163, size=None, scale_factor=[2.0,2.0], mode='nearest')
        output_module_185 = self.module_186(dim=1, tensors=[output_module_185,output_module_63])
        output_module_187 = self.module_187(output_module_185)
        output_module_187 = self.module_189(output_module_187)
        output_module_190 = self.module_190(output_module_185)
        output_module_190 = self.module_192(output_module_190)
        output_module_187 = self.module_193(output_module_187)
        output_module_187 = self.module_195(output_module_187)
        output_module_187 = self.module_196(output_module_187)
        output_module_187 = self.module_198(output_module_187)
        output_module_187 = self.module_199(output_module_187)
        output_module_187 = self.module_201(output_module_187)
        output_module_187 = self.module_202(dim=1, tensors=[output_module_187,output_module_190])
        output_module_187 = self.module_203(output_module_187)
        output_module_187 = self.module_205(output_module_187)
        output_module_206 = self.module_206(output_module_187)
        output_module_206 = self.module_208(output_module_206)
        output_module_206 = self.module_209(output_module_206)
        output_module_206 = self.module_211(output_module_206)
        output_module_206 = self.module_212(dim=1, tensors=[output_module_206,output_module_163])
        output_module_213 = self.module_213(output_module_206)
        output_module_213 = self.module_215(output_module_213)
        output_module_216 = self.module_216(output_module_206)
        output_module_216 = self.module_218(output_module_216)
        output_module_213 = self.module_219(output_module_213)
        output_module_213 = self.module_221(output_module_213)
        output_module_213 = self.module_222(output_module_213)
        output_module_213 = self.module_224(output_module_213)
        output_module_213 = self.module_225(output_module_213)
        output_module_213 = self.module_227(output_module_213)
        output_module_213 = self.module_228(dim=1, tensors=[output_module_213,output_module_216])
        output_module_213 = self.module_229(output_module_213)
        output_module_213 = self.module_231(output_module_213)
        output_module_232 = self.module_232(output_module_213)
        output_module_232 = self.module_234(output_module_232)
        output_module_232 = self.module_235(output_module_232)
        output_module_232 = self.module_237(output_module_232)
        output_module_232 = self.module_238(dim=1, tensors=[output_module_232,output_module_139])
        output_module_239 = self.module_239(output_module_232)
        output_module_239 = self.module_241(output_module_239)
        output_module_242 = self.module_242(output_module_232)
        output_module_242 = self.module_244(output_module_242)
        output_module_239 = self.module_245(output_module_239)
        output_module_239 = self.module_247(output_module_239)
        output_module_239 = self.module_248(output_module_239)
        output_module_239 = self.module_250(output_module_239)
        output_module_239 = self.module_251(output_module_239)
        output_module_239 = self.module_253(output_module_239)
        output_module_239 = self.module_254(dim=1, tensors=[output_module_239,output_module_242])
        output_module_239 = self.module_255(output_module_239)
        output_module_239 = self.module_257(output_module_239)
        output_module_258 = self.module_258(output_module_187)
        output_module_258 = self.module_260(output_module_258)
        output_module_261 = self.module_261(output_module_258)
        output_module_261 = self.module_263(output_module_261)
        output_module_261 = self.module_264(output_module_261)
        output_module_261 = self.module_266(output_module_261)
        output_module_261 = self.module_267(output_module_261)
        output_module_261 = self.module_269(output_module_261)
        output_module_261 = self.module_270(output_module_261)
        output_module_261 = self.module_272(output_module_261)
        output_module_261 = self.module_273(output_module_261)
        output_module_274 = self.module_274(output_module_258)
        output_module_274 = self.module_276(output_module_274)
        output_module_274 = self.module_277(output_module_274)
        output_module_274 = self.module_279(output_module_274)
        output_module_274 = self.module_280(output_module_274)
        output_module_274 = self.module_282(output_module_274)
        output_module_274 = self.module_283(output_module_274)
        output_module_274 = self.module_285(output_module_274)
        output_module_286 = self.module_286(output_module_274)
        output_module_287 = self.module_287(output_module_274)
        output_module_286 = self.module_288(dim=1, tensors=[output_module_286,output_module_287,output_module_261])
        output_module_286 = self.module_289(input=output_module_286)
        output_module_290 = self.module_290(output_module_213)
        output_module_290 = self.module_292(output_module_290)
        output_module_293 = self.module_293(output_module_290)
        output_module_293 = self.module_295(output_module_293)
        output_module_293 = self.module_296(output_module_293)
        output_module_293 = self.module_298(output_module_293)
        output_module_293 = self.module_299(output_module_293)
        output_module_293 = self.module_301(output_module_293)
        output_module_293 = self.module_302(output_module_293)
        output_module_293 = self.module_304(output_module_293)
        output_module_293 = self.module_305(output_module_293)
        output_module_306 = self.module_306(output_module_290)
        output_module_306 = self.module_308(output_module_306)
        output_module_306 = self.module_309(output_module_306)
        output_module_306 = self.module_311(output_module_306)
        output_module_306 = self.module_312(output_module_306)
        output_module_306 = self.module_314(output_module_306)
        output_module_306 = self.module_315(output_module_306)
        output_module_306 = self.module_317(output_module_306)
        output_module_318 = self.module_318(output_module_306)
        output_module_319 = self.module_319(output_module_306)
        output_module_318 = self.module_320(dim=1, tensors=[output_module_318,output_module_319,output_module_293])
        output_module_318 = self.module_321(input=output_module_318)
        output_module_239 = self.module_322(output_module_239)
        output_module_239 = self.module_324(output_module_239)
        output_module_325 = self.module_325(output_module_239)
        output_module_325 = self.module_327(output_module_325)
        output_module_325 = self.module_328(output_module_325)
        output_module_325 = self.module_330(output_module_325)
        output_module_325 = self.module_331(output_module_325)
        output_module_325 = self.module_333(output_module_325)
        output_module_325 = self.module_334(output_module_325)
        output_module_325 = self.module_336(output_module_325)
        output_module_325 = self.module_337(output_module_325)
        output_module_338 = self.module_338(output_module_239)
        output_module_338 = self.module_340(output_module_338)
        output_module_338 = self.module_341(output_module_338)
        output_module_338 = self.module_343(output_module_338)
        output_module_338 = self.module_344(output_module_338)
        output_module_338 = self.module_346(output_module_338)
        output_module_338 = self.module_347(output_module_338)
        output_module_338 = self.module_349(output_module_338)
        output_module_350 = self.module_350(output_module_338)
        output_module_351 = self.module_351(output_module_338)
        output_module_350 = self.module_352(dim=1, tensors=[output_module_350,output_module_351,output_module_325])
        output_module_350 = self.module_353(input=output_module_350)
        return output_module_286,output_module_318,output_module_350
