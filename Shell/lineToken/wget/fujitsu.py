from bs4 import BeautifulSoup
import requests

#weather = "https://weather.com/weather/today/l/f34b22ee0a62ff783364922f189a61e470570fa3fa061dcd11aa9652116cdfa6"

fujitsu1 = "https://catalog.redhat.com/platform/red-hat-openstack/hardware/search?p=1&rows=60"

#datetime
import datetime

dt_now = datetime.datetime.now()

#print(dt_now)
# 2019-02-04 21:04:15.412854


##weather
r_fujitsu1 = requests.get(fujitsu1)
s_fujitsu1 = BeautifulSoup(r_fujitsu1.content,"html.parser")
var_fujitsu1 = s_fujitsu1.findall("main")
print(var_fujitsu1)

#var_fujitsu1 = s_fujitsu1.find("div",class_="CurrentConditions--phraseValue--2Z18W")
#print(var_weather.get_text())
#var_weather = s_weather.find("div",class_="CurrentConditions--header--27uOE")
#print(var_weather.h1.get_text())
