tu_than = "Tu thân"
te_gia = "Tề gia"
tri_quoc = "Trị quốc"
binh_Thien_ha = "Bình thiên hạ"

#sử dụng các hàm cơ bản
print(tu_than.upper()) #TU THÂN
print(te_gia.lower())  #tề gia
print(tri_quoc.isupper()) #False
print(tri_quoc.upper().isupper()) #True

#Thao tác với index
print(binh_Thien_ha[0]) #b
print(binh_Thien_ha[1:3]) #ìn
print(binh_Thien_ha.index("h")) #3
print(binh_Thien_ha.index("thiên")) #5
#print(binh_Thien_ha.index("Thiên")) #ValueError: substring not found
print(binh_Thien_ha.replace("hạ", "địa")) #Bình thiên địa


