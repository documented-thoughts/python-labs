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

# page 74