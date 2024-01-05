## 初期設定
### compilation
vitis ai設定済みのデバイスで下記コマンドを実行し、cppライブラリをコンパイルする。
```
make
```

### xmodel, 入力ビデオ
[Release](../../releases/tag/v0.1a)からダウンロードしてkv260-deployフォルダに設置してください。

## 実行
下記コマンドで`test4img.webm`を入力として推論が行なえます。
```
python3 main.py --visualize
```
マルチスレッドの実行を確認した場合は下記。
```
python3 main_mp.py --visualize
```
オプション説明
- `--visualize`: 画面描画、bbox確認用
- `--video_path <file path>`: 入力ビデオのパス
- `--xmodel_path <file path>`: xmodelのパス
- `--camera`: カメラ入力で実行する場合セット
