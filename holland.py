class Student:
    name: str
    age = 0
    def __init__(self,name,age):
        #two underscores makes something private
        self.__name = name
    def set_age(self, age):
        if age > 0:
            self.__age = age
    def get_age(self):
        return self.__age
    def get_name(self):
        return self.__name
    def greet(self):
        greet = print("Hello my name is ", name,"!")
    def set_name(self,name):
        self.__name
        
student1 = Student("Josef")
student1.set_age(-16)
student.set_name("JM")
print("Student Name: ", student1.get_name())
print("Student age: ".capitalize student1.get_age())
student1.set_age(16)
print("Student age: ", student1.get_age())
print(student1.greet())
