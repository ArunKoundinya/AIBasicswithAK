my_dict = dict()

fruits_inventory = {
    'Apple' :  10,
    'Banana': 2,
    'Oranges': 0,
    'Black Berries': 20,
    'Kiwi': 0,
    'Avacado': 0  
}

print(fruits_inventory['Kiwi'])

fruits_inventory['Kiwi'] = 4

fruits_inventory['Oranges'] = 3

fruits_inventory['Avacado'] = 1

fruits_inventory['Watermelon'] = 1


print('Watermelon' in fruits_inventory)

print('Chicken' in fruits_inventory)

print(len(fruits_inventory))
print(fruits_inventory.keys())

for key,value in fruits_inventory.items():
    print("Fruit Name is ", key, ", we have ",value, "of them.")
    

    
sentence = "let us learn python programming"

print(set(sentence))

for letters in set(sentence):
    print(letters, sentence.count(letters))
    
value = {letters:sentence.count(letters) for letters in set(sentence)}

print(type(value))