# 02 - 番茄钟倒计时模块的基本实现

[TOC]

## 项目进度

- 实现了番茄钟最基本的倒计时功能
- 实现了按钮交互的功能

<img src="https://dynais-imh-hub.oss-cn-hangzhou.aliyuncs.com/img/20200725010712.png" alt="image-20200409231248203" style="zoom:50%;" />



## 一. 重要代码模块

### 1. 显示时间与计算时间的转换

实现倒计时时的一个问题是: 显示的时间格式需要是"XX:XX", 但是为了方便计算, 需要把这个格式的时间转化为秒数的形式, 这就需要一个显示时间与计算时间互相转换的模块

```python
# 显示时间转秒数 "XX:XX" -> flout
def tomato2sec(tomato):
    sec = int(tomato[3:])
    sec = sec + 60 * int(tomato[:2])
    return sec


# 秒数转显示时间 flout -> "XX:XX"
def sec2tomato(sec):
    t = []
    t.append(str(int(sec / 60)))
    t.append(str(int(sec % 60)))

    for i in range(0, len(t)):
        if len(t[i]) < 2:
            t[i] = "0" + t[i]

    tomato = ":".join(t)
    return tomato
```



### 2. 获取系统时间

获取系统时间在python里我使用的是time包, 还有一个相似的是datetime.time包, 注意不要搞混了

```python
import time
```

倒计时的基本思路是点击开始按钮时获取一个开启的系统时间, 然后用户会有一个给定的目标时间, 然后点按钮以后会进入一个循环, 知道计时结束才会退出, 在循环里面一直获取系统时间和其实时间运算就得到了已经过了多久, 再和目标时间判断就行了

```
t_start = time.time()
```

这个语句是获取以秒数显示的当前系统时间, 用于运算会比较方便



### 3. 页面元素的交互

简单的页面元素交互可以在Qt里直接实现

原理基本上是, 按下按钮之类的东西, 会发出一个信号

`ui_window.button_start.clicked`这个信号就是`ui_window`这个窗口下`button_start`按钮发出的点击信号, 使用`connect`绑定一个**slot**之后

```python
ui_window.button_start.clicked.connect(start_a_tomato)
```

在这里的意思就是: 单击这个按钮以后执行`start_a_tomato`函数, 注意函数名在这里不带括号



## 二. 已解决的问题

### 1. 倒计时使用time.sleep()效果不好的问题

最开始的思路里, 用户点击开始后进入一个循环, 这个循环每次执行一秒, 然后让页面更新一次, 用到的函数是这个

```python
import time
time.sleep(1)	#控制系统空置一秒
```

但是问题就是, 和单片机上不能乱用`delay()`一样, 使用`sleep()`会使程序整个无法响应, 导致拖拽手感奇怪, 且拖拽时倒计时直接停止

然后换了思路, 直接不断读取系统时间实时刷新, 解决了拖拽手感的问题, 但拖拽时倒计时还是会停止, 不过放下窗口后时间并不会出错, 就先不管了



### 2. 改变窗口元素但窗口显示不刷新的问题

最开始在循环里改变了元素, 但发现直到循环退出窗口才改变了显示, 但使用print输出又没什么问题, 于是想可能是窗口刷新的问题, 最后的解决办法就一条指令

```python
QtWidgets.QApplication.processEvents()
```

让窗口刷新





## 三. 待解决的问题

### 1. 拖动窗口时时间不走动的问题

暂时没有思路



### 2. Qt里写了中文`uic()`命令就无法成功执行的问题

应该是编码不统一的问题, 但是改了Qt的编码几次还是不行, 暂时先用英文顶着, 看看以后有没有解决办法

暂时没有思路





## 四. 下一阶段的目标

- 加入自己指定时间的模块
- 加入保存用户设置的文件
- 在倒计时结束时尝试发出通知



