import time
from datetime import datetime as dt
hosts_temp = r'C:\Users\manth\Documents\Python\App 3 Website Blocker\hosts'
redirect = '127.0.0.1'
website_lists = ['facebook.com', 'www.facebook.com']

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,10) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,12):
        print("Working Hours")
        with open('hosts', 'r+') as file:
            content = file.read()
            for website in website_lists:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')
    else:
        print("Fun Hours")
        with open('hosts', 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for lines in content:
                file.truncate()
                if not any(website in lines for website in website_lists):
                    file.write(lines)
    time.sleep(5)
