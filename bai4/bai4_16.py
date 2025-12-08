# Nhập chuỗi nhị phân, phân tách bằng dấu phẩy
binary_str = input("Nhập các số nhị phân, cách nhau bằng dấu phẩy: ")
binary_list = binary_str.split(',')

print("Các số nhị phân đã nhập:")
for b in binary_list:
    print(b)
