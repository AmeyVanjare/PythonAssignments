ceaserDictionary= {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w',
'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
'G':'T',
'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
key_list=list(ceaserDictionary.keys())
val_list= list(ceaserDictionary.values())


def decodeMessage(encodedMessage):
    decodedString=''
    for i in myString:
        if i in ceaserDictionary:
            decodedString=decodedString+ceaserDictionary[i]
        else:
            decodedString=decodedString+i
    return decodedString     

def encodeMessage(plainText):
    encodedString=''
    for i in plainText:
        if i in val_list:
            pos=val_list.index(i)
            encodedString= encodedString+ key_list[pos]
        else:
            encodedString= encodedString + i
    return encodedString

if __name__=="__main__":
    myString = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
    testString="Caesar cipher? I much prefer Caesar salad!"
    print("decoded string is :" ,decodeMessage(myString))
    print("Encoded message is : ",encodeMessage(testString))
