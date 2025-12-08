print("Sinh viên : Lê Văn Nam")
print("Mssv : 245752021610121")
from math import *

def get_sum(*num):
    tmp = 0
 # duyet cac tham so
    for i in num:
      tmp += i
    return tmp
result = get_sum(1, 2, 3, 4, 5)
print(result)

