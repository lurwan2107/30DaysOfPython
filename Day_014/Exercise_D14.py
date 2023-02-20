# 1
"""1-The map() function is a built-in function that takes a function and iterable as parameters.
   What actually map does is iterating over a list. For instance, it changes the names to 
   uppercase and returns a new list. While
   2-The filter() function calls the specified function which returns boolean for each item of the 
   specified iterable (list). It filters the items that satisfy the filtering criteria. 
   3-Whhereas reduce does not return another iterable, instead it returns a single value."""

   # 2
"""1-Higher oredr function is proramming style that in which a function take another function
   as parameter or return them as result. While
   2-A nested function that access the outer scope of the enclosing function. is called Closure.
   closure is created by nesting a function inside another encapsulating function and then 
   returning the inner function."""

# 3

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for i in countries:
    print(i)

 # 4

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for name in names:
    print(name)

# 5

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    print(num)

# 6

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# function
def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, countries)
print(list(names_upper_cased))    

# 7

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

def change_to_upper(nm):
    return nm.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    

# 8

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def square_num(x):
    return x ** 2


numbers_squared = map(square_num, numbers)
print(list(numbers_squared))    
 