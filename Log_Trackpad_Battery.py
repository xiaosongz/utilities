# This program logs data of interest to an mysql database.

import os
import json
import mysql.connector
import time, threading
from datetime import datetime

# read in the config file
# conf = open("db.cnf", "r").read()
def write_Battery_pct_to_mysql():
    print ("Current time is:",time.ctime())
    ## establish connection to mysql
    mydb = mysql.connector.connect(
            host="192.168.10.2",
            port=3306,
            user="macmini",
            password="minipasswd",
            database="macmini",
            auth_plugin='mysql_native_password'
            )

    # get battery percentage from magic trackpad
    battery_info = os.popen("ioreg -l | grep -i 'BatteryPercent'").read().split("=")
    battery_percentage = battery_info[1].split("\n")[0]
    battery_pct = int(battery_percentage)
# get current time
    timestamp = datetime.utcnow()
    # write data to mysql database
    cursor = mydb.cursor()

    add_ssd_mbw = ("INSERT INTO Trackpad_Battery "
                    "(timestamp,battery_pct) "
                    "VALUES (%s, %s)")

    data_ssd_mbw = (timestamp, battery_pct)

    cursor.execute(add_ssd_mbw, data_ssd_mbw)

    mydb.commit()
    cursor.close()
    mydb.close()
    print("successfully log Trackpad current battery percentage data.")
    threading.Timer(300, write_Battery_pct_to_mysql).start()
    print("Next log in 5 minutes.")

write_Battery_pct_to_mysql()
