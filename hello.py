
print('Hi! This is my first python code.')

print('Your Learning Path:\n\t- Python Basics\n\t- Data Engineering\n\t- AI')


#OR use ''' for new line

print('''Your Learning Path:
\t- Python Basics
\t- Data Engineering
\t- AI''')

name = input('What is your name?')
city = 'Dhaka'
print(name, 'comes from', city)


i= 'Hello'
j='1234'
k=None  #None is a None datatype
l = ''  # string datatype with blank value

text = 'hi'
number = 10

print(type(text))
print(type(number))

print(len(text))
print(len(number))   # Len() function can’t be use in int/float datatype.

# Python String Functions

#types
name = 'Humayra'
print(type(name))

age = 14
print(type(age))

print("Your age is: " + str(age))

#Math
Password = '1234ab'
print(len(Password))

if len(Password) < 8:
    print('The Password is too small!')

text = """
Python is easy to learn.
Python is powerful.
Many people love python.
"""

print(text.count('Python')) #Python is case sensitive
print(text.count('python'))


##Transformations
#replace
phone = '+49 (176) 123-4567'
print(phone.replace('+','00').replace('(','').replace(')','').replace('-', '').replace(' ',''))

# +
folder = 'C:/hp/humayra/'
file = 'Report.csv'
full_file_path = folder + file
print(full_file_path)

# f-String
name = 'Sam'
age = 24
is_student = False
print('My name is ' + name + ', I am ' + str(age) + ' years old and student status is ' + str(is_student) + '.')
print(f'My name is {name}, I am {age} years old and student status is {is_student}.')

print(f'2 + 3 = {2 + 3}')

print(f'{{This is me.}}')


# split
csv_file = '1234,Max,USA,1970-10-05,M'
print(csv_file.split(','))

#repetation (*) times
print('ha'*3)
print('='*30)

#Data Extraction - Indexing & Slicing
word = 'Python'
print(word[0])
print(word[1])

datetime = '2025-06-11'
print(datetime[0:4])
print(datetime[6:])
print(datetime[-2:])

#Data Cleansing - Remove spaces
txt = ' Engineering'.lstrip()
print(txt)

txt = 'Engineering '.rstrip()
print(txt)

txt = ' Engineering '.strip()
print(txt)

txt = 'Data Engineering'.strip() #it doesn't remove white space from in between the words
print(txt)

txt = '####ABC#####'.strip('#')
print(txt)

#Detect extra spaces - Check the lenght before and after strip() to find unwanted space
txt = '  Engineering'
print(len(txt))
print(len(txt.strip()))

num_of_spaces = len(txt) - len(txt.strip())
is_clean = len(txt) == len(txt.strip())

print('No of Spaces: ', num_of_spaces)
print('Is my data clean? ', is_clean)


#Case Conversion
search = 'Email'
data = 'email'

print(search == data)
print(search.lower() == data.lower())


#Searching Technique
phn = '+48-349-1234'
print(phn.startswith('+49'))

email = 'Humayra@outlook.com'
print(email.endswith('.com'))

print('@' in email)

phn1 = '+48-345-1234'
phn2 = '0049-456-3456'

print(phn1[4:])
print(phn1[phn1.find('-')+1:])

print(phn2[5:])
print(phn2[phn2.find('-')+1:])


#String Function - Validation
country = 'USA'
print(country.isalpha())

phn = '79889809.8908'
print(phn.isnumeric())
