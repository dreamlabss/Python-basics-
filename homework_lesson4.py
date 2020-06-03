'''1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения
расчета для конкретных значений необходимо запускать скрипт с параметрами.'''

#from sys import argv
# name, time, salary, bonus = argv
# try:
#     time = int(time)
#     salary = int(salary)
#     bonus = int(bonus)
#     res = time * salary + bonus
#     print(f'заработная плата сотрудника  {res}')
# except ValueError:
#     print('Not a number')

'''2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.'''

my_list = [15, 2, 3, 1, 7, 5, 4, 10]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')

print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

'''3. Представлен список чисел. Определить элементы списка,
не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести
в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.'''

my_list = [6, 3, 3, 4, 1, 16, 78, 8, 3, 87, 78]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)

'''4 Реализовать формирование списка, используя
функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000
(включая границы). Необходимо получить результат
вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().'''

from functools import reduce


def my_func(el_p, el):
    return el_p * el

print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

'''5 Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа,
начиная с указанного,
б) бесконечный итератор, повторяющий элементы
некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle()
модуля itertools.'''

from itertools import cycle, count

for el in count(int(input('Введите стартовое число '))):
    print(el)

for el in cycle([1, 2, 3]):
    print(el)

'''Реализовать генератор с помощью функции с ключевым
словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом:
for el in fibo_gen().
Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые 15 чисел.
Подсказка: факториал числа n — произведение
чисел от 1 до n. Например, факториал
четырёх 4! = 1 * 2 * 3 * 4 = 24.'''

from itertools import count
from math import factorial

def fibo_gen():
    for el in count(1):
        yield factorial(el)

gen = fibo_gen()
x = 0
for i in gen:
    if x < 15:
        print(i)
        x += 1
    else:
        break