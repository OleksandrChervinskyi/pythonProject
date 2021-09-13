# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон
from typing import Dict, Union, List


class Rectangle:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def __add__(self, other):
        return (self.y * self.x) + (other.x * other.y)

    def __sub__(self, other):
        return (self.y * self.x) - (other.x * other.y)

    def __eq__(self, other):
        return (self.y * self.x) == (other.x * other.y)

    def __ne__(self, other):
        return (self.y * self.x) != (other.x * other.y)

    def __lt__(self, other):
        return (self.y * self.x) < (other.x * other.y)

    def __gt__(self, other):
        return (self.y * self.x) > (other.x * other.y)

    def __len__(self):
        return self.x + self.y


figure1 = Rectangle(20, 2)
figure2 = Rectangle(10, 2)


# print(figure1 + figure2, end=' - add\n')
# print(figure1 - figure2, end=' - sub\n')
# print(figure1 == figure2, end=' - eq\n')
# print(figure1 != figure2, end=' -ne\n')
# print(figure1 > figure2, end=' - lt\n')
# print(figure1 < figure2, end=' - gt\n')
# print(len(figure2), end=' - len\n')

##################
# Це завдання на наслідування... все максимально розбити по классах
# 1) написати програму для запису відомостей про пасажирські перевезення
# 2) перевезення відбувається трьома способами, літаком, машиною, поїздом
# 3) дані які треба буде зберігати:
# - вартість квитка(літак, поїзд)
# - кількість пасажирів(машина)
# - час в дорозі(всі)
# - час реєстрації(літак)
# - клас:перший,другий(літак)
# - вартість пального(# машина)
# - км(машина)
# - місце: купе,св(поїзд)
# 4) методи:
# - розрахунок вартості доїзду(машина)
# - загальний час
# перельоту(літак)
# - порівняти час в дорозі між двома будь якими транспортними засобами(двома об'єктами)
# - наприклад"літак на 5 годин швидше за поїзд" - вивести всі дані про перевезення(поїзд)
#
class Transport:

    def __init__(self, time_in_the_road):
        self.time_in_the_road: float = time_in_the_road

    def best_time(self, other) -> str:
        _best_time = abs(self.time_in_the_road - other.time_in_the_road)
        _degree_of_comparison = 'faster' if self.time_in_the_road < other.time_in_the_road else 'slower'
        return f'First is {_degree_of_comparison} on {_best_time} hours then second'


class Plane(Transport):

    def __init__(self, time_in_the_road, price_of_ticket, time_of_registration, type_of_class):
        super().__init__(time_in_the_road)
        self.type_of_class: str = type_of_class
        self.time_of_registration: float = time_of_registration
        self.price_of_ticket: int = price_of_ticket

    def total_way_time(self) -> float:
        return self.time_of_registration + self.time_in_the_road


class Train(Transport):

    def __init__(self, time_in_the_road, price_of_ticket, place):
        super().__init__(time_in_the_road)
        self.place: str = place
        self.price_of_ticket: float = price_of_ticket

    def get_all_details(self) -> Dict[str, Union[float, str]]:
        return {'time in road': self.time_in_the_road, 'place': self.place, 'ticket price': self.price_of_ticket}


class Car(Transport):

    def __init__(self, time_in_the_road, count_of_passengers, price_of_patrol, km):
        super().__init__(time_in_the_road)
        self.km: float = km
        self.price_of_patrol: float = price_of_patrol
        self.count_of_passengers: int = count_of_passengers

    def trip_price(self) -> float:
        return self.km * self.price_of_patrol


car1 = Car(5, 2, 29.8, 400)
car2 = Car(11, 3, 29.8, 200)

train1 = Train(7, 300, 'Kyiv')
train2 = Train(5, 200, 'Ternopil')

plain1 = Plane(11, 2000, 2, 'Econom')
plain2 = Plane(7, 5000, 1, 'Business')

# print(car1.best_time(plain2))
# print(plain2.total_way_time())
# print(train2.get_all_details())
# print(car1.trip_price())
# #############################

# 1)Створити пустий list
# 2)Створити клас Letter
# 3) створити змінну класу __count.
# 4) при створенні об'єкта має створюватись змінна об'єкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
# 5) при створені об'єкта __count має збільшуватися на 1
# 6) має бути метод(метод класу) для виводу __сount
# 7) має бути метод який записує в наш ліст текст з нашої змінної __text

empty_list = list()


class Letter:
    _count: int = 0

    def __init__(self, text):
        self._text = text
        Letter._count += 1

    @property
    def text(self):
        self._count += 1
        return self._text

    @text.setter
    def text(self, new_text):
        self._text = new_text

    @text.deleter
    def text(self):
        del self._text

    @classmethod
    def get_count(cls):
        return cls._count

    def add_to_list(self, some_list: List):
        some_list.append(self._text)


letter1 = Letter('Some text')
letter1.text = 'New text'
letter2 = Letter('Other text')
letter2.add_to_list(empty_list)
letter1.add_to_list(empty_list)

# print(letter1.text)
# print(letter1.get_count())
# print(empty_list)
