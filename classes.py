# class User:
#     count = 0
#
#
# user1 = User()
# user2 = User()
# User.count = 5
# print(user2.count)

# class User:
#     _count = 0  # как би протектид
#
#     def __init__(self, name, age, sex): # Constructor
#         self.sex = sex
#         self.name = name
#         self.age = age
#
#     def __str__(self):  # Вертає строку/дікт
#         return str(self.__dict__)

# user = User('Max', 13)
# user.active = True
# print(User.__count)
# print(user)
# del user.name
# print(user)

# print(User._User__count) # обхід приватності


# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say(self):
#         print('hello')
#
#
# class Car:
#     def have(self):
#         print('I have a car')
#
#
# class User(Human, Car):  # наслідування
#     def __init__(self, name, age, active):
#         super().__init__(name, age)
#         self.active = active


# user = User('Max', 15, False)
# user.say()

# class User:   #get set - інкапсуляція
#     def __init__(self, name, age, active):
#         self._name = name
#         self._age = age
#         self._active = active
#
#     def _get_name(self):
#         return self._name
#
#     def _set_name(self, new_name):
#         self._name = new_name
#
#     def _delete_name(self):
#         del self._name
#
# Property (устарів)
#     my_name = property(fset=_set_name, fget=_get_name, fdel=_delete_name)
#
#
# user = User('Max', 12, True)
# # user.set_name('Karina')
# # print(user.get_name())
# user.my_name = 'Karina'  # як виконуються проперті
# print(user.my_name)
# del user.my_name # як виконуються проперті
# print(user.my_name)

# class User:  (нормальний варіант)
#     def __init__(self, name, age, active):
#         self._name = name
#         self._age = age
#         self._active = active
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, new_name):
#         self._name = new_name
#
#     @name.deleter
#     def name(self):
#         del self._name
#
#
# user = User('Max', 12, True)
# user.name = 'Karina' # як виконуються проперті
# print(user.name)


# class Shape: Поліморфізм (групування по сущності)
#     def area(self):
#         print('Area', end=': ')
#
#     def perimeter(self):
#         print('Perimeter', end=': ')


# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def area(self):
#         super().area()
#         print(self.a * self.b * self.c)
#
#     def perimeter(self):
#         super().perimeter()
#         print(self.a + self.b + self.c)
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         super().area()
#         print(self.a * self.b)
#
#     def perimeter(self):
#         super().perimeter()
#         print(self.a + self.b)
#
#
# shapes = [Rectangle(12, 23), Triangle(1, 2, 3)]
#
# for item in shapes:
#     item.area()
#     item.perimeter()

from abc import ABC, abstractmethod  # abstract basic class


# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#
# # shape = Shape() # так нельзя
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def area(self):
#         print(self.a * self.b * self.c)
#
#     def perimeter(self):
#         print(self.a + self.b + self.c)
#
#
# triangle = Triangle(1, 2, 3)
# triangle.area()


# class User:
#     _count = 5
#
#     def __init__(self, name, age):   # етод екземпляра класу (де є селф)
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     @classmethod   #класові методи працюють з перемеінними класу або з самим класом
#     def get_count(cls):   # cls - class
#         return cls._count
#
#     @staticmethod  #можна використовувати як від екземпляру так і від самого класу.
#     Часто  для класу, і описують лшгіку яка не відноститься ні до класу ні до екз (сервіси)

#     def greeting():
#         print('hello')
#
#
# print(User.get_count())
# User.greeting()

# Перегрузки методів - поведінка класу
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # В парі з репр
        return str(self.__dict__)

    def __repr__(self):  # Репрезентація вже не ссилки
        return self.__str__()

    def __len__(self): #  Що буде повертатись при len()
        return self.age

    def __add__(self, other): #  поведінка на +
        return self.age + other.age

    def __sub__(self, other): # на -
        return self.age - other.age

    def __mul__(self, other): # на *
        return self.age * other.age

    def __lt__(self, other): # на порівняння
        return len(self.name) < len(other.name)

    def __gt__(self, other): # >
        return len(self.name) > len(other.name)


user = User('Kira', 18)
user2 = User('Karina', 12)
print(user > user2)
# list_users = [user, user2]
# print(list_users)
# print(len(user2))

print(user + user2)
print(user - user2)
print(user * user2)
