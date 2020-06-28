print('please enter a negative integer from the decimal number system')
user_input = int(input())
twos_complement = 256 + user_input
output_sentence = str(user_input) + ' in the 8-bit twos complement system is ' + str(bin(twos_complement))
print(output_sentence)