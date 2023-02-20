# EXERCISE LEVEL1
# 1
def add_two_numbers(a, b):
    return a + b

print(add_two_numbers(12, 8))

# 2

def area_of_circle (r):
    pi = 3.14
    area = pi * r * r
    return area
print(area_of_circle(9))

# 3
def add_all_nums(*z):
    total = 0
    for k in z:
        total += k
    return total
print(add_all_nums(7, 4, 11))

# 4
def solve_quadratic_eqn(a, b, c, x):
    return a*x**2 + b*x + c
print(solve_quadratic_eqn(1, 3, 2, -1))

# 5
def print_list(lst):
    for i in lst:
        print(i)
print_list([1, 2, 3, 4, 5])

