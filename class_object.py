# class (Lớp) và object (đối tượng)
# tất cả các class cần có __init__ nó là hàm khởi tạo
class Car:
    def __init__(self, name, brand, color):
        self.name = name
        self.brand = brand
        self.color = color

    def drive (self):
        print(f"Driving the {self.name} of brand {self.brand} has color is {self.color}")

my_car = Car("vuHoang",brand="BMW" ,color="Blue")
my_car.drive()