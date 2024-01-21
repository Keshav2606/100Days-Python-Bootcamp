from logo import logo
import os

print(logo)

def calculate(n1, op, n2):
    """Takes 2 numbers and an operator as input and after performing operation on both number returns the result as output"""

    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == 'x':
        return n1 * n2
    elif op == '/':
        return n1/n2

repeat = ""
result = float(input("Enter First Number: "))
print('''
+
-
x
/
''')
while repeat != 'n':
    n1 = result
    op = input("Pick an Operation: ")
    n2 = float(input("Enter Second Number: "))
    result = calculate(n1, op, n2)
    print(f"Result of {n1} {op} {n2}: {result}")
    repeat = input(f"Do you want to perform operation with {result}? Type 'y' or 'n': ").lower()