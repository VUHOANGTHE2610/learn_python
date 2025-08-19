# #trò chơi đoán chữ
# secret_word = "python"
# hint = "đây là một ngôn ngữ lập trình"
# guess = ""
# count_guesses = 0
# print(hint)
# while guess != secret_word :
#     if count_guesses < 5:
#         guess = input("bạn đoán đây là tử gì: ")
#         count_guesses += 1
#     else:
#         break
#
# if guess == secret_word:
#     print("bạn đã đoán đúng")
# else:
#     print("bạn đã thất bại ")
#
#
# # Tính lũy thừa
# def calculate_power(base_number, exponent):
#     result = 1
#     for exponent in range(exponent):
#         result = result * base_number
#     return result
#
# print(calculate_power(2, 3)) #8

# CHUYỂN ĐỔI NGÔN NGỮ
def translate(text):
    translation = ""
    for char in text:
        if char.lower() in "áàảãạăắằẵặâấầẫậ":
            if char.isupper():
                translation += "A"
            else:
                translation += "a"
        else:
            translation += char
    return translation
print(translate("Hoàng")) #Hoang
print(translate("HOÀNG")) #HOANG
"""
đây là hoàng thế vũ
"""