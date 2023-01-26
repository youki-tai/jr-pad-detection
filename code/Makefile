# GPU settings --------------------------------------------------
export CUDA_VISIBLE_DEVICES=0
# export CUDA_VISIBLE_DEVICES=0,1,2,3
GPU_NUM=1

# train(float) ---------------------------------------------------
FLOAT_BATCH_SIZE=8
# float
FLOAT_CFG=exps/aktio/vitis_ai_yolox/yolox_s_float.py
FLOAT_EXPERIMENT_NAME=vitis_ai_yolox_s_float

# PTQ ------------------------------------------------------------
PTQ_BATCH=8
PTQ_CFG=exps/aktio/vitis_ai_yolox/yolox_s_quant.py
PTQ_WEIGHTS=YOLOX_outputs/yolox_s_aktio_float/best_ckpt.pth
PTQ_DIR=quantized

# QAT ------------------------------------------------------------
QAT_BATCH_SIZE=4
# Aktio YOLOX-s
QAT_CFG=exps/aktio/vitis_ai_yolox/yolox_s_qat.py
QAT_EXPERIMENT_NAME=vitis_ai_yolox_s_qat

# eval -----------------------------------------------------------
EVAL_BATCH_SIZE=16
# aktio official yolox-s
EVAL_CFG=exps/aktio/yolox_s_float.py
# Vitis AI YOLOX-m specification
# EVAL_CFG=exps/example/custom/yolox_m_tt100k_float.py
# float
# WEIGHTS=./YOLOX_outputs/yolox_s_aktio_float/best_ckpt.pth
# qat
EVAL_WEIGHTS=./YOLOX_outputs/yolox_s_aktio_qat/best_ckpt.pth

# compile -----------------------------------------------------------
QAT_WEIGHTS=YOLOX_outputs/yolox_s_aktio_qat/best_ckpt.pth
CVT_DIR=aktio_converted_qat


hello: MODE=world
hello:
	echo "HELLO"

	echo ${MODE}/hello


train:
	python tools/train.py -expn ${FLOAT_EXPERIMENT_NAME} -f ${FLOAT_CFG} -b ${FLOAT_BATCH_SIZE} -d ${GPU_NUM} --fp16

ptq:
	# calib
	python tools/quant.py -expn ${FLOAT_EXPERIMENT_NAME} -f ${PTQ_CFG} -c ${PTQ_WEIGHTS} -b ${PTQ_BATCH} -d ${GPU_NUM} \ 
		--conf 0.001 --quant_mode calib --quant_dir ${PTQ_DIR}
	# test
	python tools/quant.py -f ${PTQ_CFG} -c ${PTQ_WEIGHTS} -b ${PTQ_BATCH} -d ${GPU_NUM} \ 
		--conf 0.001 --quant_mode test --quant_dir ${PTQ_DIR}


qat: W_QUANT=1
qat:
	python tools/train.py -expn ${QAT_EXPERIMENT_NAME} -f ${QAT_CFG} -d ${GPU_NUM} -b ${QAT_BATCH_SIZE}


eval:
	python tools/eval.py -f ${EVAL_CFG} -c ${EVAL_WEIGHTS} -b ${EVAL_BATCH_SIZE} -d 1 --conf 0.001


compile: W_QUANT=1
compile:
	echo "converted qat model"
	python tools/convert_qat.py -f ${QAT_CFG} -c ${QAT_WEIGHTS} --cvt_dir ${CVT_DIR}

	echo "test converted qat model"
	python tools/quant.py -f ${PTQ_CFG} -c ${Q_DIR}/converted_qat.pth -b ${BATCH_SIZE} -d ${GPU_NUM} \
		--conf 0.001 --quant_mode test --quant_dir ${CVT_DIR} --nndct_equalization=False --nndct_param_corr=False
		
	echo "dump xmodel for deployment"
	python tools/quant.py -f ${PTQ_CFG} -c ${Q_DIR}/converted_qat.pth -b ${BATCH_SIZE} -d ${GPU_NUM} \
		--conf 0.001 --quant_mode test --quant_dir ${CVT_DIR} --is_dump --nndct_equalization=False --nndct_param_corr=False





