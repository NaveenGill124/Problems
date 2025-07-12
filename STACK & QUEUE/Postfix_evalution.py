def postfix_evl(inputt):
    stack = []
    
    parts = inputt.split()
    
    
    for i in parts:

        if i.isdigit():
            
            stack.append(int(i))
        
        else:
            a = stack.pop()
            b = stack.pop()
            
            if i == '+':
        
                result = b + a

            elif i == '-':
        
                result = b - a
            elif i == '*':
        
                result = b * a
            elif i == '/':
        
                result = b / a
            elif i == '^':
        
                result = b ** a

            stack.append(result)
    
    return stack[0] if stack else None
                
            

print(postfix_evl("10 2 * 3 +"))
            
        
        