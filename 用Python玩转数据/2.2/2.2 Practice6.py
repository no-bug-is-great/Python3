# 2.2 Practice

#6
'''
请用随机函数产生500行1-100之间的随机整数存入文件random.txt中，
编程寻找这些整数的众数并输出，众数即为一组数中出现最多的数。
'''

import random

with open('random.txt', 'w+') as fp:
    for i in range(500):
        fp.write(str(random.randint(1, 100)))
        fp.write('\n')
    fp.seek(0)
    nums = fp.readlines()
    print("nums original:")
    print(nums)
nums = [num.strip() for num in nums]
print("nums after strip():")
print(nums)
setNums = set(nums)
print("setNums:")
print(setNums)

lst = [0] * 101
for num in setNums:
    c = nums.count(num)
    lst[int(num)] = c
for i in range(len(lst)):
    if lst[i] == max(lst):
        print(i)
