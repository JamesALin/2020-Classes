import math
print('please enter 2 integers: ')
side1 = int(input('Side 1:'))
side2 = int(input('Side 2:'))
def theorem():
    tri_hypotenuse = math.sqrt(side1*side1 + side2*side2)
    return tri_hypotenuse
print(theorem())