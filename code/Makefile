# GPU settings --------------------------------------------------
export CUDA_VISIBLE_DEVICES=0
# export CUDA_VISIBLE_DEVICES=0,1,2,3
GPU_NUM=1

# train(float) ---------------------------------------------------
FLOAT_BATCH_SIZE=64
FLOAT_CFG=exps/aktio/vitis_ai_yolox/yolox_nano_float.py
FLOAT_EXPERIMENT_NAME=vitis_ai_yolox_nano_float

# PTQ ------------------------------------------------------------
PTQ_BATCH=8
PTQ_CFG=exps/aktio/vitis_ai_yolox/yolox_s_quant.py
#TQ_WEIGHTS=YOLOX_outputs/${FLOAT_EXPERIMENT_NAME}/best_ckpt.pth
PTQ_WEIGHTS=./best_ckpt.pth
PTQ_EXPERIMENT_NAME=vitis_ai_yolox_s_ptq
PTQ_DIR=quantized_vitis_ai_yolox_s

# QAT ------------------------------------------------------------
QAT_BATCH_SIZE=4
QAT_CFG=exps/aktio/vitis_ai_yolox/yolox_s_qat.py
QAT_EXPERIMENT_NAME=vitis_ai_yolox_s_qat

# eval -----------------------------------------------------------
# NOTE: CFG can be for both float and qat.
EVAL_BATCH_SIZE=16
EVAL_CFG=exps/aktio/yolox_s_float.py
EVAL_WEIGHTS=./aktio-trained-model-2023-01-26/yolox_s_aktio_qat/best_ckpt.pth

# demo -----------------------------------------------------------
# 1: quant 0: float
DEMO_IS_QUANT=0
DEMO_CFG=exps/aktio/vitis_ai_yolox/yolox_s_float.py
# DEMO_OUTPUT_DIR
DEMO_WEIGHTS=aktio-trained-model-2023-01-26/yolox_s_aktio_float/best_ckpt.pth
# image
DEMO_INPUT_TYPE=image
DEMO_INPUT=aktio_datasets/AKTIO_1202_alldata_COCO_format/val2017/000000000003.jpg
# video
# DEMO_INPUT_TYPE=video
# DEMO_INPUT=./aktio_test_mv.mp4
CONFIDENCE=0.6
NMS=0.45

# dump -----------------------------------------------------------
# extract qat model and export to *.xmodel
DUMP_QAT_WEIGHTS=YOLOX_outputs/${QAT_EXPERIMENT_NAME}/best_ckpt.pth
DUMP_BATCHSIZE=16
DUMP_DIR=aktio_converted_qat

# compile -----------------------------------------------------------
COMPILE_XMODEL_PATH=${DUMP_DIR}/YOLOX_0_int.xmodel
COMPILE_ARCH_PATH=/opt/vitis_ai/compiler/arch/DPUCZDX8G/KV260/arch.json
COMPILE_OUTPUT_FILE_NAME=yolox-s
COMPILE_OUTPUT_DIR=compiled-yolox-s

train:
	python tools/train.py -expn ${FLOAT_EXPERIMENT_NAME} -f ${FLOAT_CFG} -b ${FLOAT_BATCH_SIZE} -d ${GPU_NUM} --fp16


ptq: export W_QUANT=1
ptq:
	# calib
	python tools/quant.py -expn ${PTQ_EXPERIMENT_NAME} -f ${PTQ_CFG} -c ${PTQ_WEIGHTS} -b ${PTQ_BATCH} -d ${GPU_NUM} --conf 0.001 --quant_mode calib --quant_dir ${PTQ_DIR}
	# test
	python tools/quant.py -expn ${PTQ_EXPERIMENT_NAME} -f ${PTQ_CFG} -c ${PTQ_WEIGHTS} -b ${PTQ_BATCH} -d ${GPU_NUM} --conf 0.001 --quant_mode test --quant_dir ${PTQ_DIR}


qat: export W_QUANT=1
qat:
	python tools/train.py -expn ${QAT_EXPERIMENT_NAME} -f ${QAT_CFG} -d ${GPU_NUM} -b ${QAT_BATCH_SIZE}


demo: export W_QUANT=${DEMO_IS_QUANT}
demo:
	python tools/demo_sign.py ${DEMO_INPUT_TYPE} -f ${DEMO_CFG} -c ${DEMO_WEIGHTS} --path ${DEMO_INPUT} --conf ${CONFIDENCE} --nms ${NMS} --save_result --device gpu


eval:
	python tools/eval.py -f ${EVAL_CFG} -c ${EVAL_WEIGHTS} -b ${EVAL_BATCH_SIZE} -d 1 --conf 0.001


dump: export W_QUANT=1
dump:
	echo "converted qat model"
	python tools/convert_qat.py -f ${QAT_CFG} -c ${DUMP_QAT_WEIGHTS} --cvt_dir ${DUMP_DIR}

	echo "test converted qat model"
	python tools/quant.py -f ${PTQ_CFG} -c ${DUMP_DIR}/converted_qat.pth -b ${DUMP_BATCHSIZE} -d ${GPU_NUM} --conf 0.001 --quant_mode test --quant_dir ${PTQ_DIR} --nndct_equalization=False --nndct_param_corr=False
		
	echo "dump xmodel for deployment"
	python tools/quant.py -f ${PTQ_CFG} -c ${DUMP_DIR}/converted_qat.pth -b ${DUMP_BATCHSIZE} -d ${GPU_NUM} --conf 0.001 --quant_mode test --quant_dir ${PTQ_DIR} --is_dump --nndct_equalization=False --nndct_param_corr=False


patch:
	sudo conda install -n vitis-ai-pytorch https://www.xilinx.com/bin/public/openDownload?filename=unilog-1.3.2-h7b12538_35.tar.bz2
	sudo conda install -n vitis-ai-pytorch https://www.xilinx.com/bin/public/openDownload?filename=target_factory-1.3.2-hf484d3e_35.tar.bz2
	sudo conda install -n vitis-ai-pytorch https://www.xilinx.com/bin/public/openDownload?filename=xir-1.3.2-py36h7b12538_47.tar.bz2
	sudo conda install -n vitis-ai-pytorch https://www.xilinx.com/bin/public/openDownload?filename=xcompiler-1.3.2-py36h7b12538_53.tar.bz2
	sudo conda install -n vitis-ai-pytorch https://www.xilinx.com/bin/public/openDownload?filename=xnnc-1.3.2-py36_48.tar.bz2


compile:
	vai_c_xir --xmodel ${COMPILE_XMODEL_PATH} --arch ${COMPILE_ARCH_PATH} --net_name ${COMPILE_OUTPUT_FILE_NAME} --output_dir ${COMPILE_OUTPUT_DIR}
