import math
my_age = 27                                                             # 1
my_height = 60.8                                                        # 2
store_complex = 7 - 18j                                                 # 3
# 4
base = int(input('Enter base: '))
height = float(input('Enter height: '))
area = 0.5 * base * height
print('The area of the triangle is ', area)
# 5
a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))
perimeter = a + b + c
print('The perimeter of the triangle is: ', perimeter)
# 6
rectangle_length = int(input('Enter the length: '))
rectangle_width = int(input('Enter the width: '))
area = rectangle_length * rectangle_width
perimeter = 2 * (rectangle_length + rectangle_width)
print('The perimetre of the rectangle is: ', perimeter)
# 7
radius_of_circle = float(input('Enter the radius: '))
r = radius_of_circle
pi = 3.14
area = pi * r * r
c = 2 * pi * r
print('The area of the circle is: ', area, ' and the circumference of the circle is: ', c)
# 8
x = 1
y = 2 * x - 2
print('The slope y intercept is: ',  2)
# 9
x1 = 2
y1 = 2
x2 = 6
y2 = 10
# slope
m = (y2 - y1)/(x2 - x1)
print('The slope is: ', m)
# Euclidian distance
d = (x2 - x1)**2 + (y2 - y1)**2
print('The Euclidian distance is: ', math.sqrt(d))
# 10
print(m > y)
# 11
x = -3
y = x**2 + 6*x + 9
print('y is going to be ', y, ' when value of x is ', x)
# 12
p = 'python'
d = 'dragon'
print('The length of ' + p + ' and ' + d + ' is ', len(p), ' and ', len(d))
print(d == p)
# 13
if('on' in p and 'on' in d):
    print('found')
# 14
sentence = 'i hope this course is not full jargon'
if('jargan' in sentence ):
    print('yes it is in sentence')
# 15

# 16
text = 'python'
temp = len(text)
print('convert ', temp, ' to ', float(temp), ' and also to string ', str(temp))
# 17
num = int(input("Enter any number: "))
if(num % 2 == 0):
    print(num, ' is even')
else:
    print(num, ' is odd')
# 18
to_cnvt = int(2.7)
if(7 // 3 == to_cnvt):
    print('The are the same')
# 19
str_type = '10'
int_type = 10
print(str_type == int_type)
# 20
num = int('9.8')
print(num == 10)
# 21
hour = int(input('Enter hours: '))
rate_per_hour = int(input('Enter rate per hour: '))
total = rate_per_hour * hour
print('Your weekly earning is: ', total)
# 22
years = int(input('Enter number of years you have lived: '))
days = 365
hour = 24
minute = 60
seconds = 60
total_seconds = days * hour * minute * seconds
print('You have lived for ', total_seconds, ' seconds.')
# 23
print("""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125""")



