# Positional
def add(a,b):
    return a + b
print(add(3, 5))

#Default
def greet(name, msg ="Heyy, Master"):
    print(f"{msg},{name}")

greet("ManishSaama")
greet("Master","Villain")

#args / 
def total(*nums):
    return sum(nums)

def show(**info):
    for k,y in info.items():
        print(f"(k):(y)")

#keywords
def info(name, age, city):
    print(f"{name},{age},{city}")

info(age= 24, city = "KTM", name= "ManishSama")