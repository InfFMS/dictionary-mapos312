# Напишите программу, которая получает на вход строку чисел, разделенных пробелами, и формирует словарь,
#  в котором ключами служат числа, а значениями – слово "четное" или "нечетное".
numbers = input()
x = [int(n) for n in numbers.split()]
dict_1 = {n: 'чётное' for n in x if n % 2 == 0}
dict_2 = {n: 'нечётное' for n in x if n % 2 != 0}
dict_1.update(dict_2)
print(dict_1)