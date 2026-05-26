x =100  #GLOBAL - viosible everuwhere
def show_scope():
    y = 200   #LOCAL = only inside this function
    print(f"Inside : x={x}, y={y}")  #can see global

def modify_global():
    global x   #declare intent to modify global
    x = 999
    print(f"Modified x to {x}")

show_scope()
modify_global()
print(f"Outside : x={x}")  # x changed globally

#what about y
# print(y) -> NameError: y not defined outside