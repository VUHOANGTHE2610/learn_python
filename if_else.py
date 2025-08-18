a = 5
b = 10
c = 1
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b") #a is less than b
else:
    print("a is equal to b")

# các toán tử logic
if a >= b and a <= c: # cần cả hai điều kiện điều là true
    print("a là số lớn nhất")

if a == b or a < c: # chỉ cần 1 trong hai diều kiện là true
    print("chỉ là ví dụ thôi")

if  not a > b: # đão ngược giá trị điều kiện trả về nếu là true sẽ chuyễn thành false và ngược lại
    print("a không lớn hơn b")
