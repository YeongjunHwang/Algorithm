# 입력 수식의 괄호가 올바른지 검사 test : [[{{}}]]
# key open과 close를 0,1,2 으로 표현하면서 return 하는것
open = ['[','{','(']
close = [']','}',')']

def is_open(ch):
    for i in range(len(open)):
        if open[i] == ch:
            return i  #대괄호는 0 중괄호는 1 소활호는 2
    return -1

def is_close(ch):
    for i in range(len(close)):
        if close[i] == ch:
            return i
    return -1

def is_balaced(expr):
    tmp = []
    balanced = True
    index = 0

    while balanced and index<len(expr):
        ch = expr[index]
        if (is_open(ch) > -1):
            tmp.append(ch)
        elif (is_close(ch) > -1):
            if len(tmp) == 0: #오류를 위한 추가
                balanced = False
                break
            top_ch = tmp.pop()
            if is_open(top_ch) != is_close(ch):
                balanced = False
        index += 1
    return balanced and len(tmp) == 0




expr = input() #입력은 괄호만으로 이루어진 하나의 문자열이다.


if is_balaced(expr):
    print(expr + ': balanced.')
else:
    print(expr + ': unbalanced.')