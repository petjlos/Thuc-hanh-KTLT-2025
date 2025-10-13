from math import *

x, y = map(int,input().split())
def tong(x,y):
    return x + y

def tru(x, y):
    return x - y

def nhan(x, y):
    return x * y

def chia(x, y):
    return x/y

if __name__=="__main__":
     print(tong(x,y))
     print(tru(x,y))
     print(nhan(x,y))
     print(chia(x,y))
     