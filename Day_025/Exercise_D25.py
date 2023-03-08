import pandas as pd
import numpy as np

# 1. Reading the hacker_news.csv file

read_file = pd.read_csv('hacker_news.csv')
print(read_file)

# 2. Getting the first 5 rows

first_5_rows = read_file.head() #This method will autmatically give first 5 rows
print(first_5_rows)

# 3. Getting the last 5 rows

last_5_rows = read_file.tail() #This method will also give last 5 rows
print(last_5_rows)

# 4. Getting the title column as pandas series

tytle = read_file['title']
print(tytle)

# 5. Counting the number of rows and columns

print(read_file.shape) #Shape method will give the number of rows and columns

# 5(i). Filter the titles which contain python

print(read_file[read_file['title'] == 'python'])

# 5(ii). Filter the titles which contain JavaScript

print(read_file[read_file['title'] == 'JavaScript'])