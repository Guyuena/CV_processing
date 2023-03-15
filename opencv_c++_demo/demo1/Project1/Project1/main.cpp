#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

int main1()
{
    //OpenCV°æ±¾ºÅ
    cout << "OpenCV_Version: " << CV_VERSION << endl;

    //¶ÁÈ¡Í¼Æ¬
    Mat img = imread("C:\\Users\\jc\\Pictures\\yjtp.png");

    imshow("picture", img);
    waitKey(0);
    return 0;
}
