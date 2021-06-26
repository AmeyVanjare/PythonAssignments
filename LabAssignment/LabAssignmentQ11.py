def find_longest_word(lst):
    max=""
    for i in lst:
        if len(i)>len(max):
            max=i
    return max

if __name__=="__main__":
    lst=["Alpha","Beta","gamma","delta","Alexander"] 
    res=find_longest_word(lst)
    print("Lonest word is ",res)       
