# 1
print('Thirty ' + ' Days ' + ' Of ' + ' Python')
# 2
print('Coding ' + ' For ' + ' All')
# 3
company = "Coding For All"
# 4
print(company)
# 5
print(len(company))
# 6
print(company.upper())
# 7
print(company.lower())
# 8
print(company.capitalize())
print(company.title())
print(company.swapcase())
# 9
print(company[0:6])
# 10
check_if = 'Coding'
print(company.index(check_if))
print(company.find('Coding'))
# 11
print(company.replace('Coding', 'Python'))
# 12
changing_fmt = 'Python for Everyone'
print(changing_fmt.replace('for Everyone', 'for All'))
# 13
print(company.split())
# 14
spliting_var = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(spliting_var.split(', '))
# 15
    # The character at index 0 in the string 'Coding for All' is (C).
# 16
    # The last index in the string 'Coding for All' is (14-1)
# 17
    # The character at index 10 in the string 'Coding for All' is (r)
# 18
acronym1 = 'Python For Everyone'
print(acronym1[0], acronym1[7], acronym1[11])
# 19
acronym2 = 'Coding For All'
print(acronym2[0], acronym2[7], acronym2[11])
# 20
find_index = 'Coding For All'
new = 'C'
print(find_index.index(new))
# 21
new1 = 'F'
print(find_index.index(new1))
# 22
new2 = 'l'
print(find_index.rindex(new2))
# 23
first_occrnce = 'You cannot end a sentence with because because because is a conjunction'
new3 = 'because'
print(first_occrnce.index(new3))
# 24
new4 = 'because'
print(first_occrnce.rindex(new4))
# 25
first_occrnce = 'You cannot end a sentence with because because because is a conjunction'
print(first_occrnce[30:54])
# 26
print(first_occrnce.find('because'))
# 27
first_occrnce = 'You cannot end a sentence with because because because is a conjunction'
print(first_occrnce[30:54])
# 28
    # Yes
# 29
    # No
# 30
remove = ' Coding For All '
print(remove.strip(' '))
# 31
    # thirty_days_of_python
# 32
list_lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
list_join = '# '.join(list_lib)
print(list_join)
# 33
print('I \nam \nenjoying \nthis \nchallenge.')
print('I \njust \nwonder \nwhat \nis \nnext.')
# 34
print('Name \tAge \tCountry \tCity')
print('Asabeneh \t250 \tFinland \tHelsinki')
# 35
radius = 10
area = 3.142 * radius ** 2
print('The area of a circle with radius %d is %.2f meters square' %(radius, area))
# 36
x = 8
y = 6
print('{} + {} = {}'.format(x, y, x+y))
print('{} - {} = {}'.format(x, y, x-y))
print('{} * {} = {}'.format(x, y, x*y))
print('{} / {} = {:.2f}'.format(x, y, x/y))
print(f'{x} % {y} = {x % y}')
print(f'{x} // {y} = {x // y}')

