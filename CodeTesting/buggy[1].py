# buggy.py - chapter 7, pag. 68
import random
number1 = random.randint(1,10)
number2 = random.randint(1,10)
print('What is ' + str(number1) + ' + ' + str(number2) + '?')
# input return string!
answer = input()
if int(answer) == number1 + number2:
    print('Correct!')
else:
    print('Nope! The answer is ' + str(number1 + number2))
