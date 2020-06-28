input1 = input('please enter a string:')
input2 = input('please enter a phrase:')
found = False
for i in range(len(input1)):
    if (input2 == input1[i:len(input2) + i]):
        print(i)
        found= True
        break
if (found == False):
    print("not found")
