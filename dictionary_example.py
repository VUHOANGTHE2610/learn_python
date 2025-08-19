# dictionary - từ điển
# Key | value
english_vietnamese_dictionary = {
    "hello": "Xin chào",
    "bye" : "tạm biệt",
    "help": "Cứu",
}

# Tương tác với dectionary
print(english_vietnamese_dictionary["hello"]) # Xin chào
print(english_vietnamese_dictionary.get("hello")) # Xin chào
print(english_vietnamese_dictionary.get("history", "từ khóa này không tồn tại ")) #từ khóa này không tồn tại