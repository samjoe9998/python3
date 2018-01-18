import dis

x = [1,2,3]
y = iter(x)
z = iter(y)

print(next(y))
print(next(y))
print(next(z))

print(type(x))
print(type(y))
print(type(z))

for e in x:
    print(e)

dis.dis('for _ in x: pass')


