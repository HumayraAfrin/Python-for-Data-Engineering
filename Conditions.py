#if - elif - else/ nested if

score = 95
submitted_project = True

if score >= 90:
    if submitted_project:
        print('A+')
    else:
        print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print ('F')



# Logical operators with conditions

score = 78
submitted_project = False

if score >= 90 and submitted_project:
    print('A+')
elif score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70 or submitted_project:
    print('C')
else:
    print ('F')



# Independant If condition

score = 88
submitted_project = True

if score >= 48:
    print('Pass')
else:
    print('Fail')

if submitted_project:
    print('Project submitted.')
else:
    print('Project not submitted.')



#Challenges

# 1) Email must not be empty
# 2) Email must contain a '.' and a '@'
# 3) Email must contain extactly one '@' symbol
# 4) Email must end with '.com', '.org' or '.net'
# 5) Email must not be longer than 254 characters
# 6) Email must start and end with a letter or digit

#email = '  '            #Email is valid.
email = '_huma@gmail.com'
#Clean the string - use strip()
email = email.strip()   #Email is empty.

if email == '':
    print('Email is empty.')
elif not ('.' in email and '@' in email):   #using in operator
    print('Email must contain . and @')
elif email.count('@') != 1:
    print('Email must contain extactly one '@' symbol')
elif not email.endswith(('.com', '.org', '.net')):
    print('Email must end with .com, .org or .net')
elif len(email) > 254:
    print('Email must not be longer than 254 characters')
elif not (email[0].isalnum() and email[-1].isalnum()):      #isalnum() checks if the string contains only letters or digit
    print('Email must start and end with a letter or digit')
else:
    print('Email is valid.')




# Python If-Else in One Line + Match-Case

score = 100

if score >= 90:     #Classical if
    print('A')
else:
    print('F')


# this can be done in another way like below:

print('A' if score>= 90 else 'F')       #Inline if

# Or

grade = 'A' if score>= 90 else 'F'      #Inline if
print(grade)


'''Simple logic = Inline if; Complex logic = Classical if'''


score = 85

if score >= 90:     #Classical if
    print('A')
elif score >= 80:
    print('B')
else:
    print('F')

#Or 
grade = 'A' if score>= 90 else 'B' if score >= 80 else 'F'      #Inline if
print(grade)

#Or
grade = (                   #Inline if
    'A' if score>= 90 
    else 'B' if score >= 80 
    else 'F' )     
print(grade)



# Case Match
'''Task: Convert the full country names into 2 letters abbreviations'''

Country = 'Egypt'

match Country:
    case 'United States' | 'USA':
        print('US')
    case 'Egypt':
        print('EG')
    case 'Bangladesh':
        print('BD')
    case 'Germany':
        print('DE')
    case _:
        print('Unknown Country')


