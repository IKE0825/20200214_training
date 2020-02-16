#事前準備　ターミナルで下記コマンド
#pip install selenium  ライブラリ"selenium"インストール
#pip install chromedriver-binary
#chromedriverはchromeのバージョンと同じものを使用すること

import pdb
import time
from selenium import webdriver

#Chromeのパスを指定
path = r"/home/kenji-ito/firefoxdriver/geckodriver"

#Chromeを起動
driver = webdriver.Firefox()

#ブラウザを開く
driver.get('https://devjumlim.cybozu.com/login?redirect=https%3A%2F%2Fdevjumlim.cybozu.com%2F')
time.sleep(1) #ブラウザが開くまで待つ

usrId = driver.find_element_by_name('username')
usrId.send_keys('ken_itou@daiseki-eco.co.jp')

pW = driver.find_element_by_name('password')
pW.send_keys('potenz@0825')

link_el = driver.find_element_by_class_name('login-button')
link_el.click()

link_el = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div/a[2]')
link_el.click()
