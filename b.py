list = ["abc", 15, True, "damir", 53, "amir"]
print(list)
print(type(list))
print(list[0:2])
print(list[2:])
if "amir" in list:
    print("Yes")

list[1:3] = ["123"]
print(list)
list.insert(2,"water")
print(list)

list.append("Orange")
print(list)

listwo = ["Mango",124,"samira"]
list.extend(listwo)
print(list)

list.remove("damir")
print(list)

list.pop(1)
print(list)

list.pop()
print(list)

del list[0]
print(list)

list.clear()
print(list)