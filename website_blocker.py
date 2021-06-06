import time
from datetime import datetime as dt

host_path = r"\etc\hosts"
host_temp = "host"
redirect = '127.0.0.1'
website_lists = [
    'facebook.com',
    'www.facebook.com'
]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,
                                                                          17):
        print('Working Hour')
        with open(host_temp, 'r+') as file:
            content = file.read()
            print(content)

            for website in website_lists:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(host_temp, 'r+') as file:
            content = file.readline()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_lists):
                    file.write(line)
                    file.truncate()
        print('You have access of all website, ENJOY')
    time.sleep(5)
