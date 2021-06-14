print("panagram check")
#The quick brown fox, jumps over the lazy dog!!!!.
str1=input("Enter String")
s=set()
for i in str1:
    if i.isalpha():
        s.update(i.lower())

if len(s)==26:
    print("String is panagram")
else:
    print("String is not panagram")
print(s)
print(len(s))
        
