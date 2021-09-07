print(1, 3, 4, sep='-', end=' finish\n')

i = 3
f = 1.2
b = True
n = None
s = 'ss'
some_text = 'ff'

type(3)

int1 = int('4')

a = b = c = 10

a += 1

b = a / b  # Float
b = a // b  # Int
b = a % b  # Остача
b = a ** b  # Степінь

inp = input('Enter str')

int(), float(), str(), bool()
######################

l = [1, 2, 3]  # List
l2 = [22.4, 5]
l[-2]  # By index
l[1] = 2

del l[1]
len(l)
l.append('11')
l.insert(2, 'value')
l.pop(0)
new_l = l.copy()
# l.remove(2)
l.extend(l2)  # add into list
# l.index('5', 0, 3)  # find by index
# l.sort(reverse=True)
l.count('2')
l.clear()
l.reverse()
new_list = l[2:6:2]  # Слайс з другого по шостий індекс з кроком 2

#####################

# Bool
a = 5
b = 6
a == b
a != b
a is b  # Порівнює не значення, а місце в памяті
a is not b

# If
if 5 < 6:
    print('True')
elif 5 > 2:
    print('Goofd')
else:
    print('dd')

# Ternar
num = int(input('Enter the number: '))
res = 'yes' if num > 5 else 'no'
print(res)

# In
5 in [1, 2, 3, 4, 5]

#################################

# Tuple - Кортеж (незмінний list)
tuple1 = ('Anna', 22, 'women')
tuple1[-1]
#tuple1.count()
tuple1.index('Anna')

#################################

# Dict - словарь - обьект
d = dict(name='Vas', age=12)
d1 = {'name': 'Maks', 'age': 33}

d1['name']
name = d1.get('name', 'nothing')  # якщо немає виведе None, дргуий параметр - що вивиодить якщо нічого немає
d1.clear()
d1.copy()
dict.fromkeys(['name', 'age'], 'template_value')  # без значень тільки ключі
d1.keys()
d1.items()  # кортежі повертає обгорнути в list()
#name = d1.pop('name')
# pop_item = d1.popitem()  # delete random item
d1.setdefault('name2', 'max2')  # добавляє значення і ключ, а якщо ключ вже є то нічого не робить
d1.values()

#####################
# Loops
list3 = [1, 2, 5, 67, 7, 9]
dict2 = {'name': 'Alex', 'age': 22}

for item in list3:
    print(i)

for key, value in dict2.items():
    print(key)
    print(value)

i = 5
while i > 0:
    print(i)
    i -= 1
else:
    print('final')