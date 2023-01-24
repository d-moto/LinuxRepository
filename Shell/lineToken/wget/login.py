
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# メールアドレスとパスワードの指定
USER = "9L6EYDC"
PASS = "d999d666d111"

# セッションを開始
session = requests.session()

# ログイン
login_info = {
    "webmbrId":USER,
    "webmbrId":PASS,
    "back":"index.php",
    "mml_id":"0"
}

# action
#url_login = "http://uta.pw/sakusibbs/users.php?action=login&m=try"
url_login = "https://www3.lifecard.co.jp/WebDesk/action/wa101/WA10106/rWA1010601"
res = session.post(url_login, data=login_info)
res.raise_for_status() # エラーならここで例外を発生させる

print(res.text)
