"""
1. На языке Python реализовать алгоритм (функцию) определения четности целого числа,
который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути.
Объяснить плюсы и минусы обеих реализаций.
"""


def isEven(value): return value % 2 == 0


def my_even(value): return value & 1 == False


"""
Второй вариант проверки числа на четность работает только с integer, 
в то время как первый вариант может принимать float значения.
Функция my_even() оснавана на битовом операторе И (bitwise AND)
"""
print(isEven(2))
print(my_even(4))
