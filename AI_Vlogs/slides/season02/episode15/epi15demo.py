#Person
#name,gender and age
# years_since_completed

class Person:
    def __init__(self,name,gender,age=0,graduate=False):
        self.name=name
        self.gender=gender
        self.age = age
        self.graduate = graduate
    
    def years_since_completed(self, years_completed):
        self.age = self.age + years_completed
        
        
    
    
Employee1 = Person("Arun","Male",37,True)

print(Employee1.age)

Employee1.years_since_completed(45)

