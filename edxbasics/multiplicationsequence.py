print('please enter an integer')
n = int(input())
last_int = 0
for counter in range(1, n+1):
    #next_int = last_int * counter
    #sum_int = next_int + counter
    last_int = last_int + counter*(counter+1)
print(last_int)