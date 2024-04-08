
var = "This is a string"

print(type(var))

print( var + var)

print( var * 2)

print( "A" * 2)

var1 = '''
Hi.
This in a sentence one
THis is second sentence
'''


var2 = "\
Hi.\
This in a sentence one\
THis is second sentence\
"

var3 = "Slice and Dice Me"

print(var3[0])

print(len(var3))

print(var3[16])

print(var3[10:14])

var4 = "I have only a 10$ bill with me"

### Indexing
print(var4[14:16])

print(var4.split('$'))

### StringOperator
print(var4.split('$')[0].split()[4])


print(var1.find("sentence"))

print(var1.rfind("sentence"))

print(var1[15:])

print(var1[43:])

print(var1.capitalize())

print(var3.capitalize())

print(var3.title())


variable1 = "You"

Variable2 = "Me"

print(f"{variable1:.^9} know my name")

print(f"{variable1:.>9} know my name")

print(f"{variable1:.<9} know my name")

var1 = 1
var2 = 2

print(f"{var1 + var2 * var2} This is the output of the operations")