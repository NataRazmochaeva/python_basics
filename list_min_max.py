"""
data = input("Введите строку: ")
sum_nums = 0
for symbol in data:  # for i in range(len(data)): ==> 0, 1, 2, ... len(data)-1
    if symbol.isdigit():
        sum_nums += int(symbol)
print('Сумма цифр из строки: ', sum_nums)
"""
L = [int(item) for item in input("Введите список чисел через пробел: ").split(' ')]
print('Разница между максимальным и минимальным: ', max(L)-min(L))
