def pig_it(text):  # 6/1/2021
    return ' '.join([i + 'ay' if i.isalpha() else i for i in [x[1:] + x[0] for x in text.split()]])


# print(validBraces("[()]{{()}}"))   analisis de por patron
def validBraces(string):  # 11/1/2021
    parenthesis = []
    pardict = {"{": "}", "[": "]", "(": ")", "}": "{", "]": "[", ")": "("}
    for i in range(len(string)):
        print(parenthesis)
        if string[i] == "(" or string[i] == "[" or string[i] == "{":
            parenthesis.append(string[i])
        else:
            if len(parenthesis) == 0:
                return False
            elif pardict[string[i]] == parenthesis[len(parenthesis) - 1]:
                del parenthesis[len(parenthesis) - 1]
            else:
                return False
    if len(parenthesis) != 0:
        return False
    return True


def max_sequence(arr):  # 12/1/2021
    currentSum = 0
    maxSum = 0
    if (len(arr) == 0):
        return 0
    for x in arr:
        currentSum = max(x, currentSum + x)
        maxSum = max(maxSum, currentSum)
    return maxSum


def snail(snail_map):
    l = []
    while len(snail_map):
        l.extend(snail_map[0])
        snail_map.pop(0)
        snail_map = list(reversed(list(zip(*snail_map[::1]))))
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


class Calculator(object):  # 1-2-2021
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


# 3.2.2021
import collections


def encode(string2en):
    return "".join([u+u+u for u in "".join([str(bin(ord(x))).replace("b","").zfill(8) for x in string2en])])
    #return "*".join([str(bin(ord(x))).replace("b","").zfill(8) for x in string2en])

def decode(bits2dec):
    r8 = "".join(
        [collections.Counter(r).most_common(1)[0][0] for r in [bits2dec[i:i + 3] for i in range(0, len(bits2dec), 3)]]
    )
    return ''.join([chr(int(r8[i:i + 8], 2)) for i in range(0, len(r8), 8)])


#22.2.2021
'''
Take the following IPv4 address: 128.32.10.1

This address has 4 octets where each octet is a single byte (or 8 bits).

1st octet 128 has the binary representation: 10000000
2nd octet 32 has the binary representation: 00100000
3rd octet 10 has the binary representation: 00001010
4th octet 1 has the binary representation: 00000001
So 128.32.10.1 == 10000000.00100000.00001010.00000001

Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: 2149583361

Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.
'''
import re
def int32_to_ip(int32):
    return ".".join( [ str(int(num,2)) for num in  re.findall(r'[01]{8}',"{:>032b}".format(int32))])

def parts_sumss(ls):
    # your code
    r=[]
    while len(ls)!=0:
        r.append(sum(ls))
        ls.pop()
    r.append(0)
    return r

def parts_sums(ls):

    return [sum(ls[x:]) for x in range(0,len(ls)+1)]

def parts_sumsss(ls):
    sums = [0] * (len(ls) + 1)
    for i, e in enumerate(reversed(ls)):
        sums[len(ls) - i - 1] += sums[len(ls) - i] + e
    return sums