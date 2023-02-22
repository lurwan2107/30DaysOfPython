# 1

import re
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words = paragraph.replace('.', '').split(' ')
dict = {}
for k in words:
    dict[k] = dict.get(k, 0) + 1
sort = sorted(dict.items(), key= lambda i: i[1], reverse=True)
for k, v in dict.items():
    print(v, k)



