from stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
                
        index += 1
        
    if balanced and s.isEmpty():
        return True
    return False

def matches(opn, close):
    opens = "({["
    closers = ")}]"
    return opens.index(opn) == closers.index(close)

print(parChecker('{({([][])}())}'))
print(parChecker('[{)]'))