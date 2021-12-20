# This program logs data of interest to an InfluxDB database.

# Import the InfluxDB client.
import os
import json
import mysql.connector
import time, threading
from datetime import datetime
# read in the config file
# conf = open("db.cnf", "r").read()
def write_TBW_to_mysql():
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

    # get data from sensor
    ## get SSD MBW data from smartctl 
    smartctl_result = json.loads(os.popen('smartctl -aj disk0').read())
    # with open('data/smartctl_result.json', 'w') as outfile:
    #     json.dump(smartctl_result, outfile)


    # for test purposes, cache a standard result

    # parse data into fields

    ## Model Number

    model_name = smartctl_result['model_name']
    timestamp = datetime.utcnow()
    data_units_written = smartctl_result['nvme_smart_health_information_log']['data_units_written']
    GBW = data_units_written*512/1000/1000
    TBW = GBW/1000
    power_cycles = smartctl_result['nvme_smart_health_information_log']['power_cycles']
    power_on_hours = smartctl_result['nvme_smart_health_information_log']['power_on_hours']
    temperature = smartctl_result['nvme_smart_health_information_log']['temperature']
    percentage_used = smartctl_result['nvme_smart_health_information_log']['percentage_used']



    # write data to mysql database
    cursor = mydb.cursor()

    add_ssd_mbw = ("INSERT INTO SSD_status "
                    "(model_name, timestamp,data_units_written, GBW, TBW, power_cycles, power_on_hours, temperature, percentage_used) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

    data_ssd_mbw = (model_name, timestamp, data_units_written, GBW, TBW, power_cycles, power_on_hours, temperature, percentage_used)

    cursor.execute(add_ssd_mbw, data_ssd_mbw)

    mydb.commit()
    cursor.close()
    mydb.close()
    print("successfully log SSD current GBW data.")
    threading.Timer(300, write_TBW_to_mysql).start()
    print("Next log in 5 minutes.")

write_TBW_to_mysql()
