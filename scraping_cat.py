# coding: UTF-8
import urllib.request, urllib.error
from bs4 import BeautifulSoup

# アクセスするURL
url = "https://tokyocatguardian.org/cats_date/"

# URLにアクセスする htmlが帰ってくる
html = urllib.request.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

div = soup.find_all("div")
for tag in div:
    try:
        _string = tag.get("class").pop(0)

        if _string in "row-eq-height":
            cat_div = tag.string
            break
    except:
        pass

# タイトル要素を取得する
title_tag = soup.title

# 要素の文字列を取得する
title = title_tag.string

# タイトル要素を出力
print(title_tag)

# タイトルを文字列を出力
print(title)

print(cat_div)