# Bandwidth_daemon

[![Build Status](https://travis-ci.org/Chris1221/Bandwidth_daemon.svg?branch=master)](https://travis-ci.org/Chris1221/Bandwidth_daemon) [![Project Status: Active - The project has reached a stable, usable state and is being actively developed.](http://www.repostatus.org/badges/0.1.0/active.svg)](http://www.repostatus.org/#active)

Every day at a set time, retrieve bandwidth usage and statistics from your ISP. 

Currently only works with Teksavvy, though can be modified for different API structures. 

Instructions for use:

1.  Clone the repo to your local environment
2.  In teksavvy_cron.py, replace "API_KEY" with your generated API key from TekSavvy
3.  In teksavvy_cron.py, replace "email@gmail.com" and "pass" with your email and password.  I created a seperate deamon email account so as not to potentially comprimise my own account. Replace the TO field with your personal email that you would like to receive the information on. 
4.  (Optional) Customize the message and usage statistics to be displayed in the TEXT and SUBJECT fields.
5.  Test by navigating to the directory and invoking "python teksavvy_cron.py"
6.  If everything is working, you should recieve an email that looks quite close to the following:

![Image of email](https://raw.githubusercontent.com/Chris1221/Bandwidth_daemon/master/images/screenshot_1.png)

7.  Add the file to your crontab by invoking "crontab -e" in a fresh terminal window. This will default to your default text editor, which for me is vi.  
8.  Add the following line to your crontab, replacing values as desired: 0 9 * * * /path/to/python /path/to/teksavvy_cron.py
9.  Ta-da! Hopefully it works.  If not, raise an issue on this repo and we'll try to sort it out. 


Note that the computer has to be on to run the program.  I have mine running every morning at 9 am on a headless raspberry pi connected to the internet.  This tiny script will not interfere with whatever else you're using an rpi for, so I would highly recommend doing it this way.  



#import time. 
:D
