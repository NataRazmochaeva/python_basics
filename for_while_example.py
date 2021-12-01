# вывести на экран все числа из списка кратные 3
# %
# == 0

L = [int(item) for item in input("Введите элементы списка через запятую: ").split(',')]
print("Список целых чисел: ", L)

for item in L:
    if item % 3 == 0:
        print('Кратное 3-м: ', item)
    else:
        pass
else:
    print('Цикл завершен')
print('Код после цикла for')

for i in range(len(L)):
    pass

k = 0
while k < len(L):
    if L[k] % 3 == 0:
        print('Кратное 3-м:', L[k])
    k += 1  # k = k + 1, // k++;  *=, -=, /=, //=, %=

print('Код после цикла while')

