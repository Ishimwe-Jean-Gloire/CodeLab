n=int(input())
seq=list(map(int,input().split()))
for i in range(n):
    if seq[i]>=0:
        seq[i]+=2
print(*seq)