def make_ing_form(verb):
    vowels_list=['a','e','i','o','u']
    last_char=verb[-1]
    second_last_char=verb[-2]
    if second_last_char=='i' and last_char=='e':
        verb=verb[0:-2]+"ying"
    elif last_char.lower()=="e":
        verb=verb[0:-1]+"ing"
    elif second_last_char in vowels_list and last_char not in vowels_list:    
        verb=verb+last_char+"ing"    
    else:    
        verb=verb+"ing"
    return verb

if __name__=="__main__":
    choice=input("Do u want to find out ing form of verb? (Y/N) : ")
    while choice.upper()=="Y":
        verb=input("Enter a verb : ")
        newVerb = make_ing_form(verb)
        print("ing for of ",verb,"is ",newVerb)
        choice=input("Do u want to find out ing form of verb? (Y/N) : ")