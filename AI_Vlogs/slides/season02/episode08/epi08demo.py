empty_list = []

var = [10.20 , 10, 20, 100]

print(type(var[0]))

var1 = [ 1 , 2, 3]

var2 = var1 + [5,6,7]

var3 = var1 * 5

var[0] =  40

var1 = var

var[0] = 100

empty_tuple = ()

var_tuple = (10.20 , 10, 20, 100)

var2_tuple  = (1,) * 5

var3_tuple = (1,3) +  (10,20)

var4_tuple = (1,3) + tuple([10,20])

var5  = list((1,3)) + [10,20]

print(var5[0])

var5[0] = 1000

print(var4_tuple[0])

var4_tuple[0] = 100