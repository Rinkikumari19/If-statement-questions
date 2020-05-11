# def encrypt():
#   message = raw_input("Enter the message you want to encrypt ")
#   ascii_message = [ord(char)+3 for char in message]
#   encrypt_message = [ chr(char) for char in ascii_message]  
#   print ("".join (encrypt_message))


# def decrypt():
#   message = raw_input("Enter the message you want to decrypt ")
#   ascii_message = [ord(char)-3 for char in message]
#   decrypt_message = [ chr(char) for char in ascii_message]  
#   print ("".join(decrypt_message))
# flag=True
# while flag == True:
#     choice = raw_input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter E or D respectively! ")
#     if choice == 'E':
#         encrypt()
#     elif choice == 'D':
#         decrypt()    
#     else:
#         play_again = raw_input("Do you want to try agian or Do you want to exit? (Y/N) ")
#         if play_again == 'Y':
#             continue
#         else:
#             break




import random
def getSecretNum(numDigits):
# # Returns a string that is numDigits long, made up of unique random digits.
  numbers = list(range(10))
  random.shuffle(numbers)
  print(numbers)
  secretNum = ''
  for i in range(numDigits):
    secretNum += str(numbers[i])
  print(secretNum)
  return secretNum

def getClues(change, secretNum):
  change = (str(change))
  # print(type(change))
  print(secretNum)
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
    # elif len(clue) == 0:
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
    return play == ('yes')

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
    print ("running")
    change = input("change Again")
    while len(secretNum) == NUMDIGITS or isOnlyDigits(secretNum):
      print("inside")
      # print ('change') + str(numchangees)
      clue = getClues(change, secretNum)
      print(clue)
      if change == secretNum:
        break
      elif numchangees > MAXchange:
        print ('You ran out of changees. The answer was ' + secretNum)
        break
      else:
        print(type(numchangees))
        numchangees = numchangees + 1

  if not playAgain():
    break
 