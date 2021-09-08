# list1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5, 4, 64, 65, 23, 757, 2, 645, 2, 7, 8, 3]
# list3 = [1, 2, 3, 4, 5, 6, 7, 8, 88, 5, 7, 88, 9, 9, 11, 56, 24, -100, -22, 44, 2]

# ***  - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
def find_nearest_number_to_average(some_list):
    # Find average
    total = 0
    for i in some_list:
        total = total + i
    average = total / len(some_list)
    print(average)

    #  Find nearest to average
    difference = 10  # random number
    nearest_to_average = 0  # template
    for i in some_list:
        local_different = abs(average - i)
        if local_different < difference:
            difference = local_different
            nearest_to_average = i
    print(nearest_to_average)


#################################

# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
# selected_size = int(input('Enter size: '))
def square(size):
    print(size * '*')
    c = 1
    while c < size - 1:
        print('*' + ((size - 2) * ' ') + '*')
        c += 1
    print(size * '*')


# square(selected_size)

##################################

# 3) вывести табличку умножения с помощью цикла while
# collum = 1
# while collum < 10:
#     row = 1
#     row_str = ''
#     while row < 10:
#         space = ' ' if row * collum >= 10 else '  '
#         row_str = row_str + str(row * collum) + space
#         row += 1
#     collum += 1
#     print(row_str)

# 4) переделать первое задание под меню с помощью цикла
list2 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


def nav(some_list):
    print(
        '1) Найти min число в листе\n'
        '2) Удалить все дубликаты в листе\n'
        '3) Заменить каждое четвертое значение на "Х"\n'
        '4) Вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа\n'
        '5) Exit')

    selected = input('Зробіть вибір : ')

    if selected == '1':
        # - найти min число в листе
        print(min(some_list))
    elif selected == '2':
        # - удалить все дубликаты в листе
        new_set = set(some_list)
        print(new_set)
    elif selected == '3':
        # - заменить каждое четвертое значение на "Х"
        counter = 1
        while counter < len(some_list):
            if (counter + 1) % 4 == 0:
                some_list[counter] = 'X'
            counter += 1
        print(some_list)
    elif selected == '4':
        find_nearest_number_to_average(some_list)
    elif selected == '5':
        return
    else:
        print('Відсутній варіант')

# nav(list2)
