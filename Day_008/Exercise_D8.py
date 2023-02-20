# 1
empty_dct = {}
# 2
dog = {'name':'poppy', 'color':'black', 'breed':'italian', 'legs':4, 'age':2}
# 3
student_dct = {'first_name' :'Lurwan', 'last_name' :'Abdullahi',
               'gender' :'male', 'age' :27, 'marital status' :'single', 'skills' :'Data scientist',
               'country' : 'Nigeria', 'city' :'Katsina', 'address' :'kofar kaura lay out katsina'}
# 4
print(len(student_dct))
# 5
key_s = student_dct.keys()
# 6
valu_es = student_dct.values()
# 7
print(student_dct.items())
# 8
del student_dct['male']
# 9
del student_dct