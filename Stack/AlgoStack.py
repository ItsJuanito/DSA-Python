from Stack import Stack

# This function returns true or false whether the parentheses are symetrical or not
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

# Test Stack methods
if __name__ == "__main__":
    string = "({[]})"
    string2 = "(}"
    string3 = "[]()"
    print(validParenthesis(string))
    print(validParenthesis(string2))
    print(validParenthesis(string3))

'''
Sample Output:
 - True
 - False
 - True
'''