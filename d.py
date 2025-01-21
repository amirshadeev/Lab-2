list = ["apple","Banana","cherry","kiwi","mango"]
newlist = []
for x in list:
    if "a" in x:
        newlist.append(x)

print(newlist)

newlistwo = [x for x in list if "a" in x]
print(newlistwo)

newlistso = [x for x in list if x != "apple"]
print(newlistso)

newlisty = [x for x in list]
print(newlisty)

sami = [x for x in range(10) if x < 5]
print(sami)

ad = [x if x != "apple" else "orange" for x in list]
print(ad)

list.sort()
print(list)

gam = [99, 31, 2, 9, 41, 16]
gam.sort()
print(gam)
gam.sort(reverse = True)
print(gam)

def myfunc(n):
    return abs(n - 50)
gam.sort(key = myfunc)
print(gam)

list.sort(key = str.lower)
print(list)

dalist = list.copy()  #dalist = list(list) toje samoe
print(dalist)