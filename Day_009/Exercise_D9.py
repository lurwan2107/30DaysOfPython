# EXERCISE LEVEL1
# 1
get_age = int(input('Enter your age'))
if get_age >= 18:
    print('you are old enough to learn to drive')
else:
    print(f'you need {18 - get_age} more years to learn to drive')
# 2
a = int(input('Enter number one: '))
b = int(input('Enter number two: '))
if a > b:
    print(str(a) + ' is greater than ' + str(b))
elif a < b:
    print(f'{a} is smaller than {b}')
else:
    print('%d is equal to %d' %(a, b))
# 3
fruits = ['banana', 'orange', 'mango', 'lemon']
if 'lemon' not in fruits:
    print(fruits.append('lemon'))
else:
    print('The fruits already exist')
# 4
grade = int(input('Enter yor grade: '))
if grade >=80 and grade <=100:
    print('A')
elif grade >=70 and grade <=79:
    print('B')
elif grade >=60 and grade <=69:
    print('C')
elif grade >= 50 and grade <=59:
    print('D')
elif grade >=0 and grade <=49:
    print('C')

