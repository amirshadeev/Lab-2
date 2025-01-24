myset = {"apple","banana","cherry","apple",True,1,0,False}
print(myset)
print(len(myset))
for x in myset:
    print(x)

if "banana" in myset:
    print("yes")

print("banana" in myset)

myset.add("orange")
tropical = {"papaya","mango"}
myset.update(tropical)
myset.remove("banana")
myset.discard(True)
myset.clear()
print(myset)
del myset
print(myset)