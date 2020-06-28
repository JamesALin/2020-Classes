user_string = input('please enter a string:')
range1 = int(input('please enter a number:'))
range2 = int(input('please enter a number:'))
def slice(user_string, range1, range2):
    ret = ''
    for counter in range(range1, range2):
        ret = ret + user_string[counter]
    return ret
ret = slice(user_string, range1, range2)
print(ret)