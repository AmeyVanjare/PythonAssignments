import re
print("*"*10,"Q1","*"*10)
email=input("Enter emailid : ")
pattern=re.split("@",email)
print("First part of email is ",pattern[0])

print("*"*10,"Q2","*"*10)
sampleText='''007 is the best.ab is better than the rest.I am Ironman. '''
match=re.compile(r"^(\d|[a-zA-Z]{2})+\s")
lst=match.search(sampleText)
print(lst)

print("*"*10,"Q3","*"*10)
mobile=(input("Enter mobile number"))
match=re.compile(r"^\d{10}$")
extractedPattern=match.search(mobile)
print(extractedPattern)
if(extractedPattern!=None):
    print("Mobile number is valid")
else:
    print("Invalid mobile number")

