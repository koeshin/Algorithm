import sys


global N
N=int(sys.stdin.readline().strip())
def Print_3_star(idx,n,long):   # idx= 맨위나 중간을 그릴지, n= 현재 3의 거듭제곱 값, long=N//n
    l=n//3
    if l==1:
        if idx== 'top':
            str='***'*long

            stars=str
        if idx=="mid":
            str="* *"*long
        
            stars=str

    else:
        if idx== 'top':
            str='*'*l
            blank=' '*l
            stars=(str+blank+str)*long
        if idx=="mid":
            str="* *"*(l//3)
            blank=' '*l
            stars=(str+blank+str)*long
    print(stars)
    print(len(stars))
    return

def solution(n):
    global N
    k=0
    while n>1:
        n=n//3
        k+=1
    
    for i in range(k):
        num=3**(i)
        long=N//num
        Print_3_star("top",num,long)
        Print_3_star("mid",num,long)
        Print_3_star("top",num,long)
        
        
        

Print_3_star('top',27,3)