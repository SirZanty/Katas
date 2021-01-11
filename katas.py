def pig_it(text):  # 6/1/2021
    return ' '.join([i + 'ay' if i.isalpha() else i for i in [x[1:] + x[0] for x in text.split()]])

#print(validBraces("[()]{{()}}"))   analisis de por patron
def validBraces(string):
    parenthesis = []
    pardict = {"{":"}", "[":"]", "(":")", "}":"{", "]":"[", ")":"("}
    for i in range(len(string)):
        print(parenthesis)
        if string[i] == "(" or string[i] == "[" or string[i] == "{":
            parenthesis.append(string[i])
        else:
            if len(parenthesis) == 0:
                return False
            elif pardict[string[i]] == parenthesis[len(parenthesis)-1]:
                del parenthesis[len(parenthesis)-1]
            else:
                return False
    if len(parenthesis) != 0:
        return False
    return True


"""
[ 1
] 2
( 3
) 4

[   (   )   ]
1   3   4   2   
a   b   c   d
"""
