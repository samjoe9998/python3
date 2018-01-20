sum = lambda x, y: x + y

print(sum(1, 2))
print(sum(2, 3))

numbers = list(range(10))
print(numbers)

numbers3 = filter(lambda x: x > 5, numbers)
print(list(numbers3))


class Person:
    def __init__(self, name, age, ssn):
        self.name = name
        self.age = age
        self.ssn = ssn

    #    def __str__(self):
    #        return self.name + ',' + self.age + ',' + self.ssn

    def __repr__(self):
        return self.name + ',' + str(self.age) + ',' + self.ssn


class House:
    def __init__(self, area, year, address, people):
        self.area = area
        self.year = year
        self.address = address
        self.people = people

    def expand(self, extra_area):
        self.area += extra_area

    def print(self):
        print(self.address, "-", self.area, "-", self.people)

    def add_people(self, a_people):
        self.people.append(a_people)


p1 = Person('yan jie', 40, '123-45-6789')
p2 = Person('sam zhou', 50, '98-7654-32')

people1 = [p1, p2]
h1 = House(1200, 1998, "915 keaton drive", people1)
h1.print()
h1.expand(300)
h1.print()

p3 = Person('jeffrey zhou', 18, '23-2323-23')
h1.add_people(p3)
h1.print()

print('p1=', p1)
