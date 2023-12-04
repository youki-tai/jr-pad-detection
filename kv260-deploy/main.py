import cv2
import vitis_ai_yolovx_wr

#cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("xmodel_bolt/bolt_sample_416.avi")
cap = cv2.VideoCapture("test.webm")
#frame = cv2.imread('val2017/00198.png')
yolovx_obj = vitis_ai_yolovx_wr.yolovx_wr("compiled-yolox-m/yolox-m.xmodel")
#yolovx_obj = vitis_ai_yolovx_wr.yolovx_wr("models/official-yolox-m/tsd_yolox_pt.xmodel")

#import time
colors = [(255,0,0),(0,255,0),(0,0,255)]
names = ["fixed_parts", "pad_b", "pad_a"]
mm_per_pix = 373./1920
off = 20
while True:
    retval,frame = cap.read()
    if not retval:
        cv2.waitKey(10)
        continue
    #height,width = frame.shape[0],frame.shape[1]

    ## prepare input mat for DPU
    frame_2d = frame.reshape(frame.shape[0],frame.shape[1]*frame.shape[2])
    #t0 = time.time()
    yolovx_obj.detection(frame_2d)
    #t = time.time() - t0
    #print(t/100*1000, 'ms')
    #print(100/t, 'fps')

    ## draw BBOX
    for roi in range(yolovx_obj.num()):
        bbox = yolovx_obj.bbox(roi)
        xmin, ymin = int(bbox[0]), int(bbox[1])
        xmax, ymax = int(bbox[2]), int(bbox[3])
        cls_num = int(bbox[4])
        conf = bbox[5]
        print(cls_num)
        if cls_num==0: offy = 20
        else:          offy = -45
        cv2.rectangle(frame, (xmin,ymin), (xmax,ymax), colors[cls_num],
                thickness=2, lineType=cv2.LINE_4, shift=0)
        cv2.putText(frame, f'cls: {names[cls_num]}', (xmin, ymin+offy), cv2.FONT_HERSHEY_PLAIN,
                fontScale=1.5, color=(255, 255, 255), thickness=1, lineType=cv2.LINE_AA)
        cv2.putText(frame, f'conf: {conf*100:.1f}%', (xmin, ymin+offy+off*1), cv2.FONT_HERSHEY_PLAIN,
                fontScale=1.5, color=(255, 255, 255), thickness=1, lineType=cv2.LINE_AA)
        if cls_num!=0:
            length = mm_per_pix * (bbox[2]-bbox[0])
            cv2.putText(frame, f'length: {length:.1f}mm', (xmin, ymin+offy+off*2), cv2.FONT_HERSHEY_PLAIN,
                    fontScale=1.5, color=(255, 255, 255), thickness=1, lineType=cv2.LINE_AA)
        
    cv2.imshow("yolovx",frame)
    if cv2.waitKey(1)=='q':
        break

