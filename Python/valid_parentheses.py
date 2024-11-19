def is_valid(s):
    stack = []
    parentheses = {
        ']': '[',
        ')': '(',
        '}': '{'
    }
    for char in s:
        if char in parentheses.values():
            stack.append(char)
        elif char in parentheses.keys():
            try:
                last = stack.pop()
            except:
                return False
            if last != parentheses[char]:
                return False

    if len(stack) == 0:
        return True
    else:
        return False


print(is_valid('}'))
