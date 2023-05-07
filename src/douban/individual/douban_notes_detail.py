# -- coding: utf-8 --

import requests
from lxml import html
import os

etree = html.etree


def get_data(url):
    # 418, 访问的网站有反爬虫机制，而解决方法就是通过模拟浏览器来访问
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'}

    data = requests.get(url, headers=header).text
    s = etree.HTML(data)

    t = s.xpath('//div[@class="note-container"]/div[1]/h1/text()')[0]
    c = etree.tostring(s.xpath('//div[@class="note"]')[1], encoding='unicode')
    time = s.xpath('//div[@class="note-container"]/div[1]/div[1]/span/text()')[0]

    print(t)

    return t, c, time


if not os.path.exists("data"):
    os.mkdir("data")

if not os.path.exists("data/notes"):
    os.mkdir("data/notes")

with open('./data/notes.txt', 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

for item in lines:
    # 为空或全是空白字符
    if not item.strip():
        continue
    title, content, tt = get_data(item)
    result = tt + "\n" + content
    date = tt.split()[0]
    with open("./data/notes/{}-{}.txt".format(date, title), "w") as f:
        f.write(result)
