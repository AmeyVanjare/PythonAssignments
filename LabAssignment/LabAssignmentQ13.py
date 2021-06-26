def correct(sen):
    sen=sen.replace("  "," ")
    sen=sen.replace(".",". ")
    return sen
if __name__=="__main__":
    sen=input("Enter a string")
    resSen=correct(sen)
    print("Correct string is ",resSen)