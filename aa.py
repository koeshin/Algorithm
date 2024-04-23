def solution(coin, cards):
    answer = 1
    dict={}
    idx=len(cards)//3 # 카드의 3분의 1 인덱스
    MAX=(len(cards)-idx)//2+1

    pairs=[]  #현재 가지고 있는 페어
    N=len(cards)+1
    for i in range(idx):
        pair=N-cards[i]
        if pair in dict.keys(): #페어가 이미 딕셔너리에 있을 경우 pairs에 넣기
            pairs.append(pair)  
            continue
        else:
            dict[cards[i]]=pair   # 페어가 없을 경우 현재 카드값을 키로 딕셔너리에 저장
    
    
    
    tmp_dict={}
    window_pair=[]
    start=idx
    while True:
        # print("start",start)

        end=start+(len(pairs)+1)*2
        
        if end>len(cards):
            end=len(cards)
        window=cards[start:end]

        k=len(window)//2
        if k==0:
            k=1
        tmp_pairs=0 #첫 번쨰 리스트는 첫 카드의 페어, 두번쨰 리스트는 윈도우 안에 페어
        

        if coin >0:
            for num in window:
                pair=N-num
                if pair in dict.keys() and coin>0:
                    pairs.append(pair)
                    tmp_pairs+=1
                    coin-=1
                else:
                    if pair in tmp_dict.keys():
                        window_pair.append(pair)
                    else:
                        tmp_dict[num]=pair
            if coin>2 and tmp_pairs==0 and len(window_pair)!=0:
                pairs.append(window_pair.pop(0))
                coin-=2

        # print("pair2",pairs)
            
        start=end
        for i in range(k):
            if len(pairs)>0:
                pairs.pop() # 합이 n+1인 카드 두 장 내기  
                answer+=1
            else:
                if answer>MAX:
                    answer=MAX
                return answer
                
    return answer
# 위에 코도는 75점 맞은 코드 이유를 모겠음.....


