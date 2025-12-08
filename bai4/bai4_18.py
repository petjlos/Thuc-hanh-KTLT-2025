n = int(input("Nhập n: "))
fib = [0, 1]

while True:
    nxt = fib[-1] + fib[-2]
    if nxt >= n:
        break
    fib.append(nxt)

print("Danh sách Fibonacci nhỏ hơn n:", fib)
