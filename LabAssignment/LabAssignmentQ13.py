import re
def correct(sen):
    sen=re.sub(r"\s+",' ',sen)
    sen=sen.replace(".",". ")
    return sen
if __name__=="__main__":
    sen=input("Enter a string")
    resSen=correct(sen)
    print("Correct string is ",resSen)
