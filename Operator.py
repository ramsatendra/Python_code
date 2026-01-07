# Arithmetic operators
x = 2
y = 4

total = x + y
print(total)

total = x - y
print(total)

# comparison operators
x = 4
y = 5

out = x < y
print(out)

out = (x == y)
print(out)

out = (x != y)
print(out)

out = (x <= y)
print(out)

# Assignment operators
c = 0
d = 1

c += d # C = c+d its an increment operator
print(c)

c -=d # C = c-d its a decrement operator


#Logical operators And and or

a = 40
b = 60

x = 2
y = 3

out = (a < b) or (x > y) # only will check the true value
print(out)

out = (a > b) and (x > y)
print(out)

# membership operators

first_tuple = ("IOT", "Devops", 47, "num1", 1.5)
ans = "Devops" in first_tuple
print(ans)

first_tuple = ("IOT", "Devops", 47, "num1", 1.5)
ans = "Devops" not in first_tuple
print(ans)

# identity operator

a = 12
b = 15

result = a is b
print(result)

