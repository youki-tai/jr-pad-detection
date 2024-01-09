#include <Eigen/Dense>
#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <Eigen/Core>
#include <opencv2/core/eigen.hpp>
#include <vitis/ai/yolovx.hpp>



#include <vitis/ai/nnpp/yolovx.hpp>
#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>

#include <pybind11/stl.h>
#include <pybind11/complex.h>
#include <pybind11/functional.h>

#define VERSION "20240109jr"

using Image8bpp =
  Eigen::Matrix<uint8_t,Eigen::Dynamic,Eigen::Dynamic,Eigen::RowMajor>;

namespace py = pybind11;

class yolovx_wr{
  std::unique_ptr<vitis::ai::YOLOvX>  yolovx_obj;
  vitis::ai::YOLOvXResult  result;
  std::vector< vitis::ai::YOLOvXResult>   results;  
public:
  yolovx_wr(const std::string &name){
    yolovx_obj = vitis::ai::YOLOvX::create(name);
  }
  auto version(){
    return VERSION;
  }

  auto detection(const Image8bpp& x){
    cv::Mat frame;
    cv::eigen2cv(x,frame);
    //printf("%d %d %d\n",frame.cols,frame.rows,frame.channels());
    
    frame = frame.reshape(3,frame.rows);

    //printf("%d %d %d\n",frame.cols,frame.rows,frame.channels());

    result = yolovx_obj->run(frame);
  }
  
  auto detections(const std::vector< Image8bpp> & x){
    std::vector< cv::Mat>  frames(x.size());
    for (unsigned int i=0;i<x.size() ;i++){
      cv::eigen2cv(x[i],frames[i]);
      //printf("%d %d %d\n",frame.cols,frame.rows,frame.channels());
      
      frames[i] = frames[i].reshape(3,frames[i].rows);
    }
    //printf("%d %d %d\n",frame.cols,frame.rows,frame.channels());

    results = yolovx_obj->run(frames);
  }
  auto num_results(){
    return results.size();
  }
  
  auto num(){
    return result.bboxes.size();
  }
  auto bbox(int i){
    std::vector<float> bbox_pos(10);
    bbox_pos[0] = result.bboxes[i].box[0]; // x0
    bbox_pos[1] = result.bboxes[i].box[1]; // y0 
    bbox_pos[2] = result.bboxes[i].box[2]; // x1
    bbox_pos[3] = result.bboxes[i].box[3]; // y1
    bbox_pos[4] = result.bboxes[i].label;  // label
    bbox_pos[5] = result.bboxes[i].score;  // score
    return bbox_pos;
  }
  
  auto bbox_list(){
    std::vector< std::vector<float> > bbox_lst(num());
    for (unsigned int i=0;i<num();i++){
      bbox_lst[i] = bbox(i);
    }
    return bbox_lst;
  }

  
  auto num_bboxes(int i){
    return results[i].bboxes.size();
  }
  
  auto bboxes(int res,int i){
    std::vector<float> bbox_pos(10);
    bbox_pos[0] = results[res].bboxes[i].box[0]; // x0
    bbox_pos[1] = results[res].bboxes[i].box[1]; // y0 
    bbox_pos[2] = results[res].bboxes[i].box[2]; // x1
    bbox_pos[3] = results[res].bboxes[i].box[3]; // y1
    bbox_pos[4] = results[res].bboxes[i].label;  // label
    bbox_pos[5] = results[res].bboxes[i].score;  // score
    return bbox_pos;
  }
  
	auto getInputSize(){
    std::vector<int> ret{yolovx_obj->getInputHeight(), yolovx_obj->getInputWidth()};
		return ret;
	}

  
};

PYBIND11_MODULE(vitis_ai_yolovx_wr,m) {
  py::class_<yolovx_wr>(m,"yolovx_wr")
    .def(py::init<const std::string &>())
    .def("version",&yolovx_wr::version)
    .def("detection",&yolovx_wr::detection)
    .def("detections",&yolovx_wr::detections)
    .def("num_results",&yolovx_wr::num_results)
    .def("num",&yolovx_wr::num)
    .def("bbox",&yolovx_wr::bbox)
    .def("bbox_list",&yolovx_wr::bbox_list)
    .def("num_bboxes",&yolovx_wr::num_bboxes)
    .def("bboxes",&yolovx_wr::bboxes)
    .def("get_input_size",&yolovx_wr::getInputSize)
    ;
}
    
  
