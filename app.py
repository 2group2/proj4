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


  
#1. & 2. Daily, Weekly, Monthly
#(Done by Wesley) The log file began on October 24th 1994 and ended on October 11th 1994 which is 365 days minus 13 days, or 352 days. 
#All of the following are averages
dayCalc = request_total / (365-13)
dayCalc = int(dayCalc)
#352 days translates to roughly 50 weeks
weekCalc = request_total / (52 - 2)
weekCalc = int(weekCalc)
#50 weeks is rounded up to a full 12 months
monthCalc = request_total / (12)
monthCalc = int(monthCalc)



# TODO: Output for marketing
print("\nLog Data from AWS")
print("\nTotal requests from last six months:", last_six_month_request_counter)
print("\nTotal requests made:", request_total)
print("\nAverage requests made each day:", dayCalc)
print("\nAverage requests made each week:", weekCalc)
print("\nAverage requests made each month:", monthCalc)
print("\nTotal number of requests made in the last 6 months (Req. Total and Log Line)", request_total - end_date_line)

# 5. What was the most-requested file?
# Responsible: [Brandon]
#TEST
# month = "Oct"
# query = ".*\[[0-9]+/(" + month + ")/[0-9]{4}:.* \-[0-9]{4}\] \".*\" .*" 

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"] 

# 6. What was the least-requested file? 
# Responsible: [Brad]

def getCountOfFiles(log_file):
    file_count = {}
    with open(log_file, 'r') as file:
        Content = file.read()
        lines = Content.split("\n")

    for line in lines:
        data = re.split(r'.*? - .* \[.*?\] \".*? (.*?)\"? .+? .+ .+', line)
        
        if len(data) < 3:
            # if it did not parse correctly, it will re-parse
            if len(line) > 40:
                if data[0].count("\"") == 2:
                    data = re.split(r'.*\[[0-9]+/[a-zA-Z]+/[0-9]{4}:.* \-[0-9]{4}\] \"(?:GET )(.*).+\" .*', line)
                
                data = re.split(r'.*\[[0-9]+/[a-zA-Z]+/[0-9]{4}:.* \-[0-9]{4}\] \"(?:GET )(.*).+\ .*', line)
            else:
                # short ones like local   index.html
                data = re.split(r'.*? .+ .*?(.+)', line)
        
        if len(data) == 3:
            # if the data reparsed correctly
            filename = data[1]
            if filename in file_count:
                file_count[filename] += 1
            else:
                file_count[filename] = 1
        
    return file_count
    
# prints dictionary
# print(getCountOfFiles(log_file))
file_count = getCountOfFiles(log_file)
print("Most Requested File Name", max(file_count, key=file_count.get))
print("Least Requested File Name", min(file_count, key=file_count.get))



# 7. logs broken into separate files by month
# Responsible: Jai and Paula
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# creates files
for month in months:
    file=open(month+".txt", "w")

Log_pattern = r'(.*?) - (.*) \[(.*?)\] \"(.*?) (.*?)\"? (.+?) (.+) (.+)'  
 
with open(log_file, 'r') as file:
  Content = file.read()
  lines = Content.split("\n")
for line in lines:
    matches = re.match(Log_pattern, line)

    if not matches:
        continue

    time = matches.group(3)
    month = time[3:6]
    
    f = open(month+".txt", "a")
    f.write(line+'\n')
    
# 2. How many requests were made on a week-by-week basis? Per month?
# Responsible: Jai (week) and Paula (month)

# Per Month Basis

print("\nTotal requests made each month:")
for month in months:
    filename = month + ".txt"
    with open(filename, "r") as file:
        print(month, ": ", len(file.readlines()))

#3. & 4. Percentage of requests
# 3. What percentage of the requests were not successful (any 4xx status code)?
# Responsible: Ivan

# 4. What percentage of the requests were redirected elsewhere (any 3xx codes)?
# Responsible: Ivan

# 5. What was the most-requested file?
# Responsible: [Brandon]


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

