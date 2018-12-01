# 2.2 Practice

#5
'''
从键盘输入整数n（1-9之间），对于1-100之间的整数删除包含n并且能被n整除的数，例如如果n为6，
则要删掉包含6的如6，16这样的数及是6的倍数的如12和18这样的数，输出所有满足条件的数，
要求每满10个数换行。
'''

n = int(input("Enter the number: "))
count = 0
new_str = ''
print("The result string: ")

for i in range(101):
    s = str(i)
    if i % n != 0 and s.find(str(n)) == -1:
        new_str = new_str + s + ','
        count += 1
        if count % 10 == 0:
            print(new_str[:-1])
            new_str = ''
if len(new_str) > 0:
    print(new_str[:-1])
