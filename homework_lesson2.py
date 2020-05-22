# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type()
# для проверки типа.Элементы списка можно не запрашивать у пользователя, а указать явно,
# в программе.

# my_list = [1, 'dsf', 2.123, (234, 12, 3)]
# for a in my_list:
#     print(type(a))

# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
# элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо
# использовать функцию input().

# n = 0
# new_list = []
# foo = int(input('Введите сколько должно быть занчений в списке'))
# el = 0
# while n < foo:
#     new_list.append(input('Введите любое значение '))
#     n += 1
# if len(new_list) % 2 == 0:
#     i = 0
#     while i < len(new_list):
#         el = new_list[i]
#         new_list[i] = new_list[i + 1]
#         new_list[i + 1] = el
#         i += 2
# else:
#     i = 0
#     while i < len(new_list) - 1:
#         el = new_list[i]
#         new_list[i] = new_list[i + 1]
#         new_list[i + 1] = el
#         i += 2
# print(new_list)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# time = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
# number = int(input('Введите число месяца: '))
# if number < 12 or number > 0:
#     a = 0
#     for value in time.keys():
#         a = time[value]
#         if number in a:
#             print(f'Ваше число относиться к {value}')
#             break
# else:
#     print('Введен неверный формат даты')

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.Строки необходимо
# пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

# word = input('Введите строчку с несколькми словами: ')
# word_list = word.split(' ')
# i = 1
# for a in word_list:
#     print(f'{i}) {a}')
#     i += 1

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же
# значением должен разместиться после них.

# num = int(input('Поиграем в рейтинг ,введите число: '))
# my_list = [7, 5, 3, 3, 2]
# c = my_list.count(num)
# for el in my_list:
#     if c > 0:
#         i = my_list.index(num)
#         my_list.insert(i + c, num)
#         break
#     else:
#         if num > el:
#             j = my_list.index(el)
#             my_list.insert(j, num)
#             break
#         elif num < my_list[len(my_list) - 1]:
#             my_list.append(num)
# print(my_list)

# 6. Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
# номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

goods = []
while input("Would you like add product? Enter yes/no: ") == 'yes':
    number = int(input("Enter product number: "))
    features = {}
    while input("Would you like add product parameters? Enter yes/no: ") == 'yes':
        feature_key = input("Enter feature product: ")
        feature_value = input("Enter feature value product: ")
        features[feature_key] = feature_value
    goods.append(tuple([number, features]))
print(goods)

analitics = {}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analitics:
            analitics[feature_key].append(feature_value)
        else:
         analitics[feature_key] = [feature_value]
print(analitics)

