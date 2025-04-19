class Student:     
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.__id_number = id_number
    
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old"

    def set_id_number(self, new_id_number):
        self.__id_number = new_id_number

    def get_id_number(self):
        return self.__id_number
    

student1 = Student("Abdul-khaliq", 25, 202449965)
print(student1.introduce())

student1.set_id_number("202449965")
print(student1.get_id_number())

student2 = Student("Mark", 24, 2024312)
print(student2.introduce())

student2.set_id_number("20202242")
print(student2.get_id_number())




