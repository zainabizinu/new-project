
txt=("hello world from python")[::-1]
print(txt)


def my_function(x):
    return list(dict.fromkeys(x))
mylist=my_function(["hello","world","world","from","from","python"])
print(mylist)
                   

str=input("enter srting")
#input(str)
l=list(str)
#print(l)
freq=[l.count (ele) for ele in l]
#print(freq)
d=dict(zip(l ,freq ))
print(d)




