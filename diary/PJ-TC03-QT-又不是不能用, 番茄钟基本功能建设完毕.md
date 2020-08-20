# 03 - 又不是不能用, 番茄钟基本功能建设完毕

[TOC]

## 项目进度

- 加入了自己指定时间的模块

<img src="D:\WorkSpace\.Typora Images Hub\image-20200412153655534.png" alt="image-20200412153655534" style="zoom:50%;" />

- 加入保存用户设置的文件`config.json`
- 在倒计时结束时发出铃声通知
- 完善了除统计和To Do List外的Menu界面

<img src="D:\WorkSpace\.Typora Images Hub\image-20200412153753123.png" alt="image-20200412153753123" style="zoom:50%;" />

- 修正了部分bug





## 一. 重要代码模块

### 1. 打包程序成exe文件

##### pyInstaller模块

`pyInstaller`是python的一个库, 使用它可以很方便的打包文件成为exe可执行文件

要使用这个库, 首先在Pycharm里安装相应的环境, 之后新建一个.py文件, 比如我的:

![image-20200412160718129](D:\WorkSpace\.Typora Images Hub\image-20200412160718129.png)

在里面输入代码(以这次工程为例):

```python
import  os
if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts=['main.py','-w','-F','--icon=image/tomato.ico']
    run(opts)
```

其中主要注意`opts=['main.py','-w','-F','--icon=image/tomato.ico']`这一句

`main.py`是主文件, 是进程的入口

`-w`这个参数使编译出来的文件时`exe`+`文件`的形式, 去掉这个参数编译出来是一个整体的`exe`文件

`-F`参数强制编译, 也就是说本次会覆盖上次的文件, 我觉得加上比较好

最后`--icon=image/tomato.ico`是我指定的exe文件图标, 需要是一个`ico`文件

直接运行`.py`脚本就可以在`/dist`里得到编译的文件



##### 资源文件夹问题

本次制作番茄钟使用到的资源文件, 比如配置文件, 或者是`.MP3`的铃声文件, pyInstaller在编译的时候都是不会编译的, 也就是说需要自己将文件复制到产生出来的目录下, 不然程序会报错无法运行



### 2. 读取和写入配置文件

##### 使用Json作为配置文件

Json是一种常见的语言, 其中一种用法就是作为书写配置文件的语言, 虽然有人说它不适合作为配置文件语言, 但是小项目用用还是没有问题的

Json配置文件以`{`开头, 以`}`结束, 大括号在Json里代表一个对象, 具有一个键与一个值, 用`:`对应,

可以理解为Python里的字典(其实就是)

用Python的语法来看Json没有一点问题

如

```json
{"tomato": {"t_target": "00:05", "t_break": "00:05"}}
```

值得注意的是Json对语法的要求非常严格, 并且不可以有注释



##### Python3读取Json文件

Python官方内置了Json的使用库

```python
import json

#假设config是一个字典

# Json读取
with open("config.json", "r") as c:
    config = json.load(c)
    
# Json写入
with open("config.json", "w") as c:
    json.dump(config, c)
    
```

读取文件以字典形式展现, 写入的变量也需要是一个字典



### 3. 在对象方法定义里直接调用具体的实例

发现在对象的方法定义里, 可以直接调用看起来还没有定义的实例, 比如

```python
class  BreakWindow(QtWidgets.QDialog):
	...
    def start_a_new_tomato(self):
        ...
        window.start_a_tomato()
```

在这里我定义了`BreakWindow`类, 方法里调用了`window.start_a_tomato()`, `window`是另一个类, 并且在后文才定义(当然是在方法调用之前)



### 4. 循环不退出? - 使用flag标志的重要性

因为循环不退出而产生bug已经不知道多少次了, 以后注意在书写循环的时候一定要提前想好尽可能全的情况, 并且写好flag, 循环不在该退的时候退真的很讨厌





## 二. 已解决的问题

### 1. 在Python中播放声音/音乐 - playsound包

在环境里加入playsound包

调用使用

```python
from playsound import playsound

playsound("sound/XXXX.mp3")
```



真的是非常简单的API了

但是缺点也是太简单了, 几乎没有其他的可操作选项了, 可以看的出来作者基本也是没有什么经验的

还有一个就是响铃的速度好像不是很快



### 2. 窗口关闭事件信号 - 重写closeEvent()方法

在窗口关闭时, 会执行`.closeEvent()`方法, 通过重写这个方法, 可以达到检测窗口关闭的效果

```python
def closeEvent(self, event):
	event.accept()
```



### 3. 验证窗口是否在关闭 - isHidden()





## 三. 待解决的问题

### 1. 拖动窗口时时间不走动的问题

暂时没有思路



### 2. Qt里写了中文`uic()`命令就无法成功执行的问题

暂时没有思路



### 3. 进程无法完全退出问题 -> window.close()效果问题 -> 响铃bug



### 4. 占用cpu过高问题

猜测是在循环时关闭窗口导致循环还在后台运行, 没有正常退出的问题

但怎么说这个占用也太夸张了吧就算是我有个循环

![image-20200412164033369](D:\WorkSpace\.Typora Images Hub\image-20200412164033369.png)

你一个循环凭什么吃掉我1/4个CPU啊



### 5. 交互逻辑混乱问题

完全是我的锅, 因为各种小bug, 以及前期准备不足, 经验不到位, 结果使得各种循环判断, 各种地方交错调用, 命名没规范之类...

导致出现大问题无从下手, 如果要进一步给软件加入功能, 最起码的, 让他**"能用"**, 是肯定要重构代码的





## 四. 下一阶段的目标

### 											



### 												代码重构





## 五. 总结

虽然程序交互有很大进步, 但还是可以看出我的经验不足, 前期准备缺乏, 导致结构混乱, 后期出现Bug无从下手

经过这次教训, 我知道了前期纸上的准备和写代码同样重要, 写代码和我整理电脑一样, 都不可以把东西随意乱放, 不然图一时之快只会给以后的自己带来麻烦

虽然标题上写着**"又不是不能用"**, 但CPU占用如此之高, 进程无法干净退出, 无故响铃的软件, 确实就是**"不能用"**的



