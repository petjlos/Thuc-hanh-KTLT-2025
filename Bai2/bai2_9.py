print("Sinh viên : Lê Văn Nam")
print("Mssv : 245752021610121")
from math import*
s= input()
dem ={}

for i in range(len(s)):
    c = s[i]
    if c in dem:
        dem[c] += 1
    else:
        dem[c] =1

print (dem)
