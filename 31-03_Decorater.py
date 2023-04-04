#Using Decoration Function
def decor_function(input_function):
    def inner():
        print("#"*10)
        print("Decoration with flowers")
        input_function()
        print("#"*10)
    return inner
#@decore_function
def old_function():
    print("No decoration")
old_function()



