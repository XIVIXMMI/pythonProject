# if statements = a block of code that will execute if it's condition is true

age = int(input("How old are you ? : "))

if age == 100:
    print("you are a century old!")
elif age >= 18:
    print("you are an adult!")
elif age < 0:
    print("you haven't been born yet bro!")
else:
    print("you just a child!")