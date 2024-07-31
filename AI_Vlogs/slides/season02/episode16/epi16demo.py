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

## Child Class : Employee
## Attribute : is_postgraduate
## Internal attribute : company_experience
## Method : years_working

class Employee(Person):
    
    def __init__(self, name, gender, age=0, graduate=False,is_postgraduate = False):
        super().__init__(name, gender, age, graduate)
        self.is_postgraduate = is_postgraduate
        self.company_experience = 0
    
    def years_working(self, years_completed):
        self.years_since_completed(years_completed)
        self.company_experience = self.company_experience + years_completed
        
Employee2 = Employee("Arun","Male",37,True,True)

Employee2.years_working(3)
 
