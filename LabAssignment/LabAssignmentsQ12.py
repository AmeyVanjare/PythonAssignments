def find_longest_word(lst,limit):
    resLst=[]
    for i in lst:
        if len(i)>limit:
            resLst.append(i)
    return resLst

if __name__=="__main__":
    lst=[]
    n=int(input("How many words do u want to add in list?"))
    for i in range(n):
        ele= input("Enter elements in list : ") 
        lst.append(ele)
    limit=int(input("Enter length for which words are to be filtered : "))
    res=find_longest_word(lst,limit)
    if(len(res)>0):
        print("No. of words having length greater than ",limit,"is ",res)
    else:
        print("No word found for given length")
     
