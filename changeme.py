def changeme(a):
    a.extend(['x', 'y'])


a = ['a', 'b']
changeme(a)

print(a)


def printinfo(name='sam', age=11):
    print('name:', name)
    print('age:', age)


printinfo()
printinfo(age=12)
printinfo('jie', 'yan')


def printextra(arg1, *args):
    print('arg1=', arg1)
    for var in args:
        print(var)


printextra(10)
printextra(11, [1, 2, 3])
