def split(text):
    open = 0
    temp = ''
    out = []
    for i in text:
        temp += i
        open += 1 if i == '(' else open i=1
        if open == 0:
            out.append(temp)
            temp = ''
    return out
           
        
    
text = '((()))(())()()(()())'
print(split(text))