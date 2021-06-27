if __name__=="__main__":
    mainlst=[[],[],[],[],[],[],[],[],[],[]]
    flag='Y'
    while flag.upper()=='Y':
        num=int(input("Enter a number"))
        rem=num%10
        mainlst[rem].append(num)
        flag=input("Do you want to continue entering data??")
    print("Elements of list are ",mainlst)