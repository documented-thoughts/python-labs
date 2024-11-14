x = 1
y = 2
result = x + y

print(result) # = 3
result = type(result)
print(result) # <class 'int'>

x = '1'
y = '2'

result = x + y

print(result) # 12
result = type(result)
print(result) # <class 'str'>

x, y, z = 1, 2.0, "3.20"

print(type(x), type(y), type(z)) # <class 'int'> <class 'float'> <class 'str'>

breakfast = "omlet"
dinner = "turkey sandwich"

print(breakfast, dinner, sep=", ") # omlet, turkey sandwich

phrase = 'He said, "You are one of a kind."' 
print(phrase) # He said, "You are one of a kind."

phrase = 'He said, \"You are one of a kind.\"'
print(phrase) # He said, "You are one of a kind."

x = "apple"
y = "apple"

print(id(x))  # 2516685353968
print(id(y))  # 2516685353968
print(x == y) # True

phrase = "one"
print(phrase + ", two, three") # one, two, three
print("{}, two, three".format(phrase)) # one, two, three
print(f"{phrase}, two, three") # one, two, three

drink = "espresso"
print(drink[0]) # e
print(drink[1]) # s
print(drink[2]) # p
print(drink[3]) # r
print(drink[4]) # e
print(drink[5]) # s
print(drink[6]) # s
print(drink[7]) # 0
# print(drink[8]) IndexError: string index out of range 