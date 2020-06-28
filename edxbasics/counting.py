print('please enter an integer: ')
n = int(input())

final_int=0
for counter in range(1, n+1):
    final_int = counter + final_int


print(final_int)
