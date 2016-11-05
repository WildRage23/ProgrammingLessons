import random
from viselica import *

def playAgain():
    restart = input("\nБудешь еще? ")
    return restart.lower().startswith('д')

# SLOVA = ["Курица" ,"Огурчик", "Иголка", "Козел" ]
SLOVA = ["курица"]
errors = 4
randomslovo = SLOVA[random.randint(0, len(SLOVA) - 1)]
chertochki = '_' * len(randomslovo)
ugadanieBukvi = ''

while True:
    print(HANGMANPICS[errors])
    print("Неправильные буквы: ")
    for i in range(len(randomslovo)):
        if (randomslovo[i] in ugadanieBukvi):
            chertochki = chertochki[:i] + randomslovo[i] + chertochki[i + 1:]
    for bukva in chertochki:
        print(bukva, end=' ')
    bukva = input("\nВведите букву ")
    if (bukva in randomslovo):
        ugadanieBukvi = ugadanieBukvi + bukva



    # if not playAgain():
    #     break