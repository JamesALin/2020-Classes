print('please enter a string:')
user_input = input()
ord_final = 0
for i in range(len(user_input)):
    if (user_input[i] != ' '):
        ord_final = ord_final + ord(user_input[i])
print(ord_final)        