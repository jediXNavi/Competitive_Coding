str1 = '( A + B ) * ( C + D )'
str2 = '( A + B ) * C'
str3 = 'A + B * C'

from data_structures import Stack

def infixtopostfix(string):

    comp = string.split(' ')
    output = []
    operator_precedence = {"+": 1, "-": 1, "/": 2, "*": 2, "(": 3, ")": 3}
    operator_stack = Stack()

    for value in comp:
        if value in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or value in '0123456789':
            output.append(value)
        elif value == '(':
            operator_stack.push(value)
        elif value == ')':
            operator = operator_stack.pop()
            while operator != '(':
                output.append(operator)
                operator = operator_stack.pop()
        else:
            while not operator_stack.isEmpty() and \
                    operator_precedence[operator_stack.peek()] <= operator_precedence[value]:
                output.append(operator_stack.pop())
            operator_stack.push(value)

    while not operator_stack.isEmpty():
        token = operator_stack.pop()
        output.append(token)

    return ' '.join(output)

ans = infixtopostfix(str1)
print(ans)






