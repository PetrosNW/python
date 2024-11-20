class Person:
    def __init__(self, name):
        self.name = name
    
    
    def talk(self):   
        print(f"hi, i am {self.name}") 
 
person1 = Person("Peter waweru")        
person1.talk() 

# inheritance
class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")

        
class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walk()
            
