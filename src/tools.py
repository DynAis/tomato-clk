import sys
import time
import json
from qtpy import QtWidgets
from qtpy import QtCore
from PyQt5 import QtGui


def tomato2sec(tomato):
    sec = int(tomato[3:])
    sec = sec + 60 * int(tomato[:2])
    return sec


def sec2tomato(sec):
    t = []
    t.append(str(int(sec / 60)))
    t.append(str(int(sec % 60)))

    for i in range(0, len(t)):
        if len(t[i]) < 2:
            t[i] = "0" + t[i]

    tomato = ":".join(t)
    return tomato

def tomato2Qtime(tomato):
    seconds = int(tomato[3:])
    minutes = int(tomato[:2])
    return QtCore.QTime(0, minutes, seconds)






