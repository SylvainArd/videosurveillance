#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/objdetect/objdetect.hpp"
#include "opencv2/highgui/highgui.hpp"
#include <fstream>
#include <iostream>
#include <ctype.h>
#include <iostream>
#include <dirent.h>
#include <sys/types.h>
#include <stdio.h>
#include <string.h>
//#include "openCVUtils.h"

using namespace cv;
using namespace std;



static Mat _inImage;
static Mat _outImage;

static    HOGDescriptor _hog;
static const char* _windowName = "people detector";
static float _hitThreshold = 0;
static float _scaleFactor = 1.059;
static float _groupThreshold = 0.0;
static int MAX_TRACKBAR = 200;
static int _trackbar1 = _scaleFactor * MAX_TRACKBAR/2.0;
static string _pathImage;
struct MatchPathSeparator
{
    bool operator()( char ch ) const
    {
        return ch == '/';
    }
};

std::string
gnu_basename( std::string const& pathname )
{
    return std::string( 
        std::find_if( pathname.rbegin(), pathname.rend(),
                      MatchPathSeparator() ).base(),
        pathname.end() );
}



static int imshowWithCaption(const char* windowName, Mat inImage,  const char* caption )
{
    putText( inImage, caption,
            Point( MIN(10,inImage.cols), MIN(20,inImage.rows)),
            FONT_HERSHEY_PLAIN, 1, Scalar(0, 0, 255) );
    
    imshow( windowName, inImage );
    return 0;
}

static void hogDetect () {
    _inImage.copyTo(_outImage);
     vector<Rect> found;
     vector <Rect> found_filtered;
    _hog.detectMultiScale(
                          _inImage //const Mat&
                          //Matrix of the type CV_8U containing an image where objects are detected.
                          , found // vector<Rect>& objects
                          //Vector of rectangles where each rectangle contains the detected object.
                          , _hitThreshold  // hit_threshold=0
                          //hit_threshold – Threshold for the distance between features and SVM classifying plane.  Usually it is 0 and should be specfied in the detector coefficients (as the last free coefficient). But if the free coefficient is omitted (which is allowed), you can specify it manually here.
                       
                          , Size(8,8)//winSize
                          //win_stride – Window stride. It must be a multiple of block stride
                          , Size(32,32)//padding
                          //padding – Mock parameter to keep the CPU interface compatibility. It must be (0,0).
                          , _scaleFactor  // double scale = 1.05
                          //scale0 – Coefficient of the detection window increase.
                             //scaleFactor - Parameter specifying how much the image size is reduced at each image scale.
                          , _groupThreshold  //group_threshold=2
                          //group_threshold – Coefficient to regulate the similarity threshold. When detected, some objects can be covered by many rectangles. 0 means not to perform grouping. See groupRectangles() .
                          );
    
    size_t i, j;


    
    
    for( i = 0; i < found.size(); i++ )
    {
        Rect r = found[i];
        for( j = 0; j < found.size(); j++ ) {
            //filter out overlapping rectangles
            if ( j!=i ) {
            Rect iRect =  r;
            Rect jRect = found[j];
            Rect intersectRect = (iRect & jRect);
            if (intersectRect.area()>=iRect.area()*0.9) break;
            }
        }
        if( j == found.size() )
            found_filtered.push_back(r);
    }
    for( i = 0; i < found_filtered.size(); i++ )
    {
        Rect r = found_filtered[i];
        // the HOG detector returns slightly larger rectangles than the real objects.
        // so we slightly shrink the rectangles to get a nicer output.
        r.x += cvRound(r.width*0.5);
        // hacky shift right by 40px - rects seem to be shifted consistently
        r.x +=-40;
        r.width = cvRound(r.width*0.3);
        r.y += cvRound(r.height*0.07);
        r.height = cvRound(r.height*0.8);
        rectangle(_outImage, r.tl(), r.br(), cv::Scalar(0,255,0), 3);
    }
    //eliminate overlaps
    
    //imshow(_windowName, _outImage);
    
    imshow(_windowName, _outImage);
    cout<<"ok"<<"../image_code3/"+gnu_basename(_pathImage)<<endl;
    imwrite("../image_code3/"+gnu_basename(_pathImage),_outImage);

}



static void hogTrackbarCallback1 (int trackbarPos, void*) {
    _trackbar1 = trackbarPos;
    _scaleFactor = trackbarPos/100.0;
    hogDetect();
}


static void setupHogWindow() {
    
    namedWindow( _windowName, WINDOW_AUTOSIZE );
   
    createTrackbar( "scaleFactor" //– Name of the created trackbar.
                   , _windowName  //– Name of the window that will be used as a parent of the created trackbar.
                   , &_trackbar1 //– Optional pointer to an integer variable whose value reflects the position of the slider. Upon creation, the slider position is defined by this variable.
                   , MAX_TRACKBAR  //– Maximal position of the slider. The minimal position is always 0.
                   , hogTrackbarCallback1  //– Pointer to the function to be called every time the slider changes position. This function should be prototyped as void Foo(int,void*); , where the first parameter is the trackbar position and the second parameter is the user data (see the next parameter). If the callback is the NULL pointer, no callbacks are called, but only value is updated.
                   , NULL// – User data that is passed as is to the callback. It can be used to handle trackbar events without using global variables.
                   );
}

int main(int argc, char** argv) {
    DIR *dir = opendir("../images/");
	struct dirent *entry ;
	while(entry = readdir(dir)) {
		char  filename[300];
		strcpy(filename,"../images/");
		cout<<filename<<endl;
		strcat(filename,entry->d_name);
		cout <<filename<<endl;
		string s(filename);
		if ((strcmp(entry->d_name,".")==0)||(strcmp(entry->d_name,"..")==0))
			continue;
		_pathImage=s;
		_inImage=imread(s,CV_LOAD_IMAGE_COLOR);
		    //_hog = HOGDescriptor::HOGDescriptor();
		    _hog.setSVMDetector(HOGDescriptor::getDefaultPeopleDetector());
		    namedWindow(_windowName, 1);
		    setupHogWindow();
		    hogDetect();
		waitKey(0);
	}
	return 0;
}

    
    

