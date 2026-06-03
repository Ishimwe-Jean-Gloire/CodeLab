n=int(input())
seq=[n]
while n!=1:
    if n%2==0:
        n//=2
    else:
        n=n*3+1
    seq.append(n)
print(*seq)