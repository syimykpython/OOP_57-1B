from homeworks.distance import Distance

d1 = Distance(150, 'm')
d2 = Distance(4, 'km')
d3 = Distance(231, 'cm')
d4 = Distance(324, 'km')
d5 = Distance(4000, 'm')

print(d1 + d2)
print(d5 + d1)
print(d1 - d3)
print(d1 + d4)
print(d5 < d4)
print(d4 > d2)
print(d3 == d4)