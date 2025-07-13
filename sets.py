

a=set() # empty set
b={2,5,1,6,'nn',6.0}
c={9,3,7,1}
print(b)
print(len(b))
b.remove(2)
print(b)
b.add(7)
print(b)
print(b.union(c))
print(b.intersection(c))