sentence = input("Nhập một câu: ")

letters = sum(c.isalpha() for c in sentence)
digits = sum(c.isdigit() for c in sentence)

print("Số chữ cái là:", letters)
print("Số chữ số là:", digits)
