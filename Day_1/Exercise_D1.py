import math     # Because of Euclidian distance.

# Q1. python --version

# Q2. operators
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(3 % 4)
print(3 // 4)
print(3 ** 4)

# Q3. String
print('Your name')
print("Your family name")
print("your country")
print("I am enjoying 30 days of python")

# Q4. Checking data type
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Your name'))
print(type('Your family name'))
print(type('Your country'))

# EXERCISE LEVEL 3
# Q1. Data types
    # Number
print(7 + 11)
print(8.5 - 0.4)
print(7 + 9j)

    # String
print("My name is: Lurwan Abdullahi and i love ArewaDS very much")

    # Boolean
print(True)

    # List
print(['Apple', 'mango', 'banana'])

    # Tuple
print(('Egg', 'Bread', 'Milk'))

    # Set
print({1, 2, 3, 4, 5})

    # Dictionary
print({'FirstName':'Lurwan', 'LastName':'Abdullahi', 'State':'Katsina'})

# Q2. Finding Euclidian distance of (2 3) and (10 8):
    # a. To compute one dimensional Euclidian distance using 2 formulas
x = 2 - 3
print(abs(x))   # Absolute value formula
print(math.sqrt(x**2))   # Square root formula

    # b. To compute two dimensional Euclidian distance using 1 formula
a = (2-10)**2
b = (3-8)**2
c = a+b
print(math.sqrt(c))
