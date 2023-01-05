#list = used to store multiple items in a single variable

food = ["pizza","hamburger","hotdog","spaghetti","pudding"]

food[0] = "sushi"

food.append("ice cream")

food.remove("hotdog")

food.pop() #remove last element

food.insert(0,"cake")#add by numerical order

food.sort()

food.clear()#remove all element
#print(food[0])

for x in food:
    print(x)