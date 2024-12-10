username=input("enter the username:") 
if username.isalnum()and 6<=len(username)<=15:
    print("valid username")
else:
    print("invlid username.Only alphbet and numbers, 6-10 characters long")