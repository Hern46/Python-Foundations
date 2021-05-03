class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop_item(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def balanced_check(string):
    s = Stack()
    for element in string:
        s.push(element)

    closed_par_stack = Stack()
    balanced_list = ['()', '[]', '{}']
    pair_list = []

    peek = s.peek()
    if peek == '(' or peek == '[' or peek == '{':
        return False

    while s.size() > 0:
        par = s.pop_item()
        if par == ')' or par == ']' or par == '}':
            closed_par_stack.push(par)
        else:
            if closed_par_stack.size() > 0:
                pair_list.append(par + closed_par_stack.pop_item())
            else:
                return False

    if not closed_par_stack.isEmpty():
        return False

    for element in pair_list:
        if element not in balanced_list:
            return False

    return True

string = '()({[]})[][[]]{{{{}}}}[](){}{{[]}}[[[]]]()()[]{}[]{}'

string2 = '()(){]}'

print(balanced_check(string))
