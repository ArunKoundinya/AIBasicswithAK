def add(num1):
    return num1+num1
print(add(3))

addlambda = lambda num1 : num1 + num1

print(addlambda(4))

print((lambda num1 : num1 + num1)(6))

def sq_cub(num1):
    return num1 ** 2, num1 ** 3

print(sq_cub(3))

sqcub_lambda = lambda num1 : (num1 ** 2, num1 ** 3)

print(sqcub_lambda(4))

mylist = [1, 2, 3, 4]

print(map(sqcub_lambda,mylist))

print(list(map(sqcub_lambda,mylist)))

mylist1 = [2, 3, 4, 5]

print(list(map(lambda num1 : (num1 ** 2, num1 ** 3),mylist1)))

print(list(filter(lambda num1 : (num1 ** 2, num1 ** 3),mylist1)))

print(list(filter(lambda num1 : num1 > 3,mylist1)))

print(list(map(lambda num1 : num1 > 3,mylist1)))


print(list(filter(lambda num1 : num1 > 2,mylist1)))
