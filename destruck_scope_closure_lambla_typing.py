# tuple1 = (1, 2)
# a, b = tuple1

# l1 = [1, 2, 3, 4, 5, 6]
# # _, a, *_, z = l1
# a, b, *_, z, _, _ = l1
# print(a)
# print(b)
# print(z)
# # print(_)

# d = {
#     "arg1": 1,
#     "arg2": 2,
#     "arg3": 3,
# }
#
#
# def a(arg1='a', arg2='a', arg3='a'):
#     print(arg1, arg2, arg3)
#
# a(**d)
#######################################################################################

# name = 'Max'


# def a():
#     # name = 'Vasia'
#
#     def b():
#         # name = 'Petia'
#
#         def s():
#             global name
#             name = 'Max'
#             print(name)
#             print(locals())
#
#         s()
#         # print(name)
#
#     b()
#     # print(name)
#
#
# a()
# # print(name)
# print(globals())


##############################################################
# def counter():
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         return count
#
#     return wrap
#
#
# conter1 = counter()
# conter2 = counter()
#
# print(conter2())
# print(conter2())
# print(conter1())
# print(conter2())
# print(conter1())
# print(conter2())
# print(conter2())

##################################################

# func = lambda x, y: x + y
# print(func(1,2))
l1 = [1, 2, 3, 4, 5]

# map_list = map(lambda x: x ** 2, l1)
# # print(map_list)
#
# # for i in map_list:
# #     print(i)
# #
# # # for i in map_list:
# # #     print(i)
# # res = list(map_list)
# # print(res)
# #
# # print(list(filter(lambda x: x < 4, l1)))
#
# # import functools
# from functools import reduce
#
# res = reduce(lambda a, b: a + b, l1)
# print(res)

######################################################################

# def replacer(st: str, ch1: str, ch2: str) -> str:
#     return st.replace(ch1, ch2)
#
#
# print(replacer('hello', 'l', 'a'))


# def counter() -> Callable:
#     count = 0
#
#     def wrap() -> int:
#         nonlocal count
#         count += 1
#         return count
#
#     return wrap
from typing import Callable, List, Tuple, Union, Optional, Dict

list1: List[int] = [1, 2]
list1.append('dfdf')

tuple1: Tuple[int, ...] = (2, 2, 3)


# def a(b: int) -> Union[int, str]:
#     if b > 5:
#         return b
#     return 'ha'
#
#
# def a(b: int) -> Optional[int]:
#     if b > 5:
#         return b
#
#
# print(a(3))


def a(b: Dict[int, str]) -> Optional[int]:
    # if b > 5:
    #     return b
    pass
a({'d':1})