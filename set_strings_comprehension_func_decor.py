#################

# SET - унікальні значення, без повторень, дублікати автоматично залишаться в одному виді
list1 = [1, 2, 3, 4]
set0 = set(list1)

set1 = {1, 2, 3, 4, 3, 4, 2}
set2 = {2, 3, 5, 6}

set2.add(9)
set1.issubset(set2)  # чи є перший сет в другому
set1.issubset(set2)
set1.isdisjoint(set2)  # чи є спільні елементи
set3 = set1.union(set2)  # обєднання
common = set1.intersection(set2)  # повертає спільні елементи
set1.difference(set2)  # то чого немає в другому
set1.symmetric_difference(set2)  # повертає дікт з унікалтними значеннями
set1.update(set2)
set1.remove(2)
random = set1.pop()  # remove random value

###################

# SRT
stirng = 'fff "sad" fdsf \' dfsdf'
name = 'Max'
age = 2

st = 'Hello mu name is ' + name + 'and age' + str(age)
st2 = 'Hello mu name is %s and age %d' % (name, age)
st3 = 'Hello mu name is {} and age {}'.format(name, age)
st4 = 'Hello my name is {name} and age {age}'.format(age=age, name=name)  # Better
st5 = f'Hello my name is {name} and age {age}'  # The best

st.index('l', 3)
st.count('oo')
st.capitalize()  # перша буква велика
st.upper()
st.lower()
st.isupper()  # чи всі великі
st.islower()
st.isalpha()  # чи всі з букв
st.startswith('a')
st.endswith('oo')
st.strip('a')  # забирає пробєли зліва і зправа по критерію "а"
st.rstrip()
st.lstrip()
st.split('-')  # ділить на елементи по сепаратору
st.partition('is')  # ділить на три частини з сепаратором по середині
lw = ['1', '12', '3']
new_str = st.join(lw)
st.isspace()  # чи є пробєли

############################
min(1, 2, 3)
max([1, 2, 4])
sorted([1, 2, 5, 67, 3], reverse=True)
pow(44, 2)  # степінь

#############################
# List comprehemption
list1 = [i + 10 for i in range(5) if i % 2 == 0]  # генерація при умові

list2 = [[1, 2, 4, 5, 6], [1, 3, 4, 6]]
res = [i for j in list2 for i in j]
for j in list2:
    for i in j:
        res.append(i)

dict1 = {'naMe': 'Max', 'aGe': 13}

res1 = {k.lower(): v for k, v in dict1.items()}
print(res1)


####################################
# functions

def fn():
    print('hello')


fn()


def fn2(a, b, c=3, *args, **kwargs):
    print(a, b, c, args, kwargs)
    # *args - після 3-го елементу все буде добавлено в кортеж
    # **kwargs - dict


dict3 = {'name': 'Max', 'age': 22}
fn2('ff', 11, 5, 656, 67, 32, 32, **dict3)

list4 = [1, 2, 3]


def new_fn(a, b, c):
    print(a + b + c)
    return a


res4 = new_fn(*list4)
print(res4)


# Decorator

def decor(f):
    def inner(*args, **kwargs):
        print('****')
        f(*args, **kwargs)
        print('---------')

    return inner


@decor
def new_func():
    print('Hello')


@decor
def greet(str):
    print(str)


new_func()
greet('ds')
