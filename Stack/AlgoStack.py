from Stack import Stack

def validParenthesis(string):
    stack = Stack()
    for s in string:
        if (s == "(") or (s == "{") or (s == "["):
            stack.push(s)
        elif (not stack):
            return False
        else:
            lastParentheses = stack.pop()
            if (((s == ")") and (lastParentheses != "(")) or 
                ((s == "}") and (lastParentheses != "{")) or 
                ((s == "]") and (lastParentheses != "["))):
                return False
    return True


if __name__ == "__main__":
    string = "({[]})"
    string2 = "(}"
    string3 = "[]()"
    print(validParenthesis(string))
    print(validParenthesis(string2))
    print(validParenthesis(string3))