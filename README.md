# 人工智能导论作业：A*、AO* 算法实现

## 作业介绍

### 实验所用编程语言、环境和工具库

Python 3.6.0

除系统工具库用来实现可视化效果或实现优先队列外，本作业没有使用其他第三方工具库，可直接运行

github链接：[GitHub - junqizeng/Astar_AOstar: 使用pyhton实现A\*和AO\*](https://github.com/junqizeng/Astar_AOstar)

### 作业内容

实现A\*算法和AO\*算法，对算法实现进行可视化和交互演示，程序打包成exe可执行文件：

1. 本作业在实现A\*算法时，设置游戏迷宫地图，示意图如图：
   
   从蓝色起点出发，将通过A\*算法寻找到最短到达红色终点的道路。

2. 本作业在实现AO\*算法时，设置如图与或图：
   
   从n0出发，将通过AO\*算法寻找到使n0能解的代价最小的路径组合。结点上标记为结点的h'值。

### 程序文件结构说明

AI_Astar_AOstar

 ├── main.py   主函数文件，程序入口

 ├── mywork.py   封装文件，将各可视化窗口和功能函数进行综合封装，供程序入口调用

 ├── algorithms   算法功能函数文件夹

            ├──Astar.py   A\*算法实现文件，包括核心函数Astar()及其他工具函数

​            ├── AOstar.py   AO\*算法实现文件，包括核心函数AOstar()及其他工具函数

 ├── vis_windows 可视化窗口文件夹

## 程序使用

在windows环境下，可直接运行打包好的Astar_AOstar.exe

下载代码后，在程序文件夹下，直接运行main.py

```
python ./main
```

## 运行结果及说明

### 初始界面

<img title="" src="file:///./readme_imgs/0.png" alt="" width="482" data-align="center">

在该界面下可点击A\*算法、AO\*算法选择要执行的算法

### A\*算法

A\*算法演示时，使用A\*算法对提前设定好的迷宫进行寻路。

实现的思路是，在进入A\*算法时，调用算法函数./algorithms/Astar.py，对设定好的迷宫进行寻路，并返回保存好的每步解。

然后根据用户的操作，对指定步骤解进行可视化，可视化迷宫为在线生成。

<img title="" src="file:///./readme_imgs/1.png" alt="" width="489" data-align="center">

### AO\*算法

AO\*算法演示时，使用AO\*算法对提前设定好的与或图进行求解。

实现的思路是，在进入AO\*算法时，调用算法函数./algorithms/AOstar.py，对设定好的与或图进行求解，并返回保存好的每步解。

然后根据用户的操作，对指定步骤解进行可视化。

需要说明的是，由于与或图用程序绘图的效果不是很好，因此程序中展示的与或图是由离线手动制作的，但搜索过程中的连接步骤是由程序在线计算得出，./algorithms/AOstar.py 是AO\*算法的具体实现。

<img title="" src="file:///./readme_imgs/2.png" alt="" data-align="center" width="495">

## 其他说明

之前没有可视化界面且只靠传参进行显示的版本，代码、readme等在文件夹Astar_AOstar_v1.0中
