def pig_it(text):  # 6/1/2021
    return ' '.join([i + 'ay' if i.isalpha() else i for i in [x[1:] + x[0] for x in text.split()]])

#print(validBraces("[()]{{()}}"))   analisis de por patron
def validBraces(string):    # 11/1/2021
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

def max_sequence(arr):  # 12/1/2021
    currentSum = 0
    maxSum = 0
    if(len(arr) == 0):
        return 0
    for x in arr:
        currentSum = max(x, currentSum + x)
        maxSum = max(maxSum, currentSum)
    return maxSum

def snail(snail_map):
    l=[]
    while len(snail_map):
        l.extend(snail_map[0])
        snail_map.pop(0)
        snail_map=list(reversed(list(zip(*snail_map[::1]))))
    return l

"""


array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
         
         6,9
         5,8
         4,7
expected = [1,2,3,6,9,8,7,4,5]
test.assert_equals(snail(array), expected)


[ 1
] 2
( 3
) 4

[   (   )   ]
1   3   4   2   
a   b   c   d
"""



'''
https://medium.com/@lanya4190/03-94b12155fdd  #1-2-2021
Solucion buena para y optima

def top_3_words(text)
  result = {}
  ary = text.downcase.gsub(/[^ \'\w\s]|\p{Punct}{2,}|[\']\s/, "").split
  ary.each do |word|
    if result[word]
      result[word] += 1 
    else
      result[word] = 1
    end
  end
  result.max_by(3){|k, v| v}.to_h.keys
end


def top_3_words(text)
  text.scan(/[A-Za-z']+/)
      .select { |x| /[A-Za-z]+/ =~ x }
      .group_by { |x| x.downcase }
      .sort_by { |k,v| -v.count }
      .first(3)
      .map(&:first)
end


'''


class Calculator(object): #1-2-2021
    def precedence(op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return 0

        # Function to perform arithmetic
        # operations.
    def applyOp(a, b, op):

        if op == '+': return a + b

        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return a // b


# Function that returns value of
# expression after evaluation.
    def evaluate(tokens):
        # stack to store integer values.
        values = []

        # stack to store operators.
        ops = []
        i = 0

        while i < len(tokens):

            # Current token is a whitespace,
            # skip it.
            if tokens[i] == ' ':
                i += 1
                continue

        # Current token is an opening
        # brace, push it to 'ops'
            elif tokens[i] == '(':
                ops.append(tokens[i])

        # Current token is a number, push
        # it to stack for numbers.
            elif tokens[i].isdigit():
                val = 0

            # There may be more than one
            # digits in the number.
                while (i < len(tokens) and
                   tokens[i].isdigit()):
                    val = (val * 10) + int(tokens[i])
                    i += 1

                values.append(val)

            # right now the i points to
            # the character next to the digit,
            # since the for loop also increases
            # the i, we would skip one
            #  token position; we need to
            # decrease the value of i by 1 to
            # correct the offset.
                i -= 1

    # Closing brace encountered,
    # solve entire brace.
            elif tokens[i] == ')':
                while len(ops) != 0 and ops[-1] != '(':
                    val2 = values.pop()
                    val1 = values.pop()
                    op = ops.pop()

                    values.append(Calculator.applyOp(val1, val2, op))

    # pop opening brace.
                ops.pop()

# Current token is an operator.
            else:

# While top of 'ops' has same or
# greater precedence to current
# token, which is an operator.
# Apply operator on top of 'ops'
# to top two elements in values stack.
                while (len(ops) != 0 and Calculator.precedence(ops[-1]) >= Calculator.precedence(tokens[i])):
                    val2 = values.pop()
                    val1 = values.pop()
                    op = ops.pop()

                    values.append(Calculator.applyOp(val1, val2, op))

# Push current token to 'ops'.
                ops.append(tokens[i])

            i += 1

# Entire expression has been parsed
# at this point, apply remaining ops
# to remaining values.
        while len(ops) != 0:
            val2 = values.pop()
            val1 = values.pop()
            op = ops.pop()

            values.append(Calculator.applyOp(val1, val2, op))

# Top of 'values' contains result,
# return it.
        return values[-1]