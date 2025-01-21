#tuple
thistuple = ("apple","banana", "cherry","apple")
print(thistuple)
print(len(thistuple))
#нельзя add and удалять элементы
tuple = ("apple",)
print(type(tuple))
print(thistuple[-1])

if "apple" in thistuple:
    print("Yes")

#вот так можно изменить
x = ("apple","banana","cherry")
y = list(x)
y.append("orange")
#x = tuple(y)
#не знаю почему но неработает,на сайте это способ как изменит тупл

z = ("orange",)
x += z
print(x)

#полностью удалить del thistuple
fruits = ("apple", "banana", "cherry", "fama")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

