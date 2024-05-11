list1 = []

list1 = list1 + [1,2,3]

list1.append(4)

list1.append('a')

list1.clear()

my_list = ['b','d','f']

my_list.insert(0,'a')

my_list.insert(2,'c')

my_list.insert(3,'e')

list1 = ['g','h','i']

my_list.extend(list1)

my_list.pop()

my_list.remove('a')

my_list.reverse()

my_list.clear()

sentence  = "We are learning python programming"

for i in sentence.split():
    print(i)
    
new_list = [i for i in sentence.split()]


letters = 'aeiou'

new_list1 = [i for i in letters]

