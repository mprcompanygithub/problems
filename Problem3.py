class ExpressionConverter:
    def __init__(self, expression):
        self.expression = expression

    def precedence(self, op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return 0

    def infix_to_postfix(self):
        stack = []
        result = ''
        for char in self.expression:
            # print(char)
            if char.isnumeric():
                result += char
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop() # ( pop out
            else:
                while stack and self.precedence(stack[-1]) >= self.precedence(char):
                    result += stack.pop()
                stack.append(char)
            # print(stack)
        while stack:
            result += stack.pop()
        # print(result)
        print("Conversion from infix to postfix : ", result)
        print("Postfix Value After conversion : ", evaluate(result))

    def infix_to_prefix(self):
        stack = []
        result = ''
        exp = self.expression[::-1]
        for char in exp:
            if char.isnumeric():
                result += char
            elif char == ')':
                stack.append(char)
            elif char == '(':
                while stack and stack[-1] != ')':
                    result += stack.pop()
                stack.pop()
            else:
                while stack and self.precedence(stack[-1]) > self.precedence(char):
                    result += stack.pop()
                stack.append(char)
        while stack:
            result += stack.pop()
        print("Conversion from infix to prefix : ",result[::-1])
        print("Prefix Value After conversion : ",evaluate(result))



def evaluate(expression):
    # print(expression)
    stack = []
    for char in expression:
        if char.isnumeric():
            stack.append(int(char))
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            if char == '+':
                stack.append(val2 + val1) #6+0=0
            elif char == '-':
                stack.append(val2 - val1) #5-5=0
            elif char == '*':
                stack.append(val2 * val1) #3*2=6
            elif char == '/':
                stack.append(val2 / val1)
    return stack.pop()



# Problem 3
infix_expr = "(2*3)+(5-5)"
converter = ExpressionConverter(infix_expr)
converter.infix_to_postfix()
converter.infix_to_prefix()
