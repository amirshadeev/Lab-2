thisdict = {
    "brand":"mustang",
    "year": 2020
}
for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

for x in thisdict.keys():
    print(x)

for x,y in thisdict.items():
    print(x,y)

mydict = thisdict.copy()
print(mydict)

#3x dict
my_family = {
    "me": {
        "name":"amir"
    },
    "litbro": {
        "name":"sardar"
    },
    "mom": {
        "name":"nurbi"
    }
}
print(my_family)
print(my_family["me"]["name"])
for x, obj in my_family.items():
    print(x)

for y in obj:
    print(y + ':', obj[y])