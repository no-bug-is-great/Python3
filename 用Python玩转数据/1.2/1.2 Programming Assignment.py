# 1.2 Programming Assignment

# 寻找第6个默尼森数
# 经典程序设计问题：找第n个默尼森数。P是素数且M也是素数，并且满足等式M=2**P-1，则称M为默尼森数。
# 例如，P=5，M=2**P-1=31，5和31都是素数，因此31是默尼森数。

from math import sqrt

# store Monisen numbers
cacheMonisen = []

# store prime numbers
cachePrime = []

# range for prime numbers
minNumber = 2
maxNumber = 100

def isPrime(x):
    '''check if x is prime'''
    k = int(sqrt(x))
    for i in range(2, k+1):
        if x % i == 0:
            return False
    return True

def addCachePrime():
    '''add prime numbers'''
    for i in range(minNumber, maxNumber):
        if isPrime(i) and (i not in cachePrime):
            cachePrime.append(i)
            
def monisen(no):
    '''get the nth monisen number'''
    
    addCachePrime()

    if no <= len(cacheMonisen):
        return cacheMonisen[no - 1]

    for i in cachePrime:
        p = i
        m = pow(2, p) - 1
        if isPrime(p) and isPrime(m):
            cacheMonisen.append(m)
        if no == len(cacheMonisen):
            break

    if no == len(cacheMonisen):
        return cacheMonisen[no-1]

    else:
        # if the range for prime numbers is not enough
        global minNumber, maxNumber
        minNumber, maxNumber = maxNumber, maxNumber * 2
        return monisen(no)

print(monisen(int(input())))
