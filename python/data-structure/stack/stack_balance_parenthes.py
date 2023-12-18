class Stack(list):
    
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, items):
        self.items.append(items)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception('Stack is empty!')
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def main():
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        # print(stack.size())
        # print(stack.peek())
        print(stack.pop())
        # print(stack.peek())

def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index = index + 1
    
    if balanced and s.is_empty():
        return True
    else:
        return False
    
def par_checker_multiple(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
    if balanced and s.is_empty():
        return True
    else:
        return False

def matches(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)

# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.size())
# print(stack.peek())
# print(stack.pop())
# print(stack.peek())
# print(stack.size())

# print(par_checker('((()))'))
print(par_checker('((]'))
