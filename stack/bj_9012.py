import sys

N= int(sys.stdin.readline())

pro=[]



for i in range(N):
    tmp=sys.stdin.readline().strip()
    pro.append(tmp)

def sol(problem):
    
    
    for i in range(N):
        tmp=problem[i]
        tmp_list=[]
        flag=0
        for j in range(len(tmp)):
            if tmp[j]=='(':
                tmp_list.append('(')
            
            elif tmp[j]==')':
                if len(tmp_list)!=0:
                    tmp_list.pop()
                else:
                    print('NO')
                    flag = -1
                    break
        if flag==0:
            if len(tmp_list)==0:
                print("YES")
            else:
                print('NO')
        
    return

sol(pro)