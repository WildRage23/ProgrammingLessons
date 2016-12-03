# a = [5, 11, 6, 76, 4, 87, 76, 32, 5]
# b = []
#
# chislo = input("Введите число ")
# for num in a:
#    if int(num)>int(chislo):
#     b.append(int(num))
#
# print(b)

number = input("Введите число ")
for i in range(1, int(number) + 1):
    if int(number) % i == 0:
        print(i)