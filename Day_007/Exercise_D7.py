it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# EXERCISE LEVEL1
# 1
find_len = len(it_companies)
# 2
it_companies.add('Twitter')
# 3
it_companies.update('Instagram', 'Snapchat', 'Messanger')
# 4
it_companies.remove('Apple')
# 5
# EXERCISE LEVEL2
# 1
C_1 = A.union(B)
# 2
A.intersection(B)
# 3
A.issubset(B)
# 4
A.isdisjoint(B)
# 5
C_2 = A.union(B)
C_3 = B.union(A)
# 6
del it_companies
del A
del B
del age
# EXERCISE LEVEL3
conv_t = set(age)
print(len(age) > len(conv_t))

