class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])


spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont) + 1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)


spam = SpecialString("spam")
hello = SpecialString("Hello world!")
spam > hello


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
    @property
    def pineapple_allowed(self):
        return False
    @staticmethod
    def validate_topping(toppings):
        if toppings == "chicken":
            raise ValueError("No pineapples!")
        else:
            return True


ingredients = ["chesse", "onions", "spam", "pineapple"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)
    print(pizza.toppings)
pizza=Pizza(["cheese","tomate"])
print(pizza.pineapple_allowed)
#pizza.pineapple_allowed = True   #No es posible cambiar las propiedades para solo lectura


#REGULAR EXPRESSIONS
print("EXPRESIONES REGULARES")
import re
pattern = r"spam1"
matchinfo=re.search(pattern,"spamspam1spam1sdfd")
if re.match(pattern,"spamspamspam"):
    print("Match")
else:
    print("No Match")

if matchinfo:
    print(matchinfo.group())
    print(matchinfo.start())
    print(matchinfo.end())
    print(matchinfo.span())

str="Test new GP"
pattern=r"new"
newstr=re.sub(pattern,"reemplaza",str)
print(newstr)

#METACARACTERES EN EXPRESIONES REGULARES

pattern=r"gr..y"  #EL PUNTO REPRESENTA CUALQUIER CARACTYER
if re.match(pattern,"greDy"):
    print("Match 1")

pattern = r"^gr.y$"  #Inicia con gr luego esta cualquier caracter y finaliza con y
if re.match(pattern,"grey"):
    print("Match 1")

pattern = r"[aeiou]"
if re.search(pattern,"grey"):  #The pattern [aeiou] in the search function matches all strings that contain any one of the characters defined.
    print("Encuentra")

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern,"E3"):
    print('Match 1 nuevo patron')  #The pattern in the example above matches strings that contain two or more alphabetic uppercase letters followed by a digit.


pattern = r"[1-5][0-9]" #Cualquier dos o mas digitos desde 10

if re.search(pattern,"191"):
    print('Match 1 nuevo patron')


pattern = r"[^A-Z]"  #The pattern [^A-Z] excludes uppercase strings.Note, that the ^ should be inside the brackets to invert the character class.
if re.search(pattern,"this is all quiet"):
    print("Match 1")
if re.search(pattern,"AbCdEfG123"):
    print("Match 2")


pattern = r"egg(spam)*"   # * zero or more + one or more   ?  zero or one repetition
if re.match(pattern,"egg"):
    print("Empareja")

pattern = r"ice(-)?cream"
if re.match(pattern,"ice-cream"):
    print('Encuentra cero o un - dentro de la cadena')


pattern = r"9{1,3}$"   # el simbolo de dolar $ indica que ahi debe acabar la cadena, las llaves indica el intervalo que debe repetir el numero anterior
if re.match(pattern,"94"):
    print("Existe de uno a tres nueves")