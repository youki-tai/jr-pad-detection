PY_INCLUDES := `python3 -m pybind11 --includes`
SUFFIX := `python3-config --extension-suffix`
all:
	g++ -std=c++17 -O3 -Wall -shared -std=c++17 -fPIC $(PY_INCLUDES) cpp/vitis_ai_yolovx_wr.cpp -o vitis_ai_yolovx_wr$(SUFFIX)   \
	    -I/usr/include/opencv4 \
	    -I/usr/include/eigen3 \
	   -lpthread \
	   -lopencv_core \
	   -lopencv_video \
	   -lopencv_videoio \
	   -lopencv_imgproc \
	   -lopencv_imgcodecs \
	   -lopencv_highgui \
	   -lvitis_ai_library-yolovx
clean:
	rm vitis_ai_yolovx_wr$(SUFFIX)

