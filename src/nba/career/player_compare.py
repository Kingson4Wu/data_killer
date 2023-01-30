# -- coding: utf-8 --

import matplotlib.pyplot as plt
import os

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['figure.figsize'] = [15, 8]

files = os.listdir('data/')
print(files)

yy = []
starts = []
recents = []

legends = []

for index in range(len(files)):

    legends.append(files[index].split('.')[0].split('-')[0])
    f = open('data/' + files[index], 'r')
    y = []
    try:
        text_lines = f.readlines()
        for i in range(len(text_lines)):
            if i == 0 or i == 1:
                continue
            data = text_lines[i].split(',')
            if data[3] == '汇总':
                continue
            year = int(data[2])

            if len(y) == 0:
                starts.append(year)
                recents.append(year)
            else:
                recent = recents[index]
                if year == recent:
                    continue
                while recent + 1 < year:
                    y.append(0)
                    recent += 1
            recents[index] = year
            y.append(float(data[len(data) - 1].strip()))
        yy.append(y)
    finally:
        f.close()

start = starts[0]
for s in starts:
    if s < start:
        start = s

end = recents[0]
for r in recents:
    if r > end:
        end = r

x = []
for i in range(start, end + 1):
    x.append(i)

yyy = []
for index in range(len(yy)):
    ss = starts[index]
    ee = recents[index]
    s = start
    y = []
    while ss > s:
        y.append(0)
        s += 1
    for t in yy[index]:
        y.append(t)
    while ee < end:
        y.append(0)
        ee += 1
    yyy.append(y)



for y in yyy:
    plt.plot(x, y)

plt.title('历年场均得分')
plt.xlabel('年份')
plt.ylabel('得分')


for y in yyy:
    for a, b in zip(x, y):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

from matplotlib.ticker import MaxNLocator
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))

plt.xticks(ticks=x)


plt.legend(legends)
plt.show()

