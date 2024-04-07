'''
문제
2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

출력
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.


'''
import sys
sys.setrecursionlimit(10**6)
N=int(sys.stdin.readline().strip())


arr=[]
for i in range(N):
    x,y=map(int,sys.stdin.readline().split())
    
    arr.append((x,y))

def quick_sort(arr,start,end):
    if start> end:
        return arr
    
    pivot=start
    left=start+1
    right=end
    
    while left<=right:
        # left는 pivot 보다 큰 수를 만날 때 까지 반복
        while left<=end and arr[left][0]<=arr[pivot][0]:
            left+=1
        #  right 는 pivot보다 작은 수를 만날 때 까지 반복
        while right > pivot and arr[right][0]>=arr[pivot][0]:
            right-=1
            
        if left > right:
            arr[pivot],arr[right]=arr[right],arr[pivot]
        
        else:
            arr[left],arr[right]=arr[right],arr[left]
        
    quick_sort(arr,start,right-1)
    quick_sort(arr,right+1,end)
    
    return


def insert_sort(arr):
    for i in range(1,len(arr)):
        value=arr[i]
        for j in range(i-1,-1,-1):
            if arr[j][0]<value[0]:
                arr[j+1]=value
                break
            else:
                if arr[j][1]>value[1]:
                    arr[j+1]=arr[j]
                else:
                    arr[j+1]=value
                    break
                    
    return

def merge_sort(arr):
    # 
    def sort(low,high):
        if high-low<2:  # 1개 일때 멈춤
            return
        mid=(low+high)//2 # 중간 값 찾기

        sort(low,mid) #왼쪽 쪼개기
        sort(mid,high) # 오른쪽 쪼개기
        merge(low,mid,high)
        
    def merge(low,mid,high):
        
        tmp=[] #결과 담을 리스트
        l,h=low,mid
        
        while l< mid and h< high:
            if arr[l][0]<arr[h][0]:
                tmp.append(arr[l])
                l+=1
            else:
                tmp.append(arr[h])
                h+=1
            
        
        while(l<mid):
            tmp.append(arr[l])
            l+=1
        while(h<high):
            tmp.append(arr[h])
            h+=1
            
        for i in range(low,high):
            arr[i]=tmp[i-low]
        # print(arr)
    return sort(0,len(arr))

'''
merge sort 하고 insert_sort 같이 쓰는건 시간 초과 안뜸. merge sort가 시간 복잡도가 최악에도 낮아서 그런듯
하지만 가장 빠른건 내장 함수 사용하는 거. 걍 내장 함수 쓰자
'''

merge_sort(arr)
arr2=arr
insert_sort(arr2)
# quick_sort(arr,0,len(arr)-1)
# print(arr)
# arr2=sorted(arr,key=lambda x: (x[0],x[1]))  # 그냥 내장 함수를 쓰는게 제일 빠르다.

for i in range(len(arr2)):
    print("{0} {1}".format(arr2[i][0],arr2[i][1]))
    