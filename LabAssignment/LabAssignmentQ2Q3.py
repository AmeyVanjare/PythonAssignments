listInput = []
n=int(input("Enter histogram no.of inputs"))
for i in range(0,n):
    element=int(input())
    listInput.append(element)
print(listInput)

def histogram(listInput):
    for i in range(0,n):
        print("*"*listInput[i])

histogram(listInput)

print("PALINDROME CHECK")
str1 = input("Enter a string")
str1modified = ''.join(e for e in str1 if e.isalnum())
str2=str1modified[::-1]
print(str2)
if str1modified==str2:
    print("IT IS PALINDROME")
else:
    print("not a palindrome")

print("Swedish Language")
str3=input("Enter string")
listVowels = ['a','e','i','o','u']
for ch in str3:
    if ch not in listVowels:
        modString=''.join(ch).join(ch)
    else:
        modstring=''.join(ch)
print(modstring)        

        
              
