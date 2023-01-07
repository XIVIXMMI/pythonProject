# *agrs = parameter that will pack all arguments into a tuples
#         useful so that a function can accept a varying amount of arguments

def add(*agrs):
    sum = 0
    agrs = list(agrs)
    agrs[0] = 0
    for i in agrs:
        sum += i
    return sum

print(add(1,2,3,4,5,6))