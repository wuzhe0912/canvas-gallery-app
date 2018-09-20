fruits = ['apple', 'banana', 'orange', 'pineapple']

print(fruits[2])
print(fruits[1:])
print(fruits[:3])

print(fruits[1:3])
print(len(fruits))

fruits.append('mango')
print(fruits)

fruits.pop()
print(fruits)

if 'apple' in fruits:
    print('Apple is a fantastic fruit!')
