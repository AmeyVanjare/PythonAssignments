days=int(input("enter no of days in month : "))
startDay=int(input("Enter starting day no. monday-0 sunday-7 : "))
print("MON   TUE   WED  THI    FRI   SAT   SUN")
count=startDay
spaces= (7-startDay)*8
print(' '*spaces,end=" ")
for i in range(1,days+1):
    count=count+1
    print(i,end=" ")
    print(" "*2,end=" ")
    if count==7:
        count=0
        print()
        
        
