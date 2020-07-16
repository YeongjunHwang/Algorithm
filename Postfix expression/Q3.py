#후위 표기식 변환 프로그램 - 괄호없는 경우
# ex input : 2 - 10 / 5 * 6 + 4

# 중위 표기식을 처음부터 순서대로 읽으면서
# 피연산자는 즉시 출력한다.
# 모든 연산자는 일단 스택에 push한다.
# 단, 이때 스택 내에 우선순위가 자신보다 더 높은 연산자가 있으면 pop하여 출력
# 한 후에 push한다.
# 수식이 종료되면 스택에 있는 모든 연산자를 pop하여 출력한다.


operators = "+-*/"

operator_stack = []

def precedence(op):
    if op == '+':
        return 1
    elif op == '-':
         return 1
    elif op == '*':
         return 2
    elif op == '/':
         return 2

def process_op(op, pos):
    if len(operator_stack) == 0:
        operator_stack.append(op)
    else:
        top_op = operator_stack[-1]
        if precedence(op) > precedence(top_op):
            operator_stack.append(op)
        else:
            while len(operator_stack) != 0 and precedence(op) <= precedence(top_op):
                operator_stack.pop()
                pos += ' '
                pos += top_op
                if len(operator_stack) != 0:
                    top_op = operator_stack[-1]
            operator_stack.append(op)
    return pos


def is_operator(op):
    for i in range(len(operators)):
        if operators[i] == op:
            return i
    return -1

def convert(infix):
    pos = ''
    token = infix.split(' ')
    for t in token:
        if not t in operators:
            if pos != '':
                pos += ' '
            pos += t
        elif t in operators:
            pos = process_op(t, pos)
    while len(operator_stack) != 0:
        pos += ' '
        pos += operator_stack.pop()
    return pos





infix = input()
result = convert(infix)
print(result)