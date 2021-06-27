def addElement(lst,ch,dataOption):
    flag='Y'
    while flag.upper()=='Y':
        if dataOption==1:
            ele=int(input("Enter a number"))
        else:
            ele=input("Enter a string")

        if ch==1:
            lst.append(ele)
        else:
            pos=int(input("Select a position to add element in list"))
            lst.insert(pos,ele)
        flag=input("Do u want to insert more data? (Y/N)")
    return lst

def deleteByValue(lst,val):
    if val in lst:
        lst.remove(val)
        return 1
    else:
        return 2
 
def deleteByPosition(lst,ch):
    if ch==1:
        lst.pop()
        return 1
    else:
        pos=int(input("Enter position for removing element."))
        if pos<len(lst):
            lst.pop(pos)
            return 1
        else:
            return 2



import sys
if __name__=="__main__":
    lst=[]
    lst1=[]
    lst2=[]
    choice=0
    print("Menu")
    print("1.Accept Data 2.Delete data by value 3.Delete data by position")
    print("4.Sort 5.Reverse 6.Print sorted list witout changing original list")
    print("7.Print list in reverse order without changing original list")
    print("8.Display data 9.Exit")
    while choice!=9:
        choice=int(input("Select an option from above menu"))
        if choice==1:
            ch=int(input("Where do u want to add element?\n 1.At last position 2. At given position"))
            dataOption=int(input("Select one data type and stick to it throuhout the operation!! 1. Numeric 2. String"))
            lst=addElement(lst,ch,dataOption)

        elif choice==2:
            dtaOption=int(input("What type of element do u want to remmove? 1.Numeric 2.String"))
            if dataOption==1:
                val=int(input("Enter value to be removed from list. Be aware of case sensitivity!!"))
            else:
                val=input("Enter value to be removed from list. Be aware of case sensitivity!!")
            res=deleteByValue(lst,val)
            if res==1:
                print("Given element is removed from list")
            else:
                print("Element does not exist in list")

        elif choice==3:
            ch=int(input("From where do u want to remove element?\n 1.At last position 2. At given position"))
            res=deleteByPosition(lst,ch)
            if res==1:
                print("Given element is removed from list")
            else:
                print("Element does not exist in list. U have entered invalid index")
        elif choice==4:
            ch=int(input("Select sorting order\n 1.Ascending 2. Descending"))
            if ch==1:
                lst1=sorted(lst)
            else:
                lst1=sorted(lst,reverse=True)

        elif choice==5:
            lst2=lst[::-1]

        elif choice==6:
            print("Sorted list is ",lst1)

        elif choice==7:
            print("Reversed list is", lst2)

        elif choice==8:
            ch=int(input("Select display option\n 1.Normal 2.Numbered"))
            if ch==1:
                print("List in normal form is ",lst)
            else:
                enumeratedList=enumerate(lst)
                print(list(enumeratedList))

        elif choice==9:
            print("Exiting the appplication")
            sys.exit(0)
            
        else:
            print("Wrong input entered.....Please select option from 1 to 9")

            
        
