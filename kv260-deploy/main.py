import cv2
import vitis_ai_yolovx_wr
import numpy as np
from params import *
import argparse

class PreProc(object):
    def __init__(self, input_size):
        self.input_size = input_size
    def run(self, img):
        r = min(self.input_size[0] / img.shape[0], self.input_size[1] / img.shape[1] * 2)
        resized_size = int(img.shape[0] * r), int(img.shape[1] * r)
        resized_img = cv2.resize(img, resized_size[::-1], interpolation=cv2.INTER_LINEAR)
        bh = resized_img[-resized_size[0]//2:,...] #bottom half
        cat_img = cv2.vconcat([bh[:,:resized_size[1]//2,:], bh[:,-resized_size[1]//2:,:]])

        pad_b, pad_r = self.input_size[0]-cat_img.shape[0], self.input_size[1]-cat_img.shape[1]
        if pad_b!=0 or pad_r!=0:
            padded_img = cv2.copyMakeBorder(cat_img, 0, pad_b, 0, pad_r, cv2.BORDER_CONSTANT, value=(114,114,114))
        else:
            padded_img = cat_img

        return padded_img

class YOLOPredictor(object):
    def __init__(self, xmodel):
        self.yolovx_obj = vitis_ai_yolovx_wr.yolovx_wr(xmodel)
        self.input_size = self.yolovx_obj.get_input_size()
        self.preproc = PreProc(self.input_size)

    def predict(self, frame):
        frame = self.preproc.run(frame)
        self.frame_width = frame.shape[1]
        frame_2d = frame.reshape(frame.shape[0],frame.shape[1]*frame.shape[2])
        self.yolovx_obj.detection(frame_2d) ## 2次元
        return frame

    def check_length(self):
        boxli=np.array(self.yolovx_obj.bbox_list())
        if boxli.shape[0]==0: return None
        padli=boxli[boxli[:,4]!=0]
        if padli.shape[0]==0: return None
        lengthes = mm_width * (padli[:,2] - padli[:,0]) / self.frame_width
        is_left = padli[:,1]<self.input_size[0]//2
        ng = lengthes>=LENGTH_THRES_MM
        ngl = any(ng[is_left])
        ngr = any(ng[~is_left])
        return [ngl+1, ngr+1]

    def draw_bbox(self, frame):
        for roi in range(self.yolovx_obj.num()):
            bbox = self.yolovx_obj.bbox(roi)
            xmin, ymin = int(bbox[0]), int(bbox[1])
            xmax, ymax = int(bbox[2]), int(bbox[3])
            cls_num = int(bbox[4])
            conf = bbox[5]
            if cls_num==0: offy = OFFSET_Y[0]
            else:          offy = OFFSET_Y[1]
            cv2.rectangle(frame, (xmin,ymin), (xmax,ymax), colors[cls_num],
                    thickness=2, lineType=cv2.LINE_4, shift=0)
            cv2.putText(frame, f'cls: {names[cls_num]}', (xmin, ymin+offy), cv2.FONT_HERSHEY_PLAIN,
                    fontScale=FONTSCALE, color=(255, 255, 255), thickness=1, lineType=cv2.LINE_AA)
            cv2.putText(frame, f'conf: {conf*100:.1f}%', (xmin, ymin+offy+OFFSET*1), cv2.FONT_HERSHEY_PLAIN,
                    fontScale=FONTSCALE, color=(255, 255, 255), thickness=1, lineType=cv2.LINE_AA)
            if cls_num!=0:
                length = mm_width * (bbox[2]-bbox[0]) / self.frame_width
                cv2.putText(frame, f'length: {length:.1f}mm', (xmin, ymin+offy+OFFSET*2), cv2.FONT_HERSHEY_PLAIN,
                        fontScale=FONTSCALE, color=(255, 255, 255), thickness=1, lineType=cv2.LINE_AA)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video_path", "-v", default="test4img.webm", type=str)
    parser.add_argument("--xmodel_path", "-x", default="compiled-yolox-m/yolox-m.xmodel", type=str)
    parser.add_argument("--camera", action='store_true')
    parser.add_argument("--visualize", action='store_true')
    args = parser.parse_args()
    if args.camera:
        cap = cv2.VideoCapture(0)
    else:
        cap = cv2.VideoCapture(args.video_path)
    predictor = YOLOPredictor(args.xmodel_path)
    while True:
        retval,frame = cap.read()
        if not retval:
            break;

        pad_frame = predictor.predict(frame)
        res = predictor.check_length()
        print(res)

        if args.visualize:
            predictor.draw_bbox(pad_frame)
            cv2.imshow("yolovx",pad_frame)
            if cv2.waitKey(1)=='q':
                break
