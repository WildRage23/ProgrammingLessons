BAD_WORDS_LIST = ['Fuck', 'Duck']
BAD_WORD_REPLACER = 'Pony'

def badWordFilter(message):
    for badWord in BAD_WORDS_LIST:
        if (badWord in message):
            message = message.replace(badWord, BAD_WORD_REPLACER)
    return message

def askUserForMessage(ask):
    message = input(ask)
    return badWordFilter(message)