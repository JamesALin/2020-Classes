scan = 0
user_input1 = input('Please enter a line: ')
user_input2 = input('Please enter a character: ')
i = 0
while (i <= len(user_input1)):
    j = i + len(user_input2)
    if (user_input1[i:j] == user_input2):
        scan = scan + 1
    i = i + 1
print(scan)