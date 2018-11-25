# 1.2 Practice

#5
# 编程求解1-4这4个数字可以组成多少个无重复的三位数，按从小到大的顺序输出这些数字。

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != k and i != j and j != k:
                print(100*i+10*j+k)
        
