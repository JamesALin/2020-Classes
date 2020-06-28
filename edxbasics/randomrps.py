import random
print('Please choose between rock, paper, or scissors: ')
user_input = str(input())
computer_choice = random.choice(['rock', 'paper', 'scissors'])
if (user_input == 'rock' and computer_choice == 'paper'):
    print('I selected ', computer_choice, ', and you selected ' ,user_input, ', so I WIN!')
elif (user_input == 'rock' and computer_choice == 'scissors'):
    print('I selected ', computer_choice, ', and you selected ' ,user_input, ', so YOU WIN!')
elif (user_input == 'paper' and computer_choice == 'scissors'):
        print('I selected ', computer_choice, ', and you selected ', user_input, ', so I WIN!')
elif (user_input == 'paper' and computer_choice == 'rock'):
            print('I selected ', computer_choice, ', and you selected ', user_input, ', so YOU WIN!')
elif (user_input == 'scissors' and computer_choice == 'rock'):
    print('I selected ', computer_choice, ', and you selected ' ,user_input, ', so I WIN!')
elif (user_input == 'scissors' and computer_choice == 'paper'):
    print('I selected ', computer_choice, ', and you selected ' ,user_input, ', so YOU WIN!')
elif (user_input == computer_choice):
    print('I selected ', computer_choice, ', and you selected ' ,user_input, ', so we TIE!')
else:
    print('unknown choice xxx')