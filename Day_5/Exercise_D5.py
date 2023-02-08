# 1
create = list()
    # or
itm = []
# 2
num_list = [1, 2, 3, 4, 5]
# 3
new = len(num_list)
# 4
first_itm = num_list[0]
middle_itm = num_list[2]
last_item = num_list[4]
# 5
mixed_data_types = ['lurwan', 27, 8.9, 'single', 'no.1 yardaji street']
# 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# 7
print(it_companies)
# 8
print(len(it_companies))
# 9
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])
# 10
it_companies[0] = 'Apple'
print(it_companies)
# 11
it_companies.append('Tweeter')
# 12
it_companies.insert(3, 'Instagram')
# 13
it_uppa = it_companies[2].upper()
# 14
join_it = '#; '.join(it_companies)
# 15
check_if = 'Facebook' in it_companies
# 16
sort_it = it_companies.sort()
# 17
reverse_it = it_companies.reverse()
# 18
print(it_companies[0:4])
# 19
print(it_companies[-3])
# 20
print(it_companies[4])
# 21
print(it_companies.remove('Facebook'))
# 22
print(it_companies.pop(4))
# 23
print(it_companies.pop(8))
# 24
print(it_companies.clear())
# 25
del it_companies
# 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
lst_join = front_end + back_end
# 27
full_stack = lst_join.copy()
insete_itm1 = full_stack.insert(5, 'Python')
insert_itm2 = full_stack.insert(6, 'SQL')
#  EXERCISE LEVEL2
# 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
find_max = max(ages)
find_min = min(ages)

add_max = ages.append(find_max)
add_min = ages.append(find_min)

mid_1 = ages[4]
mid_2 = ages[5]
print((mid_1 + mid_2) / 2)

average = sum(ages) / 10

find_range = range(find_max - find_min)

compare_value = abs(find_min - average) and abs(find_max - average)







