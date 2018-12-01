# 2.2 Practice

#7
'''
文件article.txt中存放了一篇英文文章（请自行创建并添加测试文本），假设文章中的标点符号
仅包括“,”、“.”、“!”、“?”、“…”和“;”，编程找出其中最长的单词并输出。
'''

with open('article.txt') as fp:
    data = fp.read()
words = data.split()
lst = []
for word in words:
    if word[-3:] == '...':
        word = word[:-3]
        lst.append(word)
    elif word[-1] in ',.?!;':
        word = word[:-1]
        lst.append(word)
    else:
        lst.append(word)
result = sorted(lst, key = len, reverse = True)
print(result[0])

m = len(result[0])
# There may be tie
for word in result[1:]:
    n = len(word)
    if n == m:
        print(word)
    else:
        break
