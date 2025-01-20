print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 2
b = 1
if a < b:
    print("b is greater then a")
else :
    print("b is not greater then a")

print(bool("Hello"))
print(bool(15))

x = "hello"
y = 15
print(bool(x))
print(bool(y))


bool(False)
bool([])
bool(())
bool({})
bool(0)
bool(None)
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))