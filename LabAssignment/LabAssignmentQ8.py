print("*"*10,"Q8","*"*10)
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def main():
    print("Factorial of 1 to 20 is ")
    for n in range(1,21):
        print("%d  %d " % (n,factorial(n)))

main()
     