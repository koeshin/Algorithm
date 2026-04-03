import sys



N=int(sys.stdin.readline())

sch_list=[]
for _ in range(N):
    
    sch_list.append(tuple(map(int,sys.stdin.readline().split())))


sch_list.sort(key=lambda x:(x[0], x[1]))

# print(sch_list)
sol=[]
for sch in sch_list:
    if len(sol)==0:
        sol.append(sch)

    else:
        now_st,now_ed=sch
        front_st,front_ed=sol[-1]
        if   now_st>=front_ed:
            sol.append(sch)
        else:
            if front_ed> now_ed:
                sol.pop()
                sol.append(sch)

print(len(sol))
        
        