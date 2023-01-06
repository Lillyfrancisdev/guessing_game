
#GUESSING GAME

print('WELCOME TO THE GUESSING GAME!')
print('You have 10 chances to hit.\n')

import  random
randomnumber = random.randint(1, 50)
print('I am thinking of a number between 1,50.')
guess = int(input('Can you guess a number?'))

chances = 10
while guess:
    if randomnumber == guess:
        chances -= 1
        print(f'Congratulation,you won!')
        break
    elif guess >= randomnumber:
        chances -= 1
        print(f'Your number is too high.You still have,{chances} chances.')
        guess = int ( input ( 'Can you guess a number?' ) )
    elif guess <= randomnumber:
        chances -= 1
        print(f'Your number is to low.You still have,{chances} chances.')
        guess = int ( input ( 'Can you guess a number?' ) )
    else:
        guess = int ( input ( 'Can you guess a number?' ) )






