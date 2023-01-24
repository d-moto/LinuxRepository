
print ("hello")

from bs4 import BeautifulSoup
import requests
result = requests.get("https://pycon.jp/2016/ja/schedule/talks/list/")

print (result)

text = result.text

soup = BeautifulSoup(result.content, "html.parser")
p = soup.find("div", class_="presentation").h3.get_text()
print(p)

url = "https://www.google.com/search?q=%E3%83%89%E3%83%AB%E5%86%86&oq=%E3%83%89%E3%83%AB%E5%86%86&aqs=chrome..69i57j0i131i433i512j0i512j0i131i433l5j0i131i433i512j0i131i433.1789j1j7&sourceid=chrome&ie=UTF-8"
url2 = "https://info.finance.yahoo.co.jp/fx/detail/?code=usdjpy"

result = requests.get(url)
soup2 = BeautifulSoup(result.content, "html.parser")
p2 = soup2.find("div", class_="vLqKYe")
print(p2)

result2 = requests.get(url2)
soup2 = BeautifulSoup(result2.content, "html.parser")
p2 = soup2.find("div",class_="fxChartTtl")
print(p2.h1.get_text())

r3 = requests.get(url2)
s3 = BeautifulSoup(r3.content, "html.parser")
p3 = s3.find("div",class_="fxRateChart")
print(p3.dt.get_text())
print(p3.dd.get_text())
