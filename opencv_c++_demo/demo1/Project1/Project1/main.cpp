#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

int main1()
{
    //OpenCV�汾��
    cout << "OpenCV_Version: " << CV_VERSION << endl;

    //��ȡͼƬ
    Mat img = imread("C:\\Users\\jc\\Pictures\\yjtp.png");

    imshow("picture", img);
    waitKey(0);
    return 0;
}
