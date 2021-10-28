import sh

c1 = sh.Circle()
c2 = sh.Circle(5, 15, 20)
print(c1)
print(c2)
print(c2.area())
c2.move(5, 6)
print(c2)
