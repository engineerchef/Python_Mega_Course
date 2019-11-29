import time
from datetime import datetime as dt

hosts_temp = "hosts"
# =====================================================================================================================
# If you want to use this program in real life, please activate 'hosts_path' one of them
# and replace with 'hosts_temp' code below.
# Also you have to run this program as 'Administrator' or program won't work and give some "Admin Rights" errors.
#
# hosts_path="C:\\Windows\\System32\\drivers\\etc\\hosts"
# hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
# =====================================================================================================================
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

while True:

    # This program will block those websites gives above in 'website_list' list from 08:00 to 17:00.
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,
                                                                          17):
        print("Working hours...")
        with open(hosts_temp, "r+") as file:
            content = file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Fun hours...")
        with open(hosts_temp,"r+") as file:
            content=file.readlines()
            file.seek(0)
            print(content)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)
