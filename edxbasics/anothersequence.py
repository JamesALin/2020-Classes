print('please enter an integer')

n = int(input())
last_int = 0
for counter in range(1, n+1):
    if counter %2 ==1:
        last_int = last_int + counter
    else:
        last_int = last_int - counter

