# 1.2 Practice

#7
# 一个数如果等于它的因子之和则称这个数为完数，例如6，6=1+2+3，
# 编程计算1000之内的所有完数并输出。

for i in range(1, 1001):
    s = 0
    for j in range(1, i):
        if i % j == 0:
            s += j
    if s == i:
        print('\n', i, ' ', end = '')
        print('its factors are ', end = '')
        for j in range(1, i):
            if i % j == 0:
                print(j, ' ', end = '')
