print('please enter an integer for n:')
n = int(input())
for i in range(n+1):
    line = i*' ' + (n-i)*'*'
    print(line)