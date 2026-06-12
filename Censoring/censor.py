with open("censor.in", "r") as inline, open("censor.out", "w") as outline:
    
    S= inline.readline().strip()
    T = inline.readline().strip()

    len_T=len(T)

    stack = []

    for char in S:
        stack.append(char)
        if len(stack)>=len_T:
            if "".join(stack[-len_T:]) == T:
                del stack[-len_T:]
    outline.write("".join(stack)+'\n')
    