# nested loops = The "inner loop" will finish all of its iterations before
#                finishing one iteration of the "outer loops"

rows = int(input("How many rows?: "))
columns = int(input("How many column?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
   print()