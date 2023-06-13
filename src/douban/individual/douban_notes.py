# -- coding: utf-8 --

import requests
from lxml import html
import os
import re

etree = html.etree


def get_data(url):
    # 418, 访问的网站有反爬虫机制，而解决方法就是通过模拟浏览器来访问

    # 从文件中读取curl语句
    with open('./curl/notes.txt') as ff:
        curl_command = ff.read()

    # 使用正则表达式匹配header字段
    header_pattern = r"-H '([\w-]+): ([^']*)'"
    header_matches = re.findall(header_pattern, curl_command)

    # 将匹配到的header解析到字典中
    headers = {}
    for header_match in header_matches:
        headers[header_match[0]] = header_match[1]

    # 打印解析得到的header字典
    print(headers)

    data = requests.get(url, headers=headers).text
    s = etree.HTML(data)

    ls = s.xpath('//div[@class="article"]/div[@class="note-container"]/@data-url')

    for item in ls:
        print(item)

    return ls


url = "https://www.douban.com/people/labali/notes?start={}&type=note&_i=6670839nZDCOIK"


start = 0
result = ""
while True:
    datas = get_data(url.format(start))
    result += "\n".join(datas)
    result += "\n"

    if len(datas) < 10:
        break
    start += 10

if not os.path.exists("data"):
    os.mkdir("data")
with open("./data/notes.txt", "w") as f:
    f.write(result)
