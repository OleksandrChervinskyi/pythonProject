# # try:
# #     jkdhgdjkfhg
# # except NameError as e:
# #     print(e)
# #
# # print('dfdf')
#
# def div(a, b):
#     return a / b
#
#
# try:
#     print(div(3, 0))
# # except Exception
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# except TypeError as e:
#     print(e)
# else:
#     print('all right')
# finally:
#     print('finish')


# l = [i for i in range(50000000)]
# input('wait')

# g = (i for i in range(50000000))
# for i in g:
#     print(i)

# g = (i for i in range(2))
# try:
#     print(next(g))
#     print(next(g))
#     print(next(g))
# except StopIteration:
#     print('finish')


# def gen(name):
#     for ch in name:
#         yield ch
#
#
# g = gen('Max')
#
# # print(type(g))
#
# print(next(g))
# print('help')
# print(next(g))
# print(next(g))

import uuid


def gen_jpg_file():
    pattern = '{}.jpg'
    while True:
        yield pattern.format(uuid.uuid1())


file_name = gen_jpg_file()

# print(next(file_name))
#
# try:
#     file = open('1.txt', mode='r')
#     # read = file.read()
#     # read = file.readlines()
#     # read2 = file.readline()
#     # read3 = file.readline()
#     print(read)
#     # print(read2)
#     # print(read3)
# except FileNotFoundError:
#     print('нет такого файла')

# try:
#     file = open('1.txt', mode='w+')
#     file.write('my file2\n')
#     file.seek(0)
#     print(file.read())
# except FileNotFoundError:
#     print('нет такого файла')

# try:
#     file = open('1.txt', mode='a')
#     file.write('my file2\n')
#     # file.seek(0)
#     # print(file.read())
#     file.close()
# except FileNotFoundError:
#     print('нет такого файла')

# with open('123.jpeg', 'rb') as file:
#     data = file.read()
#     for i in range(20):
#         with open(next(file_name), 'wb') as file2:
#             file2.write(data)


# import pickle
#
# user = {'name': 'Max', 'age': 150}
#
# with open('user.user', 'wb') as file:
#     pickle.dump(user, file)
#
# with open('user.user', 'rb') as file:
#     new_user = pickle.load(file)
#     print(new_user)


import json

user = {'name': 'Max', 'age': 150}

with open('user.json', 'w') as file:
    json.dump(user, file)

with open('user.json', 'r') as file:
    new_user = json.load(file)
    print(new_user)