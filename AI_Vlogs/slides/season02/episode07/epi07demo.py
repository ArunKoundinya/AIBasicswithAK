
var = "AIBasics"

print(var == "AIBasics")

if var == "AIBasics":
    print("First Block")
    
if var != "AIBasics":
    print("Artificial")
else:
    print("AI")
    
var1 = 7

if var1 <= 5:
    print("Less Than 5")
elif var1 <= 8:
    print("Less than 8")
else:
    print("Greater than 8")
    
print(var1 <= 5)

print(var1 <= 8)

##for i in range(5):
  ##  print(i)
    
for i in range(5):
    if i == 3:
        break
    print(i)

sum = 0

for i in range(5):
    sum =  sum + i

print(sum)

i = 0

while i <= 5:
    print("This is statement",i)
    i = i +2
    


