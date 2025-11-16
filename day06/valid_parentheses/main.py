"""Day-06 Valid Parentheses
Valid brackets:(),{},[]"""

def is_valid_parentheses(s:str)->bool:

    pairs={')':'(',']':'[','}':'{','>':'<'}
    stack=[]

    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs:
            if not stack:
                return False
            top = stack.pop()
            if top!=pairs[ch]:
                return False
        else:
            return False
    return len(stack)==0

if __name__=="__main__":

    user_input = input('enter bracket string(ex:(),{},[].):')
    if is_valid_parentheses(user_input):
        print("The parentheses are valid ✓")
    else:
        print("invalid parantheses ✗") 
    

  