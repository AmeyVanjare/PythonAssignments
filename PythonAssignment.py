print("1.Display character from even position \n 2.Display character from odd position \n 3.Display length of string \n 4.Add a at the end of the string length times \n5.Exit")
str1=input("Enter String : ")
flag=True
choice=0
while flag:
    choice = int(input("Enter choice from above menu : "))
    if choice==1:
        print(str1[0::2])
    elif choice==2:
        print(str1[1::2])
    elif choice==3:
        print(len(str1))
    elif choice==4:
        str2=str1+("a"*len(str1))
        print(str2)
    elif choice==5:
        print("Exiting")
        flag=False
    else:
        print("Wrong choice")

print("*"*10,"Q2","*"*10)
str3=input("Enter string : ")
word=input("Enter word to be searched : ")
pos=str3.find(word)
print(word,"-",pos)
while pos!=-1:
    pos=str3.find(word,pos+1)
    if pos != -1:
        print(word,"-",pos)

print("*"*10,"Q4","*"*10)
listCity=[]
listLocation=[]
n=int(input("how many cities u want to enter"))
for i in range(0,n):
    city=input("Enter city")
    listCity.append(city)
    location=input("Enter location")
    listLocation.append(location)

for x,y in zip(listCity,listLocation):
    print("city",x,"Location",y)

    
print("*"*10,"Q5","*"*10)
num=int(input("Enter length of list : "))
lst1=[]
lst2=[]
for i in range(0,num):
    ele=input("Enter list elements")
    lst1.append(ele)
    
for j in range(0,len(lst1)+1):
    lst2.append(-1)
    
for position,data in enumerate(lst1):
    lst2.insert(int(data),position)

print(lst2)    
  
    
    
    
    

    

    
