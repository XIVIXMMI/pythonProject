# str.format()
# = optional method that gives users more control when displaying output

#animal = "cow"
#item = "moon"

#print("The "+animal+" jumped over the "+item)
#print("The {} jumped over the {}".format(animal,item))
#print("The {1} jumped over the {0}".format(animal,item)) #positional argument
#print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) # keyword argument

#text = "The {} jumped over the {}"
#print(text.format(animal, item))

#name = "Nguyen"

#print("Hello, my name is {}".format(name))
#print("Hello, my name is {:10}. Nice to meet you".format(name))
#print("Hello, my name is {:<10}. Nice to meet you".format(name))
#print("Hello, my name is {:>10}. Nice to meet you".format(name))
#print("Hello, my name is {:^10}. Nice to meet you".format(name))


#number = 3.14159
number = 1000

print("The number is {:.2f}".format(number))
print("The number is {:,}".format(number))
print("The number binary is {:b}".format(number))
print("The number octal is {:o}".format(number))
print("The number hexadecimal is {:x}".format(number))
print("The number is {:e}".format(number))
