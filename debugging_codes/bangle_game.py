import random
def getSecretNum(numDigits):
# # Returns a string that is numDigits long, made up of unique random digits.
  numbers = list(range(10))
  random.shuffle(numbers)
  secretNum = ''
  for i in range(numDigits):
    secretNum += str(numbers[i])
  print(secretNum)
  return secretNum

def getClues(change, secretNum):
  change = (str(change))
# Returns a string with the pico, fermi, None clues to the user.
  if change == secretNum:
    return 'You got it!'
  clue = []
  for i in range(len(change)):
    if change[i] == secretNum[i]:
      clue.append('Fermi')
    elif change[i] in secretNum:
      clue.append('Pico')
    else:
      clue.append('None')
  return ' '.join(clue)

def isOnlyDigits(numsecretNum):
# Returns True if num is a string made up only of digits. Otherwise returns False.
    if secretNum == 'none':
        return False

    for i in secretNum:
        if int(i) not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False

def playAgain():
# This function returns True if the player wants to play again, otherwise it returns False.
    play = input("Do you want to play again? Yes or No?") 
    # print(play)
    # print(play.lower=="yes")
    # print()
    # return play.lower.startswith("y")
    return play == "yes"

NUMDIGITS = 3
MAXchange = 10

# print('I am thinking of a %s-digit number. Try to change what it is.' % (NUMDIGITS))
# print('Here are some clues:')
# print('When I say:    That means:')
# print('  Pico         One digit is correct but in the wrong position.')
# print('  Fermi        One digit is correct and in the right position.')
# print('  None       No digit is correct.')

while True:
  secretNum = getSecretNum(NUMDIGITS)
  print('I have thought up a number. You have %s changees to get it.', (MAXchange))
  numchangees = 1
  while numchangees <= MAXchange:
    while len(secretNum) == NUMDIGITS or isOnlyDigits(secretNum):
      change = input("change num")
      clue = getClues(change, secretNum)
      print(clue)
      if change == int(secretNum):
        break
      elif numchangees > MAXchange:
        print ('You ran out of changees. The answer was ' + secretNum)
        break
      else:
        numchangees = numchangees + 1
    if change == int(secretNum):
        break

  if not playAgain():
    break