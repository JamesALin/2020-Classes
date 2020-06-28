print('Please enter a positive integer: ')
n = int(input())
first = 1
second = 2
for counter in range(1, n + 1):
    if (counter <= 2):
        new = counter
    else:
        new = first + second
        first = second
        second = new
    print(new, end='\t')