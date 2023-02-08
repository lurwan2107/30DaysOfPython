# EXERCISE LEVEL1
# 1
empty_tpl = ()
#empty_tpl = tuple()
# 2
sisters_tpl = ('Hauwau', 'Maryam', 'Rahma')
brothers_tpl = ('Abubakar', "Saminu", 'Aminu')
# 3
sibilings = brothers_tpl + sisters_tpl
# 4
print(len(sibilings))
# 5
modify_siblngs = list(sibilings)
family_members = ['Abdillahi', 'Aisha' ] + modify_siblngs
print(family_members)

# EXERCISE LEVEL2
# 1
*faza, sib1, sib2, sib3 = family_members
# 2
fruits = ('Apple', 'Orange', 'Mango', 'Banana')
vegetables = ('Cabbage', 'Tomato', 'Onion')
animal = ('Cow', 'Goat', 'Chicken')
food_stuff_tp = fruits + vegetables + animal
# 3
food_stuff_lt = list(food_stuff_tp)
# 4
print(food_stuff_tp[4:6])
# 5
print(food_stuff_lt[0:4])
print(food_stuff_lt[7:10])
# 6
del food_stuff_tp
# 7
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
check_if1 = 'Estonia' in nordic_countries
check_if2 = 'Iceland' in nordic_countries



