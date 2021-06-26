people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Baman':'Red','Jenny':'Pink'}
print('Number of students in dictionary is: ',len(people))
for k,v in people.items():
    if k.upper()=='LISA':
        people[k]=input("Enter lisa's new favourite colour : ")
        break

for k,v in people.items():
    if k.upper()=='JENNY':
        people.pop(k)
        break
print("Sorted dictionary elements by name: ")
for i in sorted(people.keys()):
    print(i,people[i],sep="-->")

print("New People : ",people)