def outer_fn(val):
    value=val
    def inner_fn():
        print(value)
    return inner_fn
f1=outer_fn("hai")
f1()
