#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;

int main()
{
	//���е�·�����忴�����ͼƬ��·��
	Mat src = imread("yjtp.png");
	if (src.empty())
	{
		printf("could not load image...\n");
		return 0;
	}
	else
	{
		imshow("image", src);
	}

	waitKey(0);
	return 0;
}