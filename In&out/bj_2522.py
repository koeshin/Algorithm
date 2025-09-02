import sys


N= int(sys.stdin.readline())


for i in range(1,2*N):
    k=abs(N-i)
    re=N-k
    print(' '*k + '*'*re)