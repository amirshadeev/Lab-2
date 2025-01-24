set1 = {"apple","banana"}
set2 = {"cherry"}
set3 = set1.union(set2) #toje samoe set3 = set1 | set2
#можно ещё несколько сразу set1.union(set2, set3, set4)
#myset = set1 | set2 | set3
print(set3)

x = {"a","b"} #set
y = (1,2,3) #tuple
z = x.union(y)
print(z)

list = [1,2,3]
try:
    list[0] = 10
    print(True)
except TypeError:
    print(False)