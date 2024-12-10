y=10
def outer():
    z=4
    def inner():
        x=4
        print("x:",x)
        print("inside the function y:",y)
    inner()
    print("z:",z)   
outer() 