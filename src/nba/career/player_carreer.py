# -- coding: utf-8 --

import requests
from lxml import html
import pandas as pd

etree = html.etree


def to_csv(url):
    data = requests.get(url).text
    s = etree.HTML(data)

    ls = s.xpath('//*[@id="in_box"]/div/div[1]/table[2]/tbody/tr')

    d = [[] for j in range(len(ls))]
    for j in range(1, len(ls) + 1):
        for i in range(19):
            a = ls[j - 1].xpath('td[' + str(i) + ']/text()')
            b = str(a)
            c = b[2:-2]
            d[j - 1].append(c)

    data1 = pd.DataFrame(d)

    r = url.split('/')
    r = r[len(r) - 1]
    r = r.split('.')
    r = r[0]
    data1.to_csv('data/' + r + '_season.csv')


to_csv('https://nba.hupu.com/players/lebronjames-650.html')
to_csv('https://nba.hupu.com/players/stephencurry-3311.html')
to_csv('https://nba.hupu.com/players/klaythompson-3564.html')
to_csv('https://nba.hupu.com/players/draymondgreen-3672.html')
to_csv('https://nba.hupu.com/players/kevindurant-1236.html')
to_csv('https://nba.hupu.com/players/kawhileonard-3568.html')
to_csv('https://nba.hupu.com/players/jamesharden-3306.html')
to_csv('https://nba.hupu.com/players/kyrieirving-3554.html')
to_csv('https://nba.hupu.com/players/jimmybutler-3583.html')
to_csv('https://nba.hupu.com/players/russellwestbrook-3016.html')
to_csv('https://nba.hupu.com/players/demarderozan-3314.html')