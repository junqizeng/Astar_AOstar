# 人工智能导论作业：A\*、AO\* 算法实现

## 作业介绍

### 实验所用编程语言和工具库

Python 3.6.0

除系统工具库用来实现可视化效果或实现优先队列外，本作业没有使用其他第三方工具库，可直接运行

### 作业内容

实现A\*算法和AO\*算法，并对结果提供一定可视化

1. 本作业在实现A*算法时，设置游戏迷宫地图，示意图如图：
   
   <img title="" src=".\images\迷宫示意.png" alt="迷宫示意" style="zoom: 33%;" data-align="center" width="456">
   
   从蓝色起点出发，将通过A*算法寻找到最短到达红色终点的道路。

2. 本作业在实现AO*算法时，设置如图与或图：
   
   <img title="" src=".\images\与或图示意.png" alt="与或图示意" style="zoom: 50%;" data-align="center" width="442">
   
   从n0出发，将通过AO*算法寻找到使n0能解的代价最小的路径组合。结点上标记为结点的h'值。

### 程序文件

AI_Astar_AOstar

​        ├── main.py            主函数文件，设置问题背景并调用算法解决问题

​        ├── Astar.py            A\*算法实现文件，包括核心函数Astar()及其他工具函数

​        ├── AOstar.py         AO\*算法实现文件，包括核心函数AOstar()及其他工具函数

## 程序使用

下载代码后，为保证结果可视化效果请在终端下运行

A\*算法使用（默认使用A\*算法）：

```c
python ./main --algorithm Astar
```

AO\*算法使用：

```
python ./main --algorithm AOstar
```

## 程序结果

A\*算法会展示搜索过程。红色方块代表墙壁，黄色方块代表起点，紫色方块代表终点，绿色代表搜索边界，蓝色代表已访问过的位置。示意动图如图：

<img title="" src=".\images\Astar输出.gif" alt="Astar输出" style="zoom: 80%;" data-align="center">

AO\*算法会展示搜索过程中路径标记顺序和最终的路径选择结果：

<img title="" src=".\images\AOstar输出.gif" alt="AOstar输出" style="zoom: 67%;" data-align="center" width="290">


