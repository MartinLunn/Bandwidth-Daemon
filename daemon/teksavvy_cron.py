#!/opt/local/bin/python
#you might have to change the above to point to your local python
 
from __future__ import division  
import httplib, json, time

#replace this with your API key 
APIKEY = "API_KEY"

#pull from api 
headers = {"TekSavvy-APIKey": APIKEY}
conn = httplib.HTTPSConnection("api.teksavvy.com")
conn.request('GET', '/web/Usage/UsageSummaryRecords?$filter=IsCurrent%20eq%20true', '', headers)
response = conn.getresponse()
jsonData = response.read()
 
data = json.loads(jsonData)

#label 
pd  = data["value"][0]["OnPeakDownload"]
pu  = data["value"][0]["OnPeakUpload"]
opd = data["value"][0]["OffPeakDownload"]
opu = data["value"][0]["OffPeakUpload"]
sd  = data["value"][0]["StartDate"]
ed  = data["value"][0]["EndDate"]

#monthly limits: input yours
monthly_limit = 150
total_down_used = pd + opd

#take percents
percentage_of_data_used = total_down_used/monthly_limit * 100
percentage_of_data_used = round(percentage_of_data_used, 2)

#this could be done better, not sure how
now = (time.strftime("%x %X"))
today = time.strftime("%A")
month = time.strftime("%b")
current_month = int(now[0:2])
current_day = int(now[3:5])
list_of_number_of_days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]
number_of_days_in_current_month = list_of_number_of_days_in_months[current_month-1]

percentage_of_month_passed = current_day/number_of_days_in_current_month * 100
percentage_of_month_passed = round(percentage_of_month_passed, 2)

on_peak_dl_perc = pd/total_down_used*100
on_peak_dl_perc = round(on_peak_dl_perc, 2)

#send email
def send_email():
            import smtplib

            gmail_user = "email@gmail.com" #change to yours
            gmail_pwd = "pass" #change to yours
            FROM = 'email@gmail.com' #change to yours
            TO = ['email@gmail.com'] #must be a list
            SUBJECT = "Bandwidth Tracking %s %s %s" % (today, month, current_day) 
            TEXT = "Good morning! \nToday is %s. \nYou have used %s percent of your data this month, which is equal to %s Gb of data usage. You are %s percent through this month. %s percent of this data is on peak." %(today, percentage_of_data_used, total_down_used, percentage_of_month_passed, on_peak_dl_perc)
            
#"peak down: %s, peak up: %s, offpeak up: %s, offpeak up: %s" % (pd, pu, opd, opu)

            # Prepare actual message
            message = "\From: %s\nTo: %s\nSubject: %s\n\n%s " % (FROM, ", ".join(TO), SUBJECT, TEXT)
            try:
                #server = smtplib.SMTP(SERVER) 
                server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
                server.ehlo()
                server.starttls()
                server.login(gmail_user, gmail_pwd)
                server.sendmail(FROM, TO, message)
                #server.quit()
                server.close()
                print 'successfully sent the mail'
            except:
                print "failed to send mail"
                
send_email()