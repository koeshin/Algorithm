import sys


input
global maps
maps=[]
blanks=[]


for i in range(9):
    tmp=list(map(int,sys.stdin.readline().strip().split()))
    
    maps.append(tmp)
    for j in range(9):
        if tmp[j] == 0:
            blanks.append([i,j])
# print("blanks:", blanks)        
            
def check_row(dict, row):
    
    for i in range(9):
        if maps[row][i] in dict.keys():
            del dict[maps[row][i]]
            
    return dict

def check_column(dict, column):
    for i in range(9):
        if maps[i][column] in dict.keys():
            del dict[maps[i][column]]
            
    return dict

def check_box(dict,row,col):
    
    for i in range(3):
        for j in range(3):
            if maps[row+i][col+j] in dict.keys():
                del dict[maps[row+i][col+j]]
    
    return dict


global result
result=[]
def dfs(blank,idx):
    global result,maps
    
    if idx==len(blank):
        
        for i in range(9):
            for j in range(9):
                print(maps[i][j],end=' ')
            print('\n')   
        exit(0)
        
    dict={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    row,column=blank[idx]
    print("row and col:",row,column)
    print(maps)
    
    dict=check_row(dict,row)
    if len(dict)==1:
        k=list(dict.keys())[0]
        maps[row][column]=k
        dfs(blank,idx+1)
    elif len(dict)==0:
        maps[row][column]=0
        return
    
    dict=check_column(dict,column)
    # print(dict)
    if len(dict)==1:
        k=list(dict.keys())[0]
        maps[row][column]=k
        dfs(blank,idx+1)

    elif len(dict)==0:
        maps[row][column]=0
        return
    dict=check_box(dict,row//3,column//3)
    
    if len(dict)==1:
        k=list(dict.keys())[0]
        maps[row][column]=k
        dfs(blank,idx+1)
    elif len(dict)==0:
        maps[row][column]=0
        return
    print("dict:",dict)
    for key in dict.keys():
        maps[row][column]= key
        dfs(blank,idx+1)
    return 

dfs(blanks,0)