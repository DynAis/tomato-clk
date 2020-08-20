# 01 - Python+Qt5项目环境的搭建

[TOC]

## 一. 软件

### 1. Pycharm 2019.3.3

​	Pycharm主要负责进行主体逻辑的编写, 以及统筹整个项目, 此外环境的搭建大多也在Pycharm里完成



### 2. Qt 5.12.7 / Qt Creator

​	Qt原本是为C++设计的UI界面搭建软件, 通过加入Py包之后同样也可以为Python编写桌面图形应用程序, 这里用的是官网的免费版



## 二. 环境搭建(对于已有Anaconda3)

### 1.Python解释器

由于已经安装了Anaconda3, 所以没有再安装原生的解释器, 也不清楚, 但觉得应该可以通用



### 2. 配置环境变量(对于Anaconda3)

对于Anaconda3的用户, 需要再自行配置一下环境变量, 在环境变量的`path`选项卡中添加Anaconda的以下目录

![image-20200408140342164](D:\WorkSpace\.Typora Images Hub\image-20200408140342164.png)

不然在Pycharm中搭建环境时会遇到提示pip无法成功的提示, 导致包无法安装



### 3. 在Pycharm里搭建环境/安装必要的包

完成以上两步准备就可以开始配置Pycharm了

首先新建一个项目

![image-20200408140546920](D:\WorkSpace\.Typora Images Hub\image-20200408140546920.png)

有几点需要注意的地方: 

**首先, 确保`New environment using`中是新建了一个环境,而不是使用Conda.** 

**其次, 确保`Base interpreter`中选择的是`pythonw`解释器, 而不是`python`**

**最后注意, 此处不需勾选**

![image-20200408141111529](D:\WorkSpace\.Typora Images Hub\image-20200408141111529.png)

然后就可以让它新建一个项目了





打开工程后进入 **文件 -> 设置 -> 项目 -> Project Interpreter** 在这里管理需要用到的包文件

<img src="D:\WorkSpace\.Typora Images Hub\image-20200408142236868.png" alt="image-20200408142236868" style="zoom:50%;" />

<img src="D:\WorkSpace\.Typora Images Hub\image-20200408142313603.png" alt="image-20200408142313603" style="zoom:50%;" />

需要使用Qt编程的话, 必须添加`QtPy`和`PyQt5`两个包

Pycharm会自己管理, 下载好就算是配置完成了



## 三. 工作流

大致的思路是:

- 使用Qt Creator创作图形界面
- 使用包内置函数转化Qt的.ui文件为.py文件, 作为包导入到程序中
- 使用Pycharm编写整体逻辑



### 1. 使用Qt Creator创作图形界面

打开Qt Creator新建工程

<img src="D:\WorkSpace\.Typora Images Hub\image-20200408142839431.png" alt="image-20200408142839431" style="zoom:50%;" />



注意创建时选择桌面图形应用, 这里不需要选Python的那个

<img src="D:\WorkSpace\.Typora Images Hub\image-20200408143012126.png" alt="image-20200408143012126" style="zoom:50%;" />



 工程最好命名为`ui`, 保存在一个项目文件夹下



### 2. 使用包内置函数转化Qt的.ui文件为.py文件, 作为包导入到程序中

在Pycharm中新建一个`builder.py`文件

```python
from qtpy import uic

uic.compileUiDir("这里填入Qt工程的文件夹路径")
```

运行便可以得到一个.py文件, 里面是应用程序外观的描述



在主程序py文件中写入

```python
import sys
from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)	#设置一个App

window = QtWidgets.QMainWindow()	#新建一个窗口
ui_window = Ui_MainWindow()	#新建一个导入包中窗口的类
ui_window.setupUi(window)	#注意自己的窗口要填入括号
window.setWindowTitle("Tomato Clock v0")	#设置标题

window.show()	#显示窗口

sys.exit(app.exec_())	#设置退出
```

设置完成