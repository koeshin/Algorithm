import sys


def read_puzzle():
    maps = [[int(x) for x in sys.stdin.readline().strip().split()] for _ in range(9)]
    blanks = [(i, j) for i in range(9) for j in range(9) if maps[i][j] == 0]
    return maps, blanks
# print("blanks:", blanks)        
            
def check(row,column,maps,num):  # 하나의 값만 컴증 -> 불필요한 검증 삭제
    
    dict={num:0}
    box_row=row//3
    box_col=column//3
    
    # col&row 확인
    for i in range(9):
        if maps[row][i]== num or maps[i][column]==num:
            return False
    # 3*3 박스 확인 
    for i in range(3):
        for j in range(3):
            if maps[3*box_row+i][3*box_col+j] ==num:
                # print("col,row:",row+i,col+j)
                return False
    
    return True



def dfs(maps,blank,idx):  # 시간 초과가 계속 발생
    
    if idx == len(blanks):
        # Print the solution
        for row in maps:
            print(*row, sep=' ')
       
        exit(0)
        

    row,column=blank[idx]
    # print("row and col:",row,column)
    # print(maps)
    
    for i in range(1,10):
        flag=check(row,column,maps,i)
        if flag ==False:
            continue
        maps[row][column]=i
        dfs(maps,blank,idx+1)
        maps[row][column]=0


    return 
if __name__ == "__main__":
    maps, blanks = read_puzzle()
    dfs(maps, blanks, 0)

