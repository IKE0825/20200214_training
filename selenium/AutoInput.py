#事前準備　ターミナルで下記コマンド
#pip install selenium  ライブラリ"selenium"インストール
#pip install chromedriver-binary
#chromedriverはchromeのバージョンと同じものを使用すること

import pdb
import time
from selenium import webdriver

#gegodriverのパスを指定
# path = r"/home/kenji-ito/firefoxdriver/geckodriver"  #linuxの場合

#ブラウザを起動
driver = webdriver.Firefox() #linux パス不要binにいれたら動く windowsの場合、実行ファイルと同じディレクトリ

#ブラウザを開く
driver.get('https://devjumlim.cybozu.com/login?redirect=https%3A%2F%2Fdevjumlim.cybozu.com%2F')
time.sleep(1) #ブラウザが開くまで待つ

usrId = driver.find_element_by_name('username')
usrId.send_keys('ken_itou@daiseki-eco.co.jp')

pW = driver.find_element_by_name('password')
pW.send_keys('potenz@0825')

link_el = driver.find_element_by_class_name('login-button')
link_el.click()

time.sleep(2)
link_el = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div/a[2]')
link_el.click()

# pdb.set_trace()
time.sleep(2)
link_el = driver.find_element_by_class_name('ocean-ui-kintone-recordlist-widgettitle-text')
print(link_el)
link_el.click()

link_el = driver.find_element_by_xpath('/html/body/div[10]/div[5]/div[2]/div[2]/div/div[3]/a[1]')
link_el.click()

usrName = driver.find_element_by_id(':1esearch-:1f-text')
usrName.send_keys('伊藤健二')
title = driver.find_element_by_id('31_5125442-:1w-text')
title.send_keys('LANケーブル発注')
productN = driver.find_element_by_id('32_5125435-:27-text')
productN.send_keys('LANケーブル')
unitPrice = driver.find_element_by_id('32_5125436-:2a-text')
unitPrice.send_keys('660')
math =driver.find_element_by_id('32_5125437-:2d-text')
math.send_keys('5')
purpose = driver.find_element_by_id('31_5125444-textarea')
purpose.send_keys('在庫切れのため')
saveButton = driver.find_element_by_class_name('gaia-ui-actionmenu-save')
saveButton.click()
time.sleep(4)
decideButton = driver.find_element_by_xpath('/html/body/div[8]/div[2]/div[1]/div[3]/div/div[1]/div/div/div[1]/div/span[1]/span[2]')
decideButton.click()
okButton = driver.find_element_by_name('ok')
okButton.click()

driver.close()

sys.exit()