# -- coding: utf-8 --

import requests
from lxml import html
import os

etree = html.etree

from ..common import file


def is_empty_or_whitespace(input_str):
    return len(input_str.strip()) == 0


def download_mp3(url):
    # data = requests.get(url).text
    with open('./chapter3.html') as ff:
        data = ff.read()
    # print(data)
    s = etree.HTML(data)
    # ls = s.xpath('//div[@class="grid-view"]/div/div[1]/a/@title')
    ls = s.xpath('//ul[@class="smenu"]/dd/text()')
    dirs = []
    for item in ls:
        print(item)
        if not is_empty_or_whitespace(item) > 0:
            file.create_directory(item)
            dirs.append(item)

    ls_mp3 = s.xpath('//div[@data-role="collapsibleset"]')
    print(len(ls_mp3))
    for index, item in enumerate(ls_mp3):
        ls_mp3_per = item.xpath('./div/h3/text()')
        ls_mp3_per_ = item.xpath('./div/audio')
        names = []
        for iitem in ls_mp3_per:
            names.append(iitem)
        for i, iitem in enumerate(ls_mp3_per_):
            print(dirs[index])
            print(names[i])
            print(iitem.attrib['src'])
            link = iitem.attrib['src'].strip()
            if not link.startswith("http"):
                link = "http://www.1kao.com.cn/qr/3064/" + link
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'}
            response = requests.get(link, headers=header)
            if response.status_code == 200:
                mp3_content = response.content
                mp3_path = os.path.join(dirs[index], names[i] + '.mp3')

                with open(mp3_path, "wb") as mp3_file:
                    mp3_file.write(mp3_content)
                print(f"MP3 文件已下载并保存到 {mp3_path}")
            else:
                print("下载失败")
                print(response.status_code)


download_mp3("")
