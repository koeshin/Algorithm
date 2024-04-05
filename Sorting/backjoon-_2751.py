'''
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

'''


import sys
sys.setrecursionlimit(10**6)
N=int(sys.stdin.readline().strip())

arr=[]
for i in range(N):
    tmp=int(sys.stdin.readline().strip())
    arr.append(tmp)
# print("arr:",arr)
'''
i, i+1의 값의 크기를 비교하며너 i+1이 더 크다면 i와 자리르 바꾸는 방법. 시작 복잡도는 O(N^2)
'''
def bubble_sort(list):
    for i in range(len(list)):
        for j in range(1,len(list)-i):
            if list[j-1]>list[j]:
                list[j-1],list[j]=list[j],list[j-1]
                
    
    
    
    return list


# bubble_sort_res=bubble_sort(arr)
# print(bubble_sort_res)


'''
* 선택 정렬은 앞쪽 부터 정렬하는 방식. 맨 앞에서 부터 최솟값을 찾으면서 정렬하는 방식. 비교 횟수는 많지만 교환 횟수는 적음
* 시간 복자도는 O(N^2)
'''

def selection_sort(list):
    for i in range(len(list)):
        tmp_min=list[i]
        
        for j in range(i+1,len(list)):
            if list[j]<tmp_min:
                list[i],list[j]=list[j],list[i]    

    return list

# selection_sort_res=selection_sort(arr)
# print(selection_sort_res)


'''
* 삽입 정렬은 i 번째 원소를 정렬 된 상태의 앞부분과 비교하여 적절한 곳에 삽입 하는 방식
* i-1번째 원소까지는 모두 정렬된 상태어야 하며 i-1번쨰부터 0번째까지 원소와 i번재 원소를 각가 비교
* i 번째 원소보다 작은 값이 발견되면 그 위치에 i 번째 원소를 삽입
* 시간 복잡도은 평균 O(N^2), 하지만 리스트가 정렬되어있을수록 빠르게 정렬됨.

'''


def insertion_sort(arr):
    for x in range(1, len(arr)):
        value = arr[x]
        prev = x - 1
        while prev >= 0 and arr[prev] > value:
            arr[prev + 1] = arr[prev]
            prev -= 1
            
        arr[prev + 1] = value
    return arr
# insert_sort_res=insertion_sort(arr)
# print(insert_sort_res)


'''
* 퀵 정렬은 분할 정복 방법으로 pivot을 기준으로 작은 값을 왼쪽 큰 값을 오른쪽에 위치 시킴
* 왼쪽과 오른쪽에 해당하는 원소들에 대해 두 배영롤 나눔
* 분할된 두개에 배열에 대해 재귀적으로 이과정을 반복
* 시간 복잡도는 평균 O(NlogN)
* 이건 좀 어렵다.....
'''


def quick_sort(array, start, end):
    if start >= end:
        return



    mid=(start+end)//2
    arr[start],arr[mid] = arr[mid],arr[start]
    pivot = start #피벗 초기값은 첫번째 요소
    left = start+1
    right = end
    while left <= right:
   
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left+=1
            
            #피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right-=1
            
        if left>right: # 엇갈렸다면 작은 right -=1 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]

            
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체 
            array[left], array[right] = array[right], array[left]
            
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
    
quick_sort(arr, 0, len(arr)-1)

for a in arr:
    sys.stdout.write(str(a)+"\n")



def quick_sort2(arr):   #*조금 더 깔끔한 방식 
    if len(arr) <=1:
        return arr
    
    pivot=arr[0]  #* pivot=첫번째 원소
    tail=arr[1:]  # 나머지는 테일

    left_side=[x for x in tail if x<=pivot]
    right_side=[x for x in tail if x> pivot]

    return quick_sort2(left_side)+[pivot]+quick_sort2(right_side)

# print(quick_sort2(arr))
