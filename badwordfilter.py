from filters import *

name = input('What is your name?: ')

messageToTheWorld = askUserForMessage('What is your message to the world?: ')

print(name + ' said to the world: ' + messageToTheWorld + '!')

messageToFriends = askUserForMessage('What is your message to friends?: ')

print(name + ' said to the world: ' + messageToFriends + '!')