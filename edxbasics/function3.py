user_string = input('please enter a string:')
range1 = int(input('please enter a number:'))
range2 = int(input('please enter a number:'))
def slice(user_string, range1, range2):
    ret = ''
    if (range1 < 0):
        range1 = len(user_string) + range1
    if (range2 < 0):
        range2 = len(user_string) + range2
    for counter in range(range1, range2):
        ret = ret + user_string[counter]
    return ret
ret = slice(user_string, range1, range2)
print(ret)