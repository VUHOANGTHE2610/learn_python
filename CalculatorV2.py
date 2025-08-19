num1 = float(input("Nhập số thứ nhất: "))
operator = input("Nhập vào toán tử")
num2 = float(input("Nhập số thứ hai: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Toan tu khong hop le")