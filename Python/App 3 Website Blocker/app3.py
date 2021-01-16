#--------------------Importing File
import time
import datetime
from datetime import datetime as dt

#--------------------Giving Path
hosts_temp = r'C:\Users\manth\Documents\Python\App 3 Website Blocker\hosts'
hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
redirect = "127.0.0.1"
website_lists = ["www.facebook.com", "facebook.com"]

#--------------------Code for website blocker
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,10) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,11):
        print('Working Hours...')
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_lists:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + "\n")
    else:
        print('Fun Hours...')
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_lists):
                    file.write(line)
                file.truncate()
    time.sleep(5)
