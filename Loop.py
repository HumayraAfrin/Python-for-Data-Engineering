'''Loop - Control the flow of code
Repeat the flow of code over and over until the condition is met'''

items = (1, 2, 3, 4, 5)
for item in items:
    print(f'Round: {item}')


items = ' Python'
for item in items:
    print(f'Round: {item}')

for item in range(5):       # 0-4
    print(f'Round: {item}')


for item in range(1, 5):       # 1-4
    print(f'Round: {item}')

for item in range(1, 10, 2):       # 1, 3, 5, 7, 9
    print(f'Round: {item}')


'''We use for loops to go through values and aggregate the data like summing, counting, averaging'''

scores = [80, 50, 46, 30]
total = 0
for score in scores:
    total += score
    print('Current Total:', total)
print(f'Final Total: {total}')


'''We use for loops to trasform data like cleaning data before processing'''

files = [' Report.csv ', 'DATA.csv ', ' final.TXT'] #Inconsistent casing and unnecessary spaces
for file in files:
    file = file.strip().lower().replace('.txt', '.csv')     #Clean first, Transform second
    print(f'Processing {file}')


# Break

names = ['John', 'Maria', '', 'Kumar']

for name in names:
    if name =='':
        print('Empty Name Detected!')
        break
    print(f'Name: {name}')


# Continue

names = ['John', 'Maria', '', 'Kumar']

for name in names:
    if name =='':
        print('Empty Name Detected!')
        continue                        #Use continue to skip bad or empty data without stopping the whole loop
    print(f'Name: {name}')


# Pass

names = ['John', 'Maria', '', 'Kumar']

for name in names:
    if name =='':
        pass                        #to do: To handle the missing value, It is just placeholder to be changed later 
    print(f'Name: {name}')



'''Task - Loop through a list of days and print only the working days, skipping the weekends'''

Days = ['Monday', 'Friday', 'Sunday', 'Tuesday']
Weekends = ['Saturday', 'Sunday']

for Day in Days:
    if Day in Weekends:
        continue
    print(f'{Day} is a weekday.')
    

'''Task - Scan emails to block unsafe data from entering your system'''

emails = [
        'data@gmail.com',
        'baraa@outlook.de',
        'DROP TABLE USERS;'
        'maria@gmail.com'
]

for email in emails:
    if ';' in email:
        print('SQL Injection. Hacker Attack.')
        break
    print(f'Processing email: {email}')



# Python For - Else Loop
# Check for even numbers

items = [1, 3, 4, 7]

for item in items:
    if item%2 == 0:
        print('Even number found: ', item)
        break
else:   #this else is the part of for loop and it will run only if the loop is not interrupted.
    print('All numbers are odd.')


'''Task - Check for missing names in the list'''
names = ['Kamara', 'Monika', None, 'Maria']

for name in names:
    if name is None:
        print('Found a missing name.')
        break
else:
    print('All names are available.')


'''Check if all files are csv files'''
files = [
    'data1.csv',
    'report.pdf',
    'data2.txt',
    'report2.csv'
]
for file in files:
    if not file.endswith == '.csv':
        print('Not all files are csv.')
        break
else:
    print('All files are csv.')



# Python Nested Loop
# 2 use cases - Crossing data, Navigating hierarchy

'''Crossing Data'''
colors = ['Red', 'Blue', 'Pink']
sizes = ['L', 'M', 'S']

for color in colors:
    for size in sizes:
        print(f'{color} - Size {size}')


'''Navigating hierarchy'''      
Years = ['2026', '2027']
Months = ['Jan', 'Feb']
Days = range(1, 5)

for y in Years:
    for m in Months:
        for d in Days:
            print(f'Report_of_{y}_{m}_{d}.csv')


#SELECT COUNT(*) FROM CUSTOMERS WHERE ID IS NULL

tables = ['customers', 'orders', 'prices']
columns = ['id', 'create_date']

for t in tables:
    for c in columns:
        print(f'SELECT count(*) from {t} where {c} is NULL')



# Python While Loop
# Build a counter 1 to 5

i = 1
while i <= 5:
    print(i)
    i = i+1



'''Write a program that keeps asking - "do you agree?" until the user types "yes". '''

answer = ''

while answer != 'yes':
    answer = input('Do you agree? Yes/No: ')
print('Thank You!')


# while True loop

while True:
        answer = input('Do you agree? Yes/No: ')
        if answer == 'yes':
            break
print('Thank You!')


'''Task - 
i) 3 Attempts
ii) Yes within 3 attempts - Glad we're on the same page.
iii) Otherwise - 3 Strikes. You're out!  '''

attempts = 0
while attempts < 3:
        answer = input('Do you agree? Yes/No: ')
        if answer == 'yes':
            print("Glad we're on the same page")
            break
        attempts = attempts + 1
else:
    print("3 Strikes. You're out!")


