import cv2
import vitis_ai_yolovx_wr
import numpy as np
from params import *
from main import PreProc
import argparse
import multiprocessing

class YOLOPredictorMP(multiprocessing.Process):
    def __init__(self, xmodel, queue, visualize=False):
        multiprocessing.Process.__init__(self)
        self.yolovx_obj = vitis_ai_yolovx_wr.yolovx_wr(xmodel)
        self.input_size = self.yolovx_obj.get_input_size()
        self.preproc = PreProc(self.input_size)
        self.queue = queue
        self.visualize=visualize

    def run(self):
        while True:
            pad_frame, frame_2d = self.queue.get()
            if not isinstance(frame_2d,np.ndarray): break
            self.frame_width = pad_frame.shape[1]
            self.yolovx_obj.detection(frame_2d) ## 2次元
            res = self.check_length()
            print(res)
            if self.visualize:
                self.draw_bbox(pad_frame)
                cv2.imshow("yolovx",pad_frame)
                if cv2.waitKey(1)=='q':
                    break

    def prepare(self, frame):
        frame = self.preproc.run(frame)
        self.frame_width = frame.shape[1]
        frame_2d = frame.reshape(frame.shape[0],frame.shape[1]*frame.shape[2])
        return frame_2d

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
    queue = multiprocessing.Queue()
    predictor = YOLOPredictorMP(args.xmodel_path, queue, args.visualize)
    predictor.start()

    preproc = predictor.preproc

    while True:
        retval,frame = cap.read()
        if not retval:
            queue.put((None, None))
            break;

        frame = preproc.run(frame)
        frame_2d = frame.reshape(frame.shape[0],frame.shape[1]*frame.shape[2])
        queue.put((frame, frame_2d))

    predictor.join()

