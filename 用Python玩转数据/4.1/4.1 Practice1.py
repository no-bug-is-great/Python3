# 4.1 Practice

'''
利用豆瓣电影 API（参考url：https://developers.douban.com/wiki/?title=movie_v2，
注意要遵循其API权限规定）获取id是1291546的电影条目信息，输出其评分的平均值和电影的中文名。
中文电影名和评分均值是以下哪一个选项？4部电影的id分别为1295644, 1292720, 1291546, 1292052（并非选项A-D的顺序）
提示：用GET方法获得的数据是JSON格式的，需要先解码（data = r.json()）。

A. 阿甘正传 9.4
B. 肖申克的救赎 9.6
C. 这个杀手不太冷 9.4
D. 飞越疯人院 9.1

Answer: D. 飞越疯人院 9.1
'''
import requests
r = requests.get('https://api.douban.com/v2/movie/subject/1292224')
data = r.json()
print(data['title'], data['rating']['average'])
