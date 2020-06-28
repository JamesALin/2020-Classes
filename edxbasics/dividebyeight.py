print('please enter an integer')
user_input = int(input())
whole = int(user_input // 8)
remainder = int(user_input % 8)
floatinteger = float(user_input / 8)
output_sentence = str(user_input) + ' divided by 8 is ' + str(whole) + 'R' + str(remainder) + ' or ' + str(floatinteger) + '.'
print(output_sentence)