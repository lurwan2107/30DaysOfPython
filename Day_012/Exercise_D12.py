from random import randint
import random

# 1 generating a list of hexadecimal colors

color = []
n = 6

for i in range(n):
    color.append('#%06X' % randint(0, 0xFFFFFF))


print('\nThe list of hexadicimal colors are as folloows:')
print(f'\n{color}')

# 2 def shuffle_list():
def shuffle_list():
    lst = [2, 3, 5, 1, 7, 8]
    print(f'\nThe original list is:\n{lst}')
    new1 = random.sample(lst, len(lst))
    print(f'\nThe shuffle list is:\n{new1}\n')
    

    #print(f'The shuffle list is:\n{lst}')


print(shuffle_list())