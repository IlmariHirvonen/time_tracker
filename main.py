from win32gui import GetWindowText, GetForegroundWindow
import time
import csv
from ctypes import Structure, windll, c_uint, sizeof, byref
import sys
from datetime import datetime
import os
from spinner import Spinner
import keyboard

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

cwd = os.getcwd() + "/test.csv"
datetime.fromisoformat('2011-11-04T00:05:23')

def main():
    try:
        with open(cwd, "a") as f:
            print("Press ctrl+c to quit.\nCollecting data...")
            with Spinner():
                writer = csv.writer(f)
                while True:
                    writer.writerow([datetime.now(),GetWindowText(GetForegroundWindow()),get_idle_duration()])
                    time.sleep(15)
    except KeyboardInterrupt:
        print("Exiting...")
    sys.exit(0)

if __name__ == "__main__":
    main()
