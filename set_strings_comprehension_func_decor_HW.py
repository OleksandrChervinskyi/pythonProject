# strings

# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
st = 'as 23 fdfdg544'
str_list = [i for i in st if i.isdecimal()]
# print(str_list)


# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
st = 'as 23 fdfdg544 34, dsfsd .sdfsd, 44,v23 ,434 dfd/ sf4 5'
result = str()

for i in st:
    if i.isdigit():
        result += i
    else:
        result += ' '
result = ', '.join(result.split())
# print(result)

# #################################################################################
# list comprehension

# 1)есть строка:
# записать каждый символ в лист поменяв его на верхний регистр
greeting = 'Hello, world'
new_greeting = [i.upper() for i in greeting if i.isalnum()]
# print(new_greeting)

# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
odd_numbers_to_power = [pow(i, 2) for i in range(50) if i % 2 != 0]


# print(odd_numbers_to_power)
#
# function
#
# - створити функцію яка виводить ліст
def print_list():
    print([1, 2, 3, 4])


# print_list()

# - створити функцію яка приймає три числа та виводить та повертає найменьше.
# - створити функцію яка приймає три числа та виводить та повертає найбільше.
# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# - створити функцію яка виводить ліст
# - створити функцію яка повертає найбільше число з ліста
# - створити функцію яка повертає найменьше число з ліста
# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
def action_fn(*args, **kwargs):
    numbers_list = [i for i in args if isinstance(i, int)]

    if kwargs['options'] == 'max':
        print(max(numbers_list))
    elif kwargs['options'] == 'min':
        print(min(numbers_list))
    elif kwargs['options'] == 'printMax-returnMin':
        print(max(numbers_list))
        return min(numbers_list)
    elif kwargs['options'] == 'sum':
        print(sum(numbers_list))
        return sum(numbers_list)
    elif kwargs['options'] == 'avg':
        print(sum(numbers_list) / len(numbers_list))
        return sum(numbers_list) / len(numbers_list)
    else:
        return


# action_fn(1, 2, 3, 54, 6, -2, 'mad', options='avg')

####################################
# decorators
# - є функція:
#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення
# функцию pr менять не можно

def decor_change_underlines(f):
    def inner():
        correct_str = f().replace('_', ' ')
        print(correct_str)
        return correct_str

    return inner


@decor_change_underlines
def pr():
    return 'Hello_boss_!!!'


# pr()
