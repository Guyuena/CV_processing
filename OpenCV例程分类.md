- tutorial_code: opencv教程代码
  3calibration.cpp: 同时标定三台水平放置的相机，根据自带的函数提取角点后定标，效果很不好。
  application_trace.cpp: 类似于边缘检测
  bgfg_segm.cpp: 演示高斯混合背景检测算法的使用方式，跟踪运动做前背景分割。
  calibration.cpp: 完整的多用途标定程序
  camshiftdemo.cpp: 读取实时的摄像头数据，并演示基于均值偏移算法的视频跟踪。
  cloning_demo.cpp: 命令行模式的图像克隆。
  cloning_gui.cpp: 图形界面交互的图像克隆。
  connected_components.cpp: 查找并绘制图像中的连通区域。
  contours2.cpp: 查找并绘制图像中的轮廓。
  convexhull.cpp: 查找并绘制由点的集合组成的凸包。
  cout_mat.cpp: 使用cout 来输出各种格式化的 Mat 对象。
  create_mask.cpp: 演示如何创建黑白掩码图像，截取。
  dbt_face_detection.cpp: 基于检测的人脸跟踪代码。
  delaunay2.cpp: 通过鼠标交互式地生成 Delaunay 三角形。
  demhist.cpp: 演示直方图的用法。
  detect_blob.cpp: 斑点检测，该程序演示了如何使用BLOB来检测和过滤区域。
  detect_mser: 该程序演示了如何使用MSER来检测极端区域
  dft.cpp: 演示一幅图像的离散傅里叶变换。
  digits.cpp: SVM和KNearest的数字识别
  dis_opticalflow.cpp: 无光流
  distrans.cpp: 显示边缘图像的距离变换值，计算输入图像所有非零元素和其最近的零元素的距离。
  drawing.cpp: 演示绘画和文字显示功能，简单的画点、线、文字等。
  edge.cpp: 演示Canny 边缘检测，通过滑动条调节阈值，利用Canny检测图像边缘后显示。
  em.cpp: 对随机生成的数据点进行 EM 聚类。
  facedetect.cpp: 人脸检测。根据已训练好的分类器对人脸图像进行检测，用不同颜色的圆形框或矩形框标记出检测出的五官
  facial_features: 面部特征检测。
  falsecolor.cpp: 该程序演示了applyColorMap函数的用法。
  fback.cpp: 实时的Farneback 光流跟踪，该程序演示了Gunnar Farneback的密集光流算法。
  ffilldemo.cpp: 演示 floodFill() 像素填充算法。
  filestorage.cpp: 演示序列化到外部文件，如yml、xml等。
  fitellipse.cpp: 将轮廓点匹配到椭圆，椭圆拟合，查找图像轮廓图形。
  grabcut.cpp: 演示GrabCut 分割算法。
  image_alignment.cpp: 演示 findTransformECC() 函数。该文件演示了ECC图像对齐算法的使用。 当给出一个图像时，模板图像是通过随机扭曲人工形成的。 当给出两个图像时，可以通过命令行解析来初始化扭曲。 如果缺少inputWarp，则身份转换将初始化算法。
  imagelist_creator.cpp: 创建图像列表到 xml 文件。
  imagelist_reader.cpp: 该程序使您开始能够从文件列表中读取图像。
  inpaint.cpp: 使用鼠标交互地进行图像修补。
  kalman.cpp: 使用卡尔曼滤波进行二维跟踪，先建立运动模型和观察模型，对绕圆周运动的一维点跟踪，算法结果显示了估计点和实际点的连线。
  kmeans.cpp: Kmeans 聚类算法的演示，在平面上产生随机点后用K-means算法作聚类迭代，由于聚类中心也是随机产生的，可知效果很不好。
  laplace.cpp: 拉普拉斯边缘检测，由滑动条调整阈值，先对图像作滤波（高斯，均值，中值），后Laplace检测边缘。参数sigma=2时效果最好。
  letter_recog.cpp: 字母识别，演示训练各种不同的分类器，使用uci的字符库数据集。
  lkdemo.cpp: 目标跟踪，演示Lukas-Kanade光流法。
  logistic_regression.cpp: 逻辑回归算法，对数字进行识别，有训练集和数据集。
  mask_tmpl.cpp: 该程序演示了模板与掩码匹配的用法。
  matchmethod_orb_akaze_brisk.cpp: 该程序演示了如何检测计算并匹配ORB BRISK和AKAZE描述符。
  minarea.cpp: 寻找最小包围盒、包围圆,产生随机点后计算包含所有点的面积最小的圆和矩形
  morphology2.cpp: 形态学基本运算，包括开/闭运算，膨胀/腐蚀运算。
  neural_network: 简单的神经网络。
  npr_demo.cpp: 演示各种非真实感渲染效果。
  opencv_version.cpp: 输出 OpenCV 库的版本号
  pca.cpp: 基于 PCA 的人脸识别
  peopledetect.cpp: 基于 cascade 或 hog 进行行人或人体检测
  phase_corr.cpp: 演示 phaseCorrelate() 函数，基于相位的相关图像运动方位跟踪程序。
  points_classifier.cpp: 演示各种机器学习算法，鼠标点击给定点和类。
  polar_transform.cpp: 线性坐标和极坐标相互转换。可以从摄像头捕捉图像。
  qrcode.cpp: 该程序使用OpenCV库从相机或图像中检测QR码
  segment_objects.cpp: 实时地在视频或相机画面中检测前景物体>
  select3dobj.cpp： 在一个有标定棋盘的桌子上，使用3D Box标记一个对象，在所有序列帧中，只要照相机可以看到棋盘，就可以跟踪对象，并用Box分割对象。
  smiledetect.cpp: 该程序演示微笑检测
  squares.cpp: 检测图像中的方块形状。
  stereo_calib.cpp: 双目视觉的标定
  stereo_match.cpp: 计算左右视觉的图像的差异，生成点云文件。
  stitching.cpp: 演示图像拼接算法。
  stitching_detailed.cpp: 演示更多参数的图像拼接算法。
  train_HOG.cpp: 训练 HOG 分类器。
  train_svmsgd.cpp: 训练SVM，SGD分类器，左键黄点，右键蓝点。
  travelsalesman.cpp: 推销员路径规划问题。
  tree_engine.cpp: 演示如何使用不同的决策树和森林包括Boosting和随机树
  videocapture_basic.cpp: 简单的相机捕获。
  videocapture_camera.cpp: 相机捕获。
  videocapture_gphoto2_autofocus.cpp: 该程序演示了gPhoto2 VideoCapture的用法。
  videocapture_gstreamer_pipeline.cpp: 此程序使用不同的后端OpenCV测量视频编码和解码的性能。
  videocapture_image_sequence.cpp: 此示例向您展示如何使用VideoCapture界面读取图像序列。
  videocapture_intelperc.cpp: 该程序演示了英特尔感知计算SDK支持的摄像头的用法。
  videocapture_openni.cpp: 该程序演示了深度传感器（Kinect，XtionPRO，…）的用法。
  videocapture_starter.cpp: 该程序从连接到计算机的视频文件，图像序列（01.jpg，02.jpg … 10.jpg）或相机捕获帧。
  videowriter_basic.cpp: 使用VideoWriter和VideoCapture的非常基本的示例。
  warpPerspective_demo.cpp: 简短的演示程序展示了透视变换如何应用于图像。
  watershed.cpp: 演示著名的分水岭图像分割算法
