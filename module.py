# tìm hiểu nhiều module hơn tại Python module index
import vuhoang_methob
import qrcode
print(vuhoang_methob.football_club())

# sử dụng module qrcode
# sử dụng pip (là một trình quản lý gói) đã được cài mặc địn trong python
image = qrcode.make("https://vuhoang.github.io")
image.save("qrcode.png", format="png")