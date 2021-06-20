import re
print("*"*10,"Q4","*"*10)
def validateCredentials(username,passwd):
    match=re.compile(r"^[a-zA-Z0-9]+")
    validatedUser=match.search(username)
    match=re.compile(r"^(?=.*[a-zA-Z0-9])(?=.*[@$])[a-zA-z0-9@$]{8}$")
    validatedPass=match.search(passwd)
    print("validatedPass ",validatedPass)
    if(validatedUser!=None and validatedPass!=None):
        return True
    else:
        return False


count=0
while count<3:
    username=input("Enter usename ")
    passwd=input("Enter password ")
    if(validateCredentials(username,passwd)):
        print("Welcome to application")
        break
    else:
        print("Invalid credentials")
        count=count+1
        print(count)
