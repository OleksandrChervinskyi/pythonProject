# Создать класс записной книжки
# -А каждая манипуляция над ней должна быть методом класса
# -Все данные сохраняем в переменной класса
#  реализовать записную книжку покупок:
# - каждая запись должна содержать название покупки и ее цену
# -сделать менюшку для работы с записной книжкой:
#     '1) Создать запись'
#     '2) Список все записей'
#     '3) Общая сумма всех покупок'
#     '4) Самая дорогая покупка'
#     '5) Поиск по названию покупки'
#     '9) Выход'
# - можете придумать свои пункты
#
# но в этот раз данные записываем в файл
import json
from typing import List

# Get list from file
try:
    with open('all_record.json', 'r') as file:
        exist_list = list(json.load(file))
except FileNotFoundError:
    pass


class NoteBook:
    # Initial list
    try:
        _all_records: List = exist_list
    except NameError:
        _all_records: List = []

    def __init__(self, name_of_goods, price_of_goods):
        self._price_of_goods: float = price_of_goods
        self._name_of_goods: str = name_of_goods

    def save(self):
        new_one = {'name_of_good': self._name_of_goods, 'price_of_good': self._price_of_goods}
        NoteBook._all_records.append(new_one)
        with open('all_record.json', 'w') as list_file:
            json.dump(NoteBook._all_records, list_file)

    @classmethod
    def get_all_records(cls):
        return cls._all_records

    @classmethod
    def get_total_price(cls):
        total_price: float = 0
        for good in cls._all_records:
            total_price += float(good['price_of_good'])

        return total_price

    @classmethod
    def get_most_expensive_good(cls):
        price_list = [int(i['price_of_good']) for i in cls._all_records]

        try:
            print(price_list)
            return max(price_list)
        except ValueError:
            print('List is empty')

    @classmethod
    def search_by_name(cls, name_of_good: str):
        selected = list(filter(lambda value: value['name_of_good'] == name_of_good, cls._all_records))
        if len(selected):
            return selected
        return 'Not found'

    @classmethod
    def del_by_name(cls, name_of_good):
        updated_list = list(filter(lambda value: value['name_of_good'] != name_of_good, cls._all_records))
        NoteBook._all_records = updated_list
        with open('all_record.json', 'w') as list_file:
            json.dump(NoteBook._all_records, list_file)


def restart():
    answer = input('Продолжить (Введите "1" или "0") : ')
    if answer == '1':
        return 'Ok'


def nav():
    print('1) Создать запись')
    print('2) Список все записей')
    print('3) Общая сумма всех покупок')
    print('4) Самая дорогая покупка')
    print('5) Поиск по названию покупки')
    print('6) Удалить запись по названию покупки')
    print('7) Выход')

    selected_action = input('Вибор : ')

    if selected_action == '1':
        # - Создать запись
        name = input('Введите название : ')
        price = input('Введите цену : ')
        if price.isdigit():
            new_good = NoteBook(name, price)
            new_good.save()

            # Restart def
            if restart():
                nav()
        else:
            print('Укажите цену числом')

    elif selected_action == '2':
        # - Список все записей
        print(NoteBook.get_all_records())

        # Restart def
        if restart():
            nav()

    elif selected_action == '3':
        # -  Общая сумма всех покупок
        print(NoteBook.get_total_price())

        # Restart def
        if restart():
            nav()

    elif selected_action == '4':
        # Самая дорогая покупка
        print(NoteBook.get_most_expensive_good())

        # Restart def
        if restart():
            nav()

    elif selected_action == '5':
        # Поиск по названию покупки
        name = input('Введите название : ')
        print(NoteBook.search_by_name(name))

        # Restart def
        if restart():
            nav()

    elif selected_action == '6':
        # Удалить запись по названию покупки
        name = input('Введите название : ')
        NoteBook.del_by_name(name)

        # Restart def
        if restart():
            nav()

    elif selected_action == '7':
        # Виход
        return
    else:
        print('Відсутній варіант')


nav()
