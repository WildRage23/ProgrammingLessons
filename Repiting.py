import random

name = input("Здравствуй, мой юный друг! Не подскажешь, как тебя зовут? ")
print("Ну чтож, " + name + ", я хочу с тобой сыграть в игру :):):):)Правила такие: Ты называешь мне цифру или число от 1 до 50, а я говорю тебе, больше ли твое число моего или меньше!Ну вобщем ты понял, да? И у тебя кстати 6 попыток будет всего")

while True:
    tries = 0

    difficult = input("Ыыбери себе сложность!! Легкий - диапозон от 1 до 30 и 6 попыток! Средний - диапозон от 1 до 65 и 9 попыток! Сложный - диапозон от 1 до 120 и 11 попыток! ")

    text = ""
    maxRange = 0

    if (difficult == "Легкий"):
        tries = 6
        text = "Так, ну называй число от 1 до 30 "
        maxRange = 30
    if (difficult == "Средний"):
        tries = 9
        text = "Так, ну называй число от 1 до 65 "
        maxRange = 65
    if (difficult == "сложный"):
        tries = 11
        text = "Так, ну называй число от 1 до 120 "
        maxRange = 120

    randomNumber = random.randint(1, maxRange)
    currentTry = 1

    while currentTry < tries:
        cifra = input(text)
        intCifra = int(cifra)
        while not intCifra >= 1 or not intCifra <= maxRange:
            print("Не годится!")
            cifra = input(text)
            intCifra = int(cifra)
        if (intCifra < randomNumber):
            print("Неет!!:):) Чет оно маленькое")
        if (intCifra > randomNumber):
            print(name + ", не угадал :):)Чет оно по больше")
        if (intCifra == randomNumber):
            print("ОООПАЧКИ!! ВЫ ТОЛЬКО ПОСМОТРИТЕ!!! ВЫ " + name + ", УГАДАЛИ!")
            print("Ух-ты!! Ты потратил целых " + str(currentTry) + " попыток!")
            break
        currentTry = currentTry + 1

    if (tries == currentTry and intCifra != randomNumber):
        print("Ну,чувак, я тебе " + tries + " попыток дал..ТЫ ПРОИГРАЛ ХЕХЕХЕХ :):) Число было " + str(randomNumber))

    continueGame = input("Хочешь сыграть ещё?")
    if (continueGame.lower() != "да"):
        break;
