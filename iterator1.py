from itertools import count
from itertools import cycle
from itertools import islice

counter = count(start=13)
type(counter)

print(next(counter))
print(next(counter))

colors = cycle(['red', 'white', 'blue'])
for _ in range(5):
    print(next(colors))

print("limited colors:")
limitedColors = islice(colors, 0, 5)
for x in limitedColors:
    print(x)




