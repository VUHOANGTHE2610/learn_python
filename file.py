# đọc file
# r chỉ được đọc
# w ghi đè
# a chỉ dược thêm
# có thể tương tác vói csv, html..
phone_book = open("text", "r", encoding="utf-8")
print(phone_book.readable()) # true

for line in phone_book.readlines():
    line = line.replace("\n", "")
    print(line)
phone_book.close()

#Ghi file
txt = open("new_text", "w", encoding="utf-8")
txt.write("\nVũ hoàng - 22")
txt.close()

#tương tác với html
html = open("index.html", "a", encoding="utf-8")
html.write("<p> xin chào</p>")
