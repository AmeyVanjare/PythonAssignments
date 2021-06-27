def addCityTree(city,n):
    treeList=[]
    c=cityTreeDictionary.get(city,-1)
    for i in range(0,n):
        treeName=input("Enter tree name : ")
        treeList.append(treeName)
    if c==-1:
        cityTreeDictionary[city]=treeList
        return 0
    else:
        ch=input("Do you want to overwrite? Y/N") 
        if ch.upper=='Y':
            cityTreeDictionary[city]=treeList
            return 1
        else:
            return 2   

def displayCityTree():
    for k in cityTreeDictionary:
        print(k,cityTreeDictionary[k],sep="--->")           

def displayTreebyCity(city):
    c=cityTreeDictionary.get(city,-1)
    if c!=-1:
        for k in cityTreeDictionary:
            if k==city:
                result= cityTreeDictionary[k]
                break            
    else:
        result="City not found in dictionary"
    return result
        
def deleteCity(city):
    c=cityTreeDictionary.get(city,-1)
    if c!=-1 :
        ch=input("Do u want to delete? (Y/N) : ")
        if ch.upper()=='Y':
            cityTreeDictionary.pop(city)     
            return 0
        else:
            return 1
    else:
        return 2
        
def modifyTreebycity(city,ch):
    v=cityTreeDictionary.get(city,-1)
    if v!=-1:
        if ch==1:
            n=int(input("How many trees do u want to add? "))
            for i in range(0,n):
                treeName=input("Enter tree name : ")
                v.append(treeName)
                cityTreeDictionary[city]=v
                return 0
        elif ch==2:
            n=int(input("How many trees do u want to remove? "))
            for i in range(0,n):
                treeName=input("Enter tree name : ")
                v.remove(treeName)
                cityTreeDictionary[city]=v
                return 0
        else:
            return 1
    else:
        return 2

def getCitiesByTree(treeName):
    cityList=[]
    for k,v in cityTreeDictionary.items():
        if treeName in  v:
            cityList.append(k)
    return cityList

        
import sys    
choice=0
cityTreeDictionary={}
while choice!=7:
    print("1. Add new city and trees commonly found in the city.\n2. Display all cities and the list of trees for all cities.\n3. Display list of trees of a particular city.")
    print("4. Display cities which have the given tree.\n5. Delete city\n")
    print("6. Modify tree list.\n7.exit")
    choice=int(input("Enter coice from above option"))
    if choice==1:
        city=input("Enter city : ")
        n=int(input("Enter no. of trees"))
        result=addCityTree(city,n)
        if result==0:
            print("City and trees are added")
        elif result==1:
            print("City and trees are overwritten over existing one")    
        else:
            print("City and tree not inserted")

    elif choice==2:
        dictLen=len(cityTreeDictionary)
        if dictLen>=0:
            displayCityTree()
        else:
            print("Empty Dictionary")    

    elif choice==3:
        city=input("Enter city name for which trees are to be searched")
        result=displayTreebyCity(city)
        print(result)

    elif choice==4:
        treeName=input("Enter tree name for which cities are to be searched")
        res=getCitiesByTree(treeName)
        if len(res)>=0:
            print(res)
        else:
            print("No city for given tree")

    elif choice==5:
        city=input("Enter city name for which trees are to be searched")
        res=deleteCity(city)
        if res==0:
            print("City and associated trees are dleted from dictionary")
        elif res==1:
            print("Records not deleted")
        else:
            print("City does not present in dictionary")

    elif choice==6:
        city=input("Enter city name for which trees are to be modified")
        ch=int(input("Select an operation to be performed 1- Add tree 2.Remove tree"))
        res=modifyTreebycity(city,ch)
        if res==0:
            print("Operation completed successfully!!")
        elif res==1:
            print("Operation is not completed")
        else:
            print("Given city does not exist in list")

    elif choice==7:
        sys.exit()
    else:
        print("Wrong Input!!")
