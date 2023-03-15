# 1、VS2019配置opencv

[(77条消息) VS2019下配置OpenCV（一次配置永久使用）_vs2019 opencv_zy010101的博客-CSDN博客](https://blog.csdn.net/zy010101/article/details/104838036)





<img src="C:\Users\jc\AppData\Roaming\Typora\typora-user-images\image-20230315150009000.png" alt="image-20230315150009000" style="zoom:50%;" />

![image-20230315150024636](C:\Users\jc\AppData\Roaming\Typora\typora-user-images\image-20230315150024636.png)

使用属性管理器进行配置的话，注意使用是 debug还是release版本





将工程配置好后可以作为一个 样本工程example，以后就复制这个工程就能进行二次开发，无需再次配置

![image-20230315151934763](C:\Users\jc\AppData\Roaming\Typora\typora-user-images\image-20230315151934763.png)







## （2）添加已有的属性配置



1、新建工程

<img src="C:\Users\jc\AppData\Roaming\Typora\typora-user-images\image-20230315151000604.png" alt="image-20230315151000604" style="zoom:50%;" />

2、有时候没有显示“属性管理器”，去这里调出来

<img src="C:\Users\jc\AppData\Roaming\Typora\typora-user-images\image-20230315151102910.png" alt="image-20230315151102910" style="zoom: 50%;" />

3、添加已有配置

<img src="C:\Users\jc\AppData\Roaming\Typora\typora-user-images\image-20230315151203073.png" alt="image-20230315151203073" style="zoom:50%;" />

4、找到已有开发工程同样的配置文件 “xxxx.props"

<img src="C:\Users\jc\AppData\Roaming\Typora\typora-user-images\image-20230315151235023.png" alt="image-20230315151235023" style="zoom:50%;" />

5、不过这种添加别的工程以后的属性配置虽然能正常工作，但这个属性文件没有被拷贝到本工程中，所以最后是先把属性配置文件先复制到当前工程再添加近来



空

<img src="C:\Users\jc\AppData\Roaming\Typora\typora-user-images\image-20230315151719645.png" alt="image-20230315151719645" style="zoom:50%;" />

复制过来

<img src="C:\Users\jc\AppData\Roaming\Typora\typora-user-images\image-20230315151801162.png" alt="image-20230315151801162" style="zoom:50%;" />





# 注意事项：

**在进行git保存时，需要把.vs目录删除，不然工程会非常大**

![image-20230315153151748](C:\Users\jc\AppData\Roaming\Typora\typora-user-images\image-20230315153151748.png)

![image-20230315153208491](C:\Users\jc\AppData\Roaming\Typora\typora-user-images\image-20230315153208491.png)