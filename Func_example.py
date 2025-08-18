"""
# các đoạn code nằm trong hàm phải thụt vào 1 tab so với tên hàm
# Hàm sẽ được thực thi khi chương trình bắt gặp lời gọi hàm
# Đặt tên hàm nên viết thường và cách nhau bằng gách dưới nếu có hơn 2 từ
"""
def say_hello(name):
    print(f"Hello {name}")

say_hello("Bob") #Hello Bob
say_hello("Vũ") #Hello Vũ

#Lệnh return trong hàm
def cong(a,b):
    return a+b
    # Những câu lệnh sau return sẽ không được thực thi
result = cong(1,2)
print(result) #3
print(cong(1.5,2.7)) #4.2

