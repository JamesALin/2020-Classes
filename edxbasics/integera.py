print('please enter an integer for the variable, a: ')
a = int(input())
if(a < 0):
    print('please enter another integer for the variable, b: ')
    b = int(input())
    a = int(a*b)
    if(a < 0):
        a = a*(-1)
        print(a)
    else:
        print(a)
else:
    print(a)
