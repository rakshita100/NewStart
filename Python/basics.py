# ---------------print function
print("Hello World!!")

# -------------numbers
myint = 7
print(myint)
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

# -----------strings
mystring = "hello"
print(mystring)
one = 1
two = 2
three = one + two
print(three)
hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)
# more than one assignments
a, b = 3, 4
print(a,b)

#lists
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])

for x in mylist:
    print(x)

# Arithmetic operators
number = 1 + 2 * 3 / 4.0
print(number)
remainder = 11 % 3
print(remainder)
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)
print([1,2,3] * 3)

# string formatting
name = "John"
print("Hello, %s!" % name)

str = "Hello World!"
print(str)
print(len(str))
print(str.index("o"))
print(str.count("l"))
print(str.upper())
print(str.lower())
print(str.startswith("Hello"))
print(str.endswith("abc"))
str1 = str.split(" ")
print(str1)

# Conditions
x=2
print(x==2)
print(x==3)
print(x<3)

# boolean
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

x=[1,2,3]
y=[1,2,3]
z=x
print(x==y)
print(x is y)
print(x is z)

print(not False)

# loops
nos = [1,2,3,4]
for n in nos:
    print(n)

for x in range(5):
    print(x)
for x in range(3,8,2):
    print(x)

# while loop
count =0
while count<5:
    print(count)
    count+=1

# break and continue
count=0
while True:
    print(count)
    count+=1
    if count>=5:
        break

for x in range(10):
    if x%2 == 0:
        continue
    print(x)

# ------------functions
def my_func():
    print("Hello!!")
my_func()

def my_fun(name,greeting):
    print("Hello %s , %s" %(name,greeting))
my_fun("John","GoodLuck!!")

def sumF(a,b):
    return a+b
print(sumF(2,3))

#-------------Classes and objects
class myclass:
    var="blah"
    def fn(self):
        pass
myobj=myclass()
print(myobj.var)

# -------------dictionaries
ph_bk={}
ph_bk["John"]=9743566602
ph_bk["Ravi"]=8050501456
print(ph_bk)
for name,no in ph_bk.items():
    print("Phone numbe of %s is %d" %(name,no))
 # remove a pair from dictionary
del ph_bk["Ravi"]
print(ph_bk)

