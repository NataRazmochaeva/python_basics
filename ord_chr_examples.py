S = input()

for symbol in S:
    print(ord(symbol))

code = int(input())
while code != 48:
    print('Вы ввели код: ', code, ', который соотвествует символу: ', chr(code))
    code = int(input())
