class SpecialString:
	def __init__(self, cont):
		self.cont = cont
	def __truediv__(self,other):
		line="="*len(other.cont)
		return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam/hello)



class SpecialString:
	def __init__(self, cont):
		self.cont = cont
	def __gt__(self,other):
		for index in range(len(other.cont)+1):
			result = other.cont[:index] + ">" + self.cont
			result += ">" + other.cont[index:]
			print(result)

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
spam>hello