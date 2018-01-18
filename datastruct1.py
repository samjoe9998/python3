squares = list()

for x in range(10):
    squares.append(x ** 2)

print(squares)

squares2 = list(map(lambda x: x ** 2, range(10)))
print(squares2)
squares3 = [x ** 2 for x in range(10)]
print(squares3)

for _ in range(10):
    print('hello')

listComp = [(x, y) for x in range(3) for y in range(2) if x != y]
print(listComp)

vec = [list(range(1,4,1)), list(range(4,7,1)), list(range(7,10,1))]
print(vec)

flat = [num for elem in vec for num in elem]
print(flat)

