from bs4 import BeautifulSoup
import requests

google = "https://www.google.com/search?q=%E3%83%89%E3%83%AB%E5%86%86&oq=%E3%83%89%E3%83%AB%E5%86%86&aqs=chrome..69i57j0i131i433i512j0i512j0i131i433l5j0i131i433i512j0i131i433.1789j1j7&sourceid=chrome&ie=UTF-8"
yahoo = "https://info.finance.yahoo.co.jp/fx/detail/?code=usdjpy"
nikkei = "https://www.nikkei.com/"

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
var_yahoo = s_yahoo.find("div",class_="fxChartTtl")
print(var_yahoo.h1.get_text())


var_yahoo2 = s_yahoo.find("div",class_="fxRateChart")
print(var_yahoo2.dt.get_text())
print(var_yahoo2.dd.get_text())


##nikkei info
r_nikkei = requests.get(nikkei)
s_nikkei = BeautifulSoup(r_nikkei.content,"html.parser")

var_nikkei_all = s_nikkei.find_all("div",class_="block_bch8brg")
var_nikkei = s_nikkei.find("div",class_="block_bch8brg")
#print(var_nikkei.div.get_text())
#print(len(var_nikkei))
print(var_nikkei.a.get_text())

for var_nikkei in var_nikkei_all:
    print(var_nikkei.a.get_text())


#get all titles
#nikkei_title = s_nikkei.find_all("div",class_="blocks_b1619kyv")
#len(nikkei_title)
#for var_nikkei in nikkei_title:
#    print(var_nikkei.div.get_text())


en_word = "https://park.sjnk.co.jp/education/english/0/"

r_en_word = requests.get(en_word)
s_en_word = BeautifulSoup(r_en_word.content,"html.parser")

var_en_word_all = s_en_word.find_all("div",class_="qustionText")
var_en_word = s_en_word.find("div",class_="questionText")
print(var_en_word)
