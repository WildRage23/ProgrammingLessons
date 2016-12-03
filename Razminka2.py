# number = input("Введите цифру ")
# if int(number) % 4 == 0:
#     print("Это число делится на 4")
# elif int(number) % 2 == 0:
#     print("Четное")
# else:
#     print("Не четное")

first = input("Введите число ")
second = input("Введите второе число ")
if int(first) % int(second) == 0:
    print("Без остатка")
else:
    print("С остатком")