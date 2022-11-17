from win32gui import GetWindowText, GetForegroundWindow
import time
import csv
from ctypes import Structure, windll, c_uint, sizeof, byref


class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]

def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0

from datetime import datetime
datetime.fromisoformat('2011-11-04T00:05:23')
import os
cwd = os.getcwd() + "/test.csv"
print(cwd)
with open(cwd, "a") as f:
    writer = csv.writer(f)
    while(True):
        writer.writerow([datetime.now(),GetWindowText(GetForegroundWindow()),get_idle_duration()])
        time.sleep(15)


