# We all collobarated together on visual studio code editor under a shared terminal with live share which only uses the host terminal
# and that's why a majority of the work was under Jai's commit.

# library imports
from pip._vendor import requests
from urllib.request import urlretrieve
import os
import re

# variable initialization
URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
log_file = 'http_access_log.txt'
end_date_line = 323330

# create all files
jan_file=open("Jan.txt", "w")
feb_file=open("Feb.txt", "w") 
mar_file=open("Mar.txt", "w")
apr_file=open("Apr.txt", "w")
may_file=open("May.txt", "w") 
jun_file=open("Jun.txt", "w") 
jul_file=open("Jul.txt", "w")
aug_file=open("Aug.txt", "w") 
sep_file=open("Sep.txt", "w") 
oct_file=open("Oct.txt", "w")
nov_file=open("Nov.txt", "w") 
dec_file=open("Dec.txt", "w") 

# retrieve log file and save to machine

if os.path.exists(log_file):
  retrievefile = open(log_file, "r")
else:
  print("Loading Log File...")
  log_file, headers = urlretrieve(URL_PATH, log_file, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)


# We found the specific line in the log file that represented the past six months then we wrote the following program to display that line:
last_six_month_request_counter = 0
end_date = "09/Apr/1995"

with open(log_file, 'r') as file:
  Content = file.read()
  lines = Content.split("\n")
  
  lines.reverse()
  
  for line in lines:
    if end_date in line:
      break
    else:
      last_six_month_request_counter += 1

# TODO: Output the lines of code
with open(log_file, "r") as file:
  request_total = len(file.readlines())


  

# TODO: Output for marketing
print("\nLog Data from AWS")
print("\nTotal requests from last six months:", last_six_month_request_counter)
print("\nTotal requests made:", request_total)
print("\nTotal requests made each day:")
print("\nTotal requests made each week:")
print("\nTotal requests made each month:")
print("\nTotal number of requests made in the last 6 months (Req. Total and Log Line)", request_total - end_date_line)

#TEST
# month = "Oct"
# query = ".*\[[0-9]+/(" + month + ")/[0-9]{4}:.* \-[0-9]{4}\] \".*\" .*"  
   

# 5. What was the most-requested file?
# Responsible: [Brandon]

#.*\[[0-9]+/[a-zA-Z]+/[0-9]{4}:.* \-[0-9]{4}\] (\".*\") .*

# 6. What was the least-requested file? 
# Responsible: [NAME]

# 7. logs broken into separate files by month
# Responsible: Jai and Paula
Log_pattern = r'(.*?) - (.*) \[(.*?)\] \"(.*?) (.*?)\"? (.+?) (.+) (.+)'   
with open(log_file, 'r') as file:
  Content = file.read()
  lines = Content.split("\n")
for line in lines:
    matches = re.match(Log_pattern, line)

    if not matches:
        continue

    matches.group(0) 
    matches.group(3) 
    time = matches.group(3)
    month = time[3:6]

    if (month == "Jan"): 
        jan_file.write(line+'\n')
    elif (month == "Feb"): 
        feb_file.write(line+'\n')
    elif (month == "Mar"): 
        mar_file.write(line+'\n')
    elif (month == "Apr"): 
        apr_file.write(line+'\n')
    elif (month == "May"): 
        may_file.write(line+'\n')
    elif (month == "Jun"): 
        jun_file.write(line+'\n')
    elif (month == "Jul"): 
        jul_file.write(line+'\n')
    elif (month == "Aug"): 
        aug_file.write(line+'\n')
    elif (month == "Sep"): 
        sep_file.write(line+'\n')
    elif (month == "Oct"): 
        oct_file.write(line+'\n')
    elif (month == "Nov"): 
        nov_file.write(line+'\n')
    elif (month == "Dec"): 
        dec_file.write(line+'\n')
    else:
        continue

# TODO: Percentage of requests that had an error code or where redirected elsewhere
error3count = 0
error4count = 0

with open(log_file, 'r') as file:
    Contents = file.read()
    lined = Contents.split("\n")
    for line in lined:
        matches = re.search(r'\"\s3\d{2}', line)
        matches2 = re.search(r'\"\s4\d{2}', line)
        if matches:
            error3count += 1
        if matches2:
            error4count += 1

percent3 = ("{:.2f}%".format(error3count/request_total * 100))
percent4 = ("{:.2f}%".format(error4count/request_total * 100))
print(percent4, "of requests were not successful")
print(percent3, "of requests were redirected elsewhere")