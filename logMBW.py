# This is a python script that will log the MBW to my Macbook Pro SSD periodically

import os
import time, threading

def MBWlogger():
        print ("Current time is:",time.ctime())
        os.system('smartctl -a disk0 | grep 175 |  sed -e "s/^/$(date) /" >> data/MBW.txt')
        threading.Timer(1800, MBWlogger).start()
        print("successfully log SSD current MBW data.")

MBWlogger()


