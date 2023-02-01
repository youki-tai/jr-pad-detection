# aktio-yolox
アクティオ案件のFPGA実装周り

## Requirements
- Ubuntu 20.04 lts (or 18.04 lts)
- GPU (Tutorials use `RTX 2080Ti`)
- Memory: 32Gi~


## Terminology
- [Official YOLOX](https://github.com/Megvii-BaseDetection/YOLOX): リンク先の公式YOLOX
- [Vitis AI YOLOX](https://github.com/Xilinx/Vitis-AI/blob/2.5/model_zoo/model-list/pt_yolox_TT100K_640_640_73G_2.5/model.yaml): Vitis AIが提供するYOLOX 
※Vitis AI ver `2.0 & 2.5` にTT100Kのデモがある

## Get Started
### 1. Prepare for Vitis AI docker image
以下を参照してください.
https://github.com/tokyo-ai/aktio-yolovx/issues/1

Docker Imageを準備後, Vitis AIのディレクトリ上でこのレポジトリをcloneする. 
```shell
cd Vitis-AI
git clone git@github.com:tokyo-ai/aktio-yolox.git
```

### 2. Run docker image
上記`Vitis-AI`ディレクトリにおいて
```shell
./docker_run.sh xilinx/vitis-ai-gpu:2.0.0.1103
```

### 3. Python package settings
`/workspace`において
```shell
conda activate vitis-ai-pytorch
```

`/workspace/aktio-yolox`(このrepoをcloneしたもの)において
```shell
pip install --user -r requirements.txt
```

`/workspace/aktio-yolox/code`ディレクトリにおいて
```shell
pip install --user -v -e .
```

### 4. Modify experiment settings
`/workspace/aktio-yolox/code`ディレクトリにある`Makefile`に実験の設定を記述する. 
各用語
- `CFG`: モデル定義とepoch等の実験設定が記載されている. 実装済みのモデル定義一覧は[こちら](https://github.com/tokyo-ai/aktio-yolox/issues/21)
- `EXPERIMENT_NAME`: 結果が`YOLO_outputs/{EXPERIMENT_NAME}/*`に出力される. 

設定後, たとえば`float`での学習の際には
```
make train
```
を実行する. 学習, 評価, デモ, コンパイルが同じ方法で実行可能.   
**[注意]** コンパイル前にパッチを当ててください
https://github.com/tokyo-ai/aktio-yolox/issues/2#issuecomment-1383558678  
学習データセットは誰かからもらってください. 


## Documents
- [Environment Settings(Install GPU Driver + Docker & Build Vitis AI Docker Image)](https://github.com/tokyo-ai/aktio-yolovx/issues/1)
- [Vitis AI Tutorials for Training Vitis AI YOLOX-m](https://github.com/tokyo-ai/aktio-yolovx/issues/2) 
- Deployment Tutorials
  - [Vitis AI Tutorials](https://github.com/tokyo-ai/aktio-yolovx/issues/3)
  - [Deployment with Camera](https://github.com/tokyo-ai/aktio-yolox/issues/4)
- [Model Definition Files](https://github.com/tokyo-ai/aktio-yolox/issues/21) 
