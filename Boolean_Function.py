#Values
print(True)
print(False)
print(type(True))

#Functions

print(bool(123))
print(bool('Hi'))
print(bool())
print(bool(''))
print(bool(0))
print(bool(None))

#any(), all() functions
email = ''
phone = '01671232'
username = 'abc223'

#Allows registration if any field is filled.
print(any([email, phone, username]))  

#Allows registration if all fields are filled.
print(all([email, phone, username]))
  
print(isinstance(True, str))
print("Hello".startswith("H"))
print("Hello".endswith("o"))

#Operator

print(6 < 7 < 9)

age = 35
print(18 < age < 30)

print('A' != 'a')


#Checks if the system is under pressure
cpu_use = 70
memory_use = 95
print(cpu_use > 90 or memory_use > 90)
print(cpu_use < 90 and memory_use > 90)

print(not 3 > 2)
print(not not False)

#Allow access only if the user is logged in
#or they are guest
#but they must not be banned

is_logged = True
is_guest = False
is_banned = False

print(is_logged or is_guest and not is_banned) #in such case, and operator executes first, then or operator executes
 #                  -------- false -----------
#     ---------true----------------------------

#Membership (in) operator
print('p' in 'python')  #True
print('f' not in 'python')  #True

#is operator

#--in case of list
x = ['a', 'b', 'c']
y = ['a', 'b', 'c']
print(x == y)   #True - compares the values
print(x is y)   #False - compares object/id

#--in case of a single value
x = 50
y = 50
print(x == y)   #True - compares the values
print(x is y)   #True - compares object/id --both x and y having same object


#Make sure the email exists and it is not empty
email = 'emailaddress@google.com'
print(email != '')

email = None
print(email is not None or email != '')     #best practice : using is operator with None


