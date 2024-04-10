class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
    def introduce(self):
            print(f"Hello! My name is {self.name}. I am {self.age} years old and identify as {self.gender}.")
            
person1=Person("Lydiah", 19,"Female")

person1.introduce()            
            