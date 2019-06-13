import requests, codecs
from lxml import html
import time
import random

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'}
f_cookies = open('cookie.txt', 'r')
cookies = {}
for line in f_cookies.read().split(';'):
    name, value = line.strip().split('=', 1)
    cookies[name] = value

# print(cookies)
for num in range(0, 1600, 20):
    url = 'https://movie.douban.com/subject/30331149/comments?start=' + str(
        num) + '&amp;limit=20&amp;sort=new_score&amp;status=P'

    ## https: // movie.douban.com / subject / 30135448 / comments?start = 20 & limit = 20 & sort = new_score & status = P
    with codecs.open('baise.txt', 'a', encoding='utf-8') as f:
        try:
            r = requests.get(url, headers=header, cookies=cookies)
            result = html.fromstring(r.text)
            comment = result.xpath(" // div[@class ='comment']/p//text()")
            # " // div[@class ='comment'] / p / text() "
            # //*[@id="comments"]/div[1]/div[2]/p/span
            # // *[ @ id = "comments"] / div[3] / div[2] / p / span
            for i in comment:
                f.write(i.strip().replace("\r","").replace("\n","")+'\n')
        except Exception as e:
            print(e)
    time.sleep(1 + float(random.randint(1, 100)) / 20)

import numpy as np
from snownlp import SnowNLP
import matplotlib.pyplot as plt

f = open('baise.txt', 'r', encoding='UTF-8')
li = f.readlines()
sentimentslist = []
for i in li:
    s = SnowNLP(i)
    # print s.sentiments
    sentimentslist.append(s.sentiments)

plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor='g')
plt.xlabel('Sentiments Probability')
plt.ylabel('Quantity')
plt.title('Analysis of Sentiments')
plt.show()

# coding=utf-8

import matplotlib.pyplot as plt
from scipy.misc import imread
from wordcloud import WordCloud
import jieba, codecs
from collections import Counter

text = codecs.open('baise.txt', 'r', encoding='utf-8').read()
text_jieba = list(jieba.cut(text))
c = Counter(text_jieba)  # 计数
word = c.most_common(800)  # 取前500
bg_pic = imread('src.jpg')
wc = WordCloud(
    font_path='C:\Windows\Fonts\simsun.ttc',  # 指定中文字体
    background_color='white',  # 设置背景颜色
    max_words=2000,  # 设置最大显示的字数
    mask=bg_pic,  # 设置背景图片
    max_font_size=200,  # 设置字体最大值
    random_state=20  # 设置多少种随机状态，即多少种配色
)

wc.generate_from_frequencies(dict(word))  # 生成词云
wc.to_file('result.jpg')
# show
plt.imshow(wc)
plt.axis("off")
plt.figure()
plt.imshow(bg_pic, cmap=plt.cm.gray)
plt.axis("off")
plt.show()
