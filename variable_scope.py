# scope = the region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created


name = "Nguyen" # global scope (available inside and outside functions)
def display_name():
    name = "Nguyen"  # local scope (available only inside this function)
    print(name)

display_name()
print(name)
