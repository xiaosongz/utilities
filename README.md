# Utilities
Some scripts for my curiosity and OCD

## SSD usage logger

SSD is fantstic! But do you every worry about how much Data you every wrote to SSD? 
Under normal usage, user probably won't need to worry about the lifespan of a SSD. But there are some rare cases that buggy Apps wrote excessive amount data to your SSD. It is theoretically possible that the SSD's lifespan could end much faster than expected and data could be lost too.  

Anyway, just trying to covience myself this is not a useless thing.

## log trackpad battery percentage into mysql

I want to track how much battery percentage is left in my trackpad, relative to how much I used it.

- check tracpad battery percentage every 10 minutes
- break the output into fields and send the data to mysql

## MYSQL running on Synology NAS docker container

After tring the InfluxDB, we found that it's limited to tacking numeric data only, thus we need to use MySQL to store some text data such as Model_number.


