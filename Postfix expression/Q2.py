#후위표기식 계산 프로그램
# input 7 4 -3 * 1 5 + / *
# result : -14

operators = '+-*/'

operand_stack = []

def is_operator(ch):
    for i in range(len(operators)):
        if operators[i] == ch:
            return i
    return -1
def eval_op(op):
    if len(operand_stack) == 0:
        print("Syntax Error: Stack empty in eval_op")
        exit()
    rhs = operand_stack.pop()
    if len(operand_stack) == 0:
        print("Syntax Error: Stack empty in eval_op")
        exit()
    lhs = operand_stack.pop()
    if op == '+':
        return lhs + rhs
    elif op == '-':
        return lhs - rhs
    elif op == '*':
        return lhs * rhs
    elif op == '/':
        return lhs / rhs



def eval(expr):
    token = expr.split(' ')
    for t in token:
        if not t in operators:
            operand_stack.append(int(t))
        elif is_operator(t) > -1:
            result = eval_op(t)
            operand_stack.append(result)
        else:
            print('Syntax Error : invalid character encountered')

expr = input()
eval(expr)
print(int(operand_stack.pop()))
