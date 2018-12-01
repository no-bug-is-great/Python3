# 2.2 Practice

#1
'''
string = 'My moral standing is: 0.98765'
将其中的数字字符串转换成浮点数并输出。
'''

string = 'My moral standing is: 0.98765'
moral_str = string.split(":")[1]
result = float(moral_str)
print(result)
print(type(result))

