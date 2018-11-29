# 2.1 Practice

#1
# 请在豆瓣任意找一本图书，抓取它某一页的短评并进行页面解析将短评文字抽取后输出，
# 再对其中的评分进行抽取计算其总分。

import requests
from bs4 import BeautifulSoup
import re

s = 0
r = requests.get('https://book.douban.com/subject/26356948/comments/')
soup = BeautifulSoup(r.text, 'lxml')
pattern = soup.find_all('span', 'short')  
for item in pattern:
    print(item.string)
    
pattern_s = re.compile('<span class="user-stars allstar(.*?) rating"')
p = re.findall(pattern_s, r.text)
for star in p:
    s += int(star)
print(s)
