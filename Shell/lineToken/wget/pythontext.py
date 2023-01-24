import requests 
from bs4 import BeautifulSoup

result = requests.get("https://pycon.jp/2016/ja/schedule/talks/list/")
soup = BeautifulSoup(result.content,"html.parser")
presentation_html_list = soup.find_all("div",class_="presentation")
#print(" language | title")
print("{0:<10}| {1}".format("language","title"))
print("{0:<10}| {0}".format("--------"))


#print("---------|---------")

for presentation_html in presentation_html_list:
    presentation_title_text = presentation_html.h3.get_text()
    
    if "(en)" in presentation_title_text:
        language = "English"
        title = presentation_title_text.replace('\xa0(en)','')
    elif "(ja)" in presentation_title_text:
        language = 'Japanese' 
        title = presentation_title_text.replace('\xa0(ja)','') 
    print("{0:<10}|{1}".format(language,title))
