class Student:
    def __init__(self, grade = None):
        self.__grade = grade
    
    def get_grade(self):
        return self.__grade
    
    def set_grade(self, grade):
        if 0 <= grade <= 100 :
            self.__grade = grade

        else:
            print("The grade must be between 0 and 100")

student1 = Student()
student1.set_grade(10)
print(student1.get_grade())



    

