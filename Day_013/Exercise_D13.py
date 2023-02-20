# 1 filtering zero and negative numbers.

n = [-4, -3, -2, -1, 0, 2, 4, 6]
filtering = [i for i in n if i <= 0]
print(filtering)

# 2 flatten the list.

lst_of_lst = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flatten1 = [k for z in lst_of_lst for k in z]
flatten2 = [a for b in flatten1 for a in b]
print(flatten2)

# 3 outputting the list in the following order

lst_beauty = [(l,l+1,l*l,l*l*l,l*l*l*l,l*l*l*l,l*l*l*l*l) for l in range(11)]

print(lst_beauty)
print('\n')