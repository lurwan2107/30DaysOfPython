from datetime import datetime
time = datetime.now()
minute = time.minute
hour = time.hour
day = time.day
month = time.month
year = time.year
print(f'\n{minute}')
print(f'{hour}')
print(f'{day}')
print(f'{month}')
print(f'{year}')
print(f'{hour}:{minute}')
print(f'{day}/{month}/{year}\n')
timestamp = time.timestamp()
print('timestamp ', timestamp)
