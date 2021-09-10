# 1) написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# - первый записывает в эту переменную запись
# - второй возвращает все записи
# запишите 5 тудушек
# и выведете все
# 2) протипизировать первое задание

from typing import Callable, Dict, List
from functools import reduce


def todos_list() -> Dict[str, Callable]:
    todos_list1: List[str] = list()

    def add_new(todo) -> None:
        nonlocal todos_list1
        todos_list1.append(todo)

    def get_all() -> List[str]:
        nonlocal todos_list1
        return todos_list1

    return {
        'add': add_new,
        'get': get_all
    }


first_todos_list = todos_list()
first_todos_list['add']('new Todo 1')
first_todos_list['add']('new Todo 2')
first_todos_list['add']('new Todo 3')
first_todos_list['add']('new Todo 4')
first_todos_list['add']('new Todo 5')
# print(first_todos_list['get']())

#########################################
# 3) С помощью lambda функции извлеките из списка числа, делимые на 15 без остатка.
some_list: List[int] = [1, 2, 4, 5, 55, 77, 8, 32, 6, 75, 11, 4, 45, 55, 15]

new_numbers_list = list(filter(lambda value: value % 15 == 0, some_list))


# print(new_numbers_list)
# print(new_numbers_list)

##################################################
# 4) написать функцию которая будет принимать целое число n и посчитайте n + nn + nnn.
def multi_number(some_int: int, count_of_times: int) -> None:
    total: int = 0
    for i in range(1, count_of_times):
        total += int(str(some_int) * i)
    print(total)


# multi_number(7, 4)

#############################################
# сделать функцию которая будет принимать число и будет считать количество уножений цифр этого числа,
# если в результате умножения получилась больше чем одна цифра условие повторяется а счетчик увеличивается на 1
# Пример:
# persistence(999)  # вернется 4, потому что было четыре действия 9*9*9=729, 7*2*9=126,
# # 1*2*6=12, и в конце 1*2=2
#
# persistence(4)  # вернется 0, потому что и так одна цифра

def persistence() -> Callable:
    counter: int = 1

    def multiplication(some_int: int) -> int:
        nonlocal counter
        if some_int < 9:
            return 0

        str_int: List[int] = [int(i) for i in str(some_int)]
        result_of_multiplication = reduce(lambda x, y: x * y, str_int)

        if result_of_multiplication > 9:
            counter += 1
            multiplication(result_of_multiplication)

        return counter

    return multiplication


new_number = persistence()

# print(new_number(777))
###########################################
