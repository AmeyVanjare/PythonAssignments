def overlapping(lst1,lst2):
    lstn=[]
    lstn=list(set(lst1) & set(lst2))
    if len(lstn)>0:
        return True
    else:
        return False
    

def main():
    lst1=[1,4,5]
    lst2=[2,4,7]
    if overlapping(lst1,lst2):
        print("Atleast one element present in list")
    else:
        print("No common element in list")

main()        