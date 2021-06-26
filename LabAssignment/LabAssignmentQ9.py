print("*"*10,"Q9","*"*10)   
def sumLab(n):
    sum=0
    if n==1:
        return 1
    else:
        sum=sumLab(n-1)+n
    return sum

def main():
    print("Calculating sumof first 10 numbers ")    
    sum=sumLab(n=10)        
    print("Sum is : ",sum)

main()