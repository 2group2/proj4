# We all collobarated together on visual studio code editor under a shared terminal with live share which only uses the host terminal
# and that's why a majority of the work was under Jai's commit.

# library imports
from pip._vendor import requests
from urllib.request import urlretrieve
import os

# variable initialization
URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
log_file = 'http_access_log.txt'
end_date_line = 323330

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
print("Log Data from AWS")
print("\nTotal requests from last six months", last_six_month_request_counter)
print("\nTotal requests made:", request_total)

print("\nTotal number of requests made in the last 6 months (Req. Total and Log Line)", request_total - end_date_line)
#
#
#
# Part 2
#
#
#

# 1. How many requests were made on each day? 
# Responsible: Paula

# 2. How many requests were made on a week-by-week basis? Per month?
# Responsible: Jai (week) and Paula (month)

# 3. What percentage of the requests were not successful (any 4xx status code)?
# Responsible: Ivan

# 4. What percentage of the requests were redirected elsewhere (any 3xx codes)?
# Responsible: Ivan

# 5. What was the most-requested file?
# Responsible: [NAME]

# 6. What was the least-requested file? 
# Responsible: [NAME]

# 7. logs broken into separate files by month
# Responsible: Jai and Paula
