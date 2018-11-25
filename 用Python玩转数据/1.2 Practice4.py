# 1.2 Practice

#4
# 输入n，用递推法（例如前项之间的关系推导后项，本题为一重循环）编程
# 求1+2!+3!+...+n!的和并输出。

n = int(input())
s = term = 1

for i in range(2, n+1):
    term *= i
    s += term
print(s)
