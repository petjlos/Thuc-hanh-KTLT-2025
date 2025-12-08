n = int(input("Nhập n: "))

for i in range(1, n):
    sum_div = sum([j for j in range(1, i) if i % j == 0])
    if sum_div > i:
        print(i, end=' ')
