import sys

n=int(sys.stdin.readline().strip())

zeros=0
divisor=5

while n>=divisor:
    zeros+=n//divisor
    divisor*=5

print(zeros)