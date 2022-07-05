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
# This function returns a reversed version of the string
def reverseString(string):
    if len(string) == 0:
        return string
    stack = Stack()
    for i in string:
        stack.push(i)
    result = ""
    while stack.size() != 0:
        result += stack.pop()
    return result

# Test Stack methods
if __name__ == "__main__":
    string = "({[]})"
    string2 = "(}"
    string3 = "[]()"
    string4 = "restart"
    print(validParenthesis(string))
    print(validParenthesis(string2))
    print(validParenthesis(string3))
    
    print(reverseString(string4))

'''
Sample Output:
 - True
 - False
 - True
 - tratser
'''