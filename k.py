thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020,
    "colors": ["red","green","yellow"]

}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))

dict = dict(name = "amir", age = 18,country = "Kazakhstan")
print(dict)

x = thisdict["model"] #x = thisdict.get("model")
y = thisdict.keys()
print(y)
print(x)

thisdict["color"] = "white"
print(y)

z = thisdict.values()
print(z)

if "model" in thisdict:
    print("Yes") 

thisdict["year"] = 2019 # or thisdict.update({"year": 2020})

thisdict.pop("model")
thisdict.popitem()
print(thisdict)
del thisdict["colors"]
print(thisdict)
#del thisdict 
thisdict.clear()
print(thisdict)