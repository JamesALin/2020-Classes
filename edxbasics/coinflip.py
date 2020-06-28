import random
print('please enter the amount of times you want to flip a coin.')
n = input()
while (n != 'end'):
    n= int(n)
    head_count=0
    for counter in range(n):
        newflip = random.randint(0,1)
        if (newflip == 1):
            head_count = head_count+1
    print('There are ', head_count, 'heads out of ', n, ' flips, the frequency of flipping a head is ', str(head_count / n))
    print('next: please enter the amount of times you want to flip a coin.')
    n = input()
