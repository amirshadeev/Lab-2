thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

for i in range(len(thistuple)):
  print(thistuple[i])

i = 0
while i < len(thistuple):
   print(thistuple[i])
   i += 1

tuple1 = ("a", "b", "c")
tuple2 = (1,2,3)
tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple","banana","cherry")
mytuple = fruits * 3
print(mytuple)