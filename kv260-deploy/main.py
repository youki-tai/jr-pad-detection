

import cv2
import vitis_ai_yolovx_wr

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("xmodel_bolt/bolt_sample_416.avi")

yolovx_obj = vitis_ai_yolovx_wr.yolovx_wr("tsd_yolox_pt.xmodel")

while True:
    retval,frame = cap.read()
    if not retval:
        cv2.waitKey(10)
        continue
    
    ## 画サイズ取得
    height,width = frame.shape[0],frame.shape[1]

    ## 2次元に変換してC++にわたす
    frame_2d = frame.reshape(frame.shape[0],frame.shape[1]*frame.shape[2])
    yolovx_obj.detections(frame_2d) ## 2次元

    ## BBOX描画
    for roi in range(yolovx_obj.num()):
        bbox = yolovx_obj.bbox(roi)
        xmin = int(bbox[0])
        ymin = int(bbox[1])
        xmax = int(bbox[2])
        ymax = int(bbox[3])
        cv2.rectangle(frame,
                      (xmin,ymin),
                      (xmax,ymax),
                      (0,255,0),
                      3,
                      3,
                      0)
        
    cv2.imshow("yolovx",frame)
    if cv2.waitKey(1)=='q':
        break
    

    

