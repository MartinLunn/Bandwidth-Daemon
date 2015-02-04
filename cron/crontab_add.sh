#!/bin/bash

#you cant run this directly, dont try

crontab -e
#run every morning at 9 am
0 9 * * * /path/to/python /path/to/teksavvy_cron.py