# Exception (ngoai le)
# throw an exception (ném ra ngoại lệ)
# handle exception (xử lý ngoại lệ)

#ví dụ 1
try:
    print(text)
except:
    print("có lỗi xảy")

 #ví dụ 2
try:
    a = int(input("nhập a: "))
    b = int(input("nhập b: "))
    result = a / b
    print(f"the result is {result}")
except ZeroDivisionError:
    print("mẫu số nhập vào phải khác 0 vuii lòng nhập lại ")
except ValueError:
    print("các số nhập vào phải là số nguyên")
except:
    print("có lôi xảy ra vui lòng liên hệ admin")


