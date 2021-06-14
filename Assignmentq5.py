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
