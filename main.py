numbers = [1, 2, 3, 4, 5, 7]
print(numbers[1:5])

ru = [1, 2, 3, 4,]
eu = [5, 6, 7, 8, 9]

ru.extend(eu)
print(ru)

names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
names.append('oscar')
print(names)
if 'oscar' in names:
   names.remove('oscar')
print(names)

pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
f_loop = pythonList.index('loop')
pythonList.pop(f_loop)
print(pythonList)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
alfa = a[0] * a[1] * a[2] * a[3] * a[4] * a[5] * a[6] * a[7] * a[8] * a[9] * a[10]
print(alfa)

numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
print(numbers[1:3])

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for b in a:
   if b>5:
    print(b)

spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
numbers = []
spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
letters = []
for i in spisok_1:
    if str(i).isdigit():
        numbers.append(int(i))
print(numbers)
for y in spisok_2:
    if str(y).isalpha():
        letters.append(y)
print(letters)
