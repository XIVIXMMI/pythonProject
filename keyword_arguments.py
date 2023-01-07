# keyword_arguments = argument preceded by an identifier when we pass them to a function
#                      The order of the argument doesn't matter, unlike positional arguments
#                      Python knows the names of arguments that our function receives

def hello(first, middle, last):
    print("Hello "+first+" "+middle+" "+last)

hello(first="Nguyen",middle="Khoi",last="Le")