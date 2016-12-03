import datetime

name = input("Как вас зовут? ")
age = input("Сколько вам лет? ")
currentYear = datetime.datetime.now().year
god = 100 - int(age) + currentYear
print("Тебе в " + str(god) + " будет сто лет" )
