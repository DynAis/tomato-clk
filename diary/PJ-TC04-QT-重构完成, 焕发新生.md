# 04 - 重构完成, 焕发新生

[TOC]

## 项目进度

- 重构了代码

- 修正了大部分bug





## 一. 重要代码模块

### 1. Qtimer

> https://blog.csdn.net/jia666666/article/details/81672344

Qtimer是Qt自带的定时器类, 位于PyQt5.Qcore下, 和单片机的中断函数非常像, 并且提供单次触发和多次触发两种触发方式

##### 多次触发

```python
timer.timeout.connect(function)
...
timer = Qtimer()
timer.start(1000)
```

这里`timeout`是Qtimer的中断信号, 这里设定`timer.start(1000)`代表每一秒执行一次中断, 在番茄钟里, 我使用这个中断来进行时间的更新, 时间的更新仍然使用的是原生的time模块

如果要停止Qtimer,使用

```python
timer.stop()
```



### 2. 自定义信号

>  https://blog.csdn.net/foreveronly/article/details/82453697



## 二. 已解决的问题

### 1. 拖动窗口时时间不走动的问题

加完Qtimer中断完全没有问题



### 3. 进程无法完全退出问题 -> window.close()效果问题 -> 响铃bug

通过将子窗口变为主窗口类的成员, 并使用以下语句初始化

```python
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #子窗口建立
        self.subBreak = BreakWindow(self)# 注意这里
        
class BreakWindow(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
```

关键也就是加入`def __init__(self,parent=None)`, 使主从窗口关联起来(具体实现逻辑尚不清晰), 再加上合理的退出判断, 就可以实现干净的退出了

响铃bug加完Qtimer中断完后全没有问题



### 4. 占用cpu过高问题

加完Qtimer中断完全没有问题



### 5. 交互逻辑混乱问题

通过重构代码逻辑解决了, 现在所有的子窗口都是主窗口的成员了





## 三. 待解决的问题

### 1. Qt里写了中文`uic()`命令就无法成功执行的问题

暂时没有思路





## 四. 下一阶段的目标

### 1. 实现使用时间的统计模块, 尝试使用Mysql来储存数据?





## 五. 总结

再此理解了那句话, 不能让程序假死, 比如之前我想要time.sleep()来实现...

正确使用中断是很重要的, 这方面还要多加练习

并且另外很重要的一点就是, 使用一个库里现成的东西往往整个的整合度会更好

本来甚至都准备上多线程了...

