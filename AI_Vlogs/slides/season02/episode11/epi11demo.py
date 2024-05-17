def my_firstfunction(num1):
    print(f"This  is my first function {num1}")
    
my_firstfunction(10)

def add(num1,num2):
    return num1+num2

print(add(5,10))

x = add(5,10)

def add_mul(num1,num2,num3):
    add1 = num1+num2+num3
    mul1 = num1*num2*num3
    return add1,mul1

add1,mul1 = add_mul(10,2,3)

def add_mul_2(num1=2,num2=3,num3=4):
    def addition_operations(num1,num2,num3):
        return num1+num2+num3
    def multiplication_operations(num1,num2,num3):
        return num1*num2*num3
    
    return addition_operations(num1,num2,num3), multiplication_operations(num1,num2,num3)

v= add_mul_2(2,3,4)

print(list(range(1,3+1)))

def factorial(num):
    total = 1
    for i in range(1,num+1):
        total = total * i
    return total

z = factorial(5)

v1= add_mul_2()

def my_generator():
    n = 1
    yield n
    n = n+1
    yield n
    
g = my_generator()

print(next(g))
print(next(g))

def my_generator_generic(first,last):
    n = first
    while n <= last:
        yield n
        n = n + 1

g1 = my_generator_generic(1,10)

v2 = next(g1)
v3 = next(g1)
v4 = next(g1)


