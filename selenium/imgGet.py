from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import os
import tkinter as tk
import sys
import pdb
import re
import urllib.request as urlreq

path = r"C:\Users\ec000248\Documents\python\chromedriver.exe"

linkData = []

def searchImage():
  keyword = Entry1.get()
  max = int(Entry2.get())
  # 検索結果から各ページのリンク先をmaxページ分だけ取得
  for num in range(0,max,20):
      res = requests.get("http://www.irasutoya.com/search?q="+keyword+"&max-results=20&start="+str(num))
      soup = BeautifulSoup(res.text, "lxml")

      # Linkの箇所をselect
      links = soup.select("a[href]")
      for a in links:
          # Linkタグのhref属性の箇所を抜き出す
          href = a.attrs['href']
          # 画像データに対応するページのリンク先のみをリストに格納
          if re.search(r"irasutoya.*blog-post.*html$",href):
              if not href in linkData:
                  linkData.append(href)

  pdb.set_trace()
  print(linkData)

  # 各ページから画像データのリンクを取得して、画像を保存
  for link in linkData:
      res = requests.get(link)
      soup = BeautifulSoup(res.text, "lxml")

      # 記事中の画像データを抜き出す
      # class separator -> a の抜き出し
      links = soup.select(".separator > a")
      for a in links:
          # hrefのデータを取得
          imageLink = a.get('href')
          # ファイル名の取得
          filename = re.search(r".*\/(.*png|.*jpg)$",imageLink)
          # 画像をダウンロードする
          urlreq.urlretrieve(imageLink,r"C:\Users\ec000248\Documents\Git\200222_training\selenium\img\img"+filename.group(1))
          # デバッグ用にダウンロード先Linkを表示
          print(imageLink)

#-------------------------------------------------------------------------------------

#ツール準備
root = tk.Tk()
root.title("イラスト屋自動取得")
root.geometry("250x250")

label = tk.Label(root,text="テスト")

#表示
label.grid()

# ラベル
lbl = tk.Label(text='検索用語')
lbl.place(x=30, y=70)

# テキストボックス
Entry1 = tk.Entry(width=20)
Entry1.place(x=90, y=70)

# ラベル
lbl = tk.Label(text='取得枚数')
lbl.place(x=30, y=100)

# テキストボックス
Entry2 = tk.Entry(width=20)
Entry2.place(x=90, y=100)

search = tk.Button(root,text="検索開始",font=('',15),command=searchImage,fg='#ffffff',bg='#0080ff',width=15,height=3)
search.place(x=30,y=150)

root.mainloop()