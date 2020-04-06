# https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/basic-calculator-iii.py


def calculate(s):
    operands, operators = [], []
    operand = ""
    for i in reversed(range(len(s))):
        if s[i].isdigit():
            operand += s[i]
            if i == 0 or not s[i - 1].isdigit():
                operands.append(int(operand[::-1]))
                operand = ""
        elif s[i] == ')' or s[i] == '*' or s[i] == '/':
            operators.append(s[i])
        elif s[i] == '+' or s[i] == '-':
            while operators and \
                    (operators[-1] == '*' or operators[-1] == '/'):
                compute(operands, operators)
            operators.append(s[i])
        elif s[i] == '(':
            while operators[-1] != ')':
                compute(operands, operators)
            operators.pop()

    while operators:
        compute(operands, operators)

    return operands[-1]


def compute(operands, operators):
    left, right = operands.pop(), operands.pop()
    op = operators.pop()
    if op == '+':
        operands.append(left + right)
    elif op == '-':
        operands.append(left - right)
    elif op == '*':
        operands.append(left * right)
    elif op == '/':
        operands.append(left / right)


while True:
    try:
        s = input().strip()
        print(calculate(s))
    except:
        break
