from stack import *

def is_balanced(new_string):
    stack = Stack()
    balanced = True
    index = 0
    
    while index < len(new_string) and balanced:
        symbol = new_string[index]
        if symbol in "({[":
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                top = stack.pop()
                if not pairs(top, symbol):
                    balanced = False

        index = index + 1

    if stack.is_empty() and balanced:
        return True
    else:
        return False

def pairs(open, close):
    opens = "({["
    closes = ")}]"
    return opens.index(open) == closes.index(close)

print(is_balanced("((()))"))








