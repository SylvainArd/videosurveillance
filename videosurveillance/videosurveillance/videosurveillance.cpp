#include "opencv2/video/tracking.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/video/video.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/objdetect/objdetect.hpp"
#include <fstream>
#include <iostream>
#include <ctype.h>
#include <iostream>
#include <dirent.h>
#include <sys/types.h>
#include <string>
using namespace cv;
using namespace std;
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



int main( int argc, char** argv )
{
    
    Mat img;
    HOGDescriptor hog;
    hog.setSVMDetector(HOGDescriptor::getDefaultPeopleDetector());
 
    namedWindow("video capture", CV_WINDOW_AUTOSIZE);
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
		img=imread(s,CV_LOAD_IMAGE_COLOR);
 cout<<"ok";
        vector<Rect> found, found_filtered;
        hog.detectMultiScale(img, found, 0, Size(8,8), Size(32,32), 1.05, 2);
 
        size_t i, j;
        for (i=0; i<found.size(); i++)
        {
            Rect r = found[i];
            for (j=0; j<found.size(); j++)
                if (j!=i && (r & found[j])==r)
                    break;
            if (j==found.size())
                found_filtered.push_back(r);
        }
        for (i=0; i<found_filtered.size(); i++)
        {
	    Rect r = found_filtered[i];
            r.x += cvRound(r.width*0.1);
	    r.width = cvRound(r.width*0.8);
	    r.y += cvRound(r.height*0.06);
	    r.height = cvRound(r.height*0.9);
	    rectangle(img, r.tl(), r.br(), cv::Scalar(0,255,0), 2);
	}
        imshow("image", img);
        cout<<"ok"<<"../image_code4/"+gnu_basename(filename)<<endl;
    imwrite("../image_code4/"+gnu_basename(filename),img);
        waitKey(0);
  }
 closedir(dir);
}

