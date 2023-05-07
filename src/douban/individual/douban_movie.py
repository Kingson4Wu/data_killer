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

    ls = s.xpath('//div[@class="grid-view"]/div/div[1]/a/@title')

    info = s.xpath('//div[@class="grid-view"]/div/div[2]/ul/li[1]/a/em/text()')

    for item in ls:
        print(item)

    return ls, info


url = "https://movie.douban.com/people/labali/collect?start={}&sort=time&rating=all&filter=all&mode=grid"

start = 0
result = ""
result2 = ""
while True:
    datas, infos = get_data(url.format(start))
    result += "\n".join(datas)
    result += "\n"

    result2 += "\n".join(infos)
    result2 += "\n"

    if len(datas) < 15:
        break
    start += 15

if not os.path.exists("data"):
    os.mkdir("data")
with open("./data/movie.txt", "w") as f:
    f.write(result)
with open("./data/movie_info.txt", "w") as f:
    f.write(result2)
