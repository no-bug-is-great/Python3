# 3.1 Practice

#3
'''
自定义函数twonums_sum(n, lst)，在列表lst中查找是否有两数之和等于n，若有则返回两数的下标，否则返回-1。
对于一个不包含重复数字的有序列表[1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 18, 19, 20, 21, 29, 34, 54, 65]，
从键盘输入n，调用函数twonums_sum()输出满足条件的两个数的下标（找到一组即可且要求其中的一个数尽量小），
若所有数均不满足条件则输出“not found”。
Exampe Input:
17
Example Output:
(1, 10)
'''
def twonums_sum(n, lst):
    d = {}
    for i in range(len(lst)):
        d[lst[i]] = i
    for i in range(len(lst)):
        if n - lst[i] in d:
            return i, d[n-lst[i]]
    return -1

lst = [1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 18, 19, 20, 21, 29, 34, 54, 65]
n = int(input())
result = twonums_sum(n, lst)
if result == -1:
    print("not found")
else:
    print(result)
