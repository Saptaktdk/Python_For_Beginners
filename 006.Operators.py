# Arithmetic Operators
x = 6
y = 4

ans = x + y #Addition Operator
print(ans)

ans = x - y #Subtraction Operator
print(ans)

ans = x*y #Modulus Operator
print(ans)

ans = y/x #Division Operator
print(ans)

ans  = y%x #Modulus Operator
print(ans)

ans = x**y #Exponential Operator
print(ans)

#Comparison Operators
ans = x < y
print(ans)

ans = (x != y)
print(ans)

ans = (x >= y)
print(ans)

ans = (x <= y)
print(ans)

#Assignment Operators
c = 0
d = 1

c += d # c=c+d
print(c)

c -= d # c=c-d
print(c)

#Logical Operators
a = 4
b = 5

x = 1
y = 2

out = (a < b) or (x > y)
print(out)

out = (a > b) and (x < y)
print(out)

out = not( x < y)
print(out)

#Membership Operator
tuple = ("Espada","Arrancar", 45, 2, 900)

ans = "Espada" in tuple
print(ans)

ans = "Grimmjow" not in tuple

#Identity Operators
a = 6
b = 8

res = a is b
print(res)

res = a is not b
print(res)
