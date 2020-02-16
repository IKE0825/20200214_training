#事前準備　ターミナルで下記コマンド
#pip install selenium  ライブラリ"selenium"インストール
#pip install chromedriver-binary
#chromedriverはchromeのバージョンと同じものを使用すること

#デバッグ用ライブラリ
import pdb
#処理ステップ管理用ライブラリ
import time

from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expcepted_conditions as EC
#from selenium.common.exceptions import TimeoutException

#Chromeのパスを指定
path = r"/home/kenji-ito/chromedriver/chromedriver"

#Chromeを起動
browser = webdriver.Chrome(path)
pdb.set_trace()

#ブラウザを開く
browser.get('')
time.sleep(1) #ブラウザが開くまで待つ

