class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
         return f"My name is {self.name} and I am {self.age} years old"

    def get_id_number(self):
        return self.__id_number
    
    def set_id_number(self, id_number):
        self.__id_number = id_number


student1 = Student("Abdul-khaliq", 25)
print(student1.introduce())

student1.set_id_number("202449965")
print(student1.get_id_number())

student2 = Student("Mark", 24)
print(student2.introduce())

student2.set_id_number("20204312")
print(student2.get_id_number())


