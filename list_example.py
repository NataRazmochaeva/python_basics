L = [int(item) for item in input().strip().split(' ')]
print("Исходный список: ", L)
# первый нулевой, второй нулевой элемент, произведение чисел между ними
M = L.copy()  # M[:]
if M.count(0) >= 2:
    first_index = M.index(0)
    M.remove(0)
    second_index = M.index(0)
    print("Измененный список: ", M)
    print("Индекс первого нуля: ", first_index, "\nИндекс второго нуля: ", second_index)
    mult = 1
    new_L = M[first_index:second_index]
    if first_index != second_index:
        for item in new_L:
            mult *= item
        print('Произведение чисел между первым 0-м и вторым 0-м', mult)
    else:
        print('Первый и второй ноль расположены рядом (друг за другом)')
else:
    print('В списке недостаточно нулей')


if M is not L:
    pass
