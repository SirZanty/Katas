def pig_it(text): #6/1/2021
    return ' '.join([i+'ay' if i.isalpha() else i for i in [x[1:]+x[0] for x in text.split()]])