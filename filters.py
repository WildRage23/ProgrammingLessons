import random

BAD_WORD_LIST = ['Fuck', 'Shit', 'Asshole', 'Bullshit']
BAD_WORD_REPLACE = ['Pony', 'Flower', 'Love', 'Bird', 'Kitty', 'Butterfly']

def filterAndPrintMessage(message):
    for badWord in BAD_WORD_LIST:
        if (badWord in message):
            message = message.replace(badWord, BAD_WORD_REPLACE[random.randint(0, len(BAD_WORD_REPLACE) - 1)])
    return message

def askUserForMessage(question):
    message = input(question)
    return filterAndPrintMessage(message)