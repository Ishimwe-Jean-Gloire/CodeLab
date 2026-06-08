n=int(input())
if n > 100:
    raise ValueError("n must be less than or equal to 100")
seq=list(map(int,input().split()))  # elements must each have |x| <= 100
if any(abs(x) > 100 for x in seq):
    raise ValueError("sequence elements must have absolute value at most 100")
else:

    for i in range(n):
        if seq[i]>=0:
            seq[i]+=2
print(*seq)