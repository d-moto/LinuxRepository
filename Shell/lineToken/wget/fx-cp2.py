from bs4 import BeautifulSoup
import requests

google = "https://www.google.com/search?q=%E3%83%89%E3%83%AB%E5%86%86&oq=%E3%83%89%E3%83%AB%E5%86%86&aqs=chrome..69i57j0i131i433i512j0i512j0i131i433l5j0i131i433i512j0i131i433.1789j1j7&sourceid=chrome&ie=UTF-8"
yahoo = "https://info.finance.yahoo.co.jp/fx/detail/?code=usdjpy"

r_google = requests.get(google)
s_google = BeautifulSoup(r_google.content,"html.parser")
var_google = s_google.find("div",class_="vLqKYe")
#print(var_google)

#datetime
import datetime

dt_now = datetime.datetime.now()

print(dt_now)
# 2019-02-04 21:04:15.412854

#fx
r_yahoo = requests.get(yahoo)
s_yahoo = BeautifulSoup(r_yahoo.content,"html.parser")

#
var_yahoo = s_yahoo.find("div",class_="DL5lxuTC")
print(var_yahoo.h1.get_text())


var_yahoo2 = s_yahoo.find("div",class_="_2QdA_Jef")
print(var_yahoo2.dt.get_text())
print(var_yahoo2.dd.get_text())

