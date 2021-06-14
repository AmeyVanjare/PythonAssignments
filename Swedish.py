print("Swedish Language")
str3=input("Enter string")
listVowels = ['a','e','i','o','u',' ']
myList=[]
for ch in str3.lower():
    if ch not in listVowels:
        myList.append(ch)
        myList.append('o')
        myList.append(ch)
    else:
        myList.append(ch)
            
                
print(''.join(myList))     
