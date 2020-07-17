#후위 표기식 변환 프로그램 - 괄호있는 경우
# 1.,여는 괄호는 무조건 스택에 push한다. 이때 스택 내의 어떤 연산자도 pop하지 않는다.
# 2. 어떤 연산자를 스택에 push할 때 스택의 top에 여는 괄호가 있으면 아무도 pop하지 않고 그냥 push한다.
# 3. 입력에 닫는 괄호가 나오면 스택에서 여는 괄호가 나올 때 까지 pop하여 출력한다. 닫는 괄호는 스택에 push하지 않는다.

# EX input : ( 2 + 10 ) / ( 9 - 6 )
# result : 2 10 + 9 6 - /

operators = '+-*/()'
precedence = [1,1,2,2,-1,-1]
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
    elif op == '(':
        return -1
    elif op == ')':
        return -1


def process_op(op, pos):
    if len(operator_stack) == 0 or op == '(':
        operator_stack.append(op)
    else:
        top_op = operator_stack[-1]
        if precedence(op) > precedence(top_op):
            operator_stack.append(op)
        else:
            while len(operator_stack) != 0 and precedence(op) <= precedence(top_op):
                operator_stack.pop()
                if top_op == '(': # op의 우선 순위가 top_op 보다 낮거나 같은데 top_op가 여는 괄호이면 op는 단는 괄호이다
                    break
                pos += ' '
                pos += top_op
                if len(operator_stack) !=0:
                    top_op = operator_stack[-1]
            if op != ')':
                operator_stack.append(op)
    return pos
def convert(infix):
    pos =''
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