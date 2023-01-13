import heapq

def solution(scoville, K):
    answer =0
    heapq.heapify(scoville)
    while True:
        min1 = heapq.heappop(scoville)  #최소값
        
        if min1 >= K :                  #최소값이 K를 넘으면 모든 수가 넘으므로 반복문 break
            break
        elif len(scoville)==0:          #리스트 안에 수가 pop으로 인해 모두 삭제(원래 한개 였기에 음식을 섞을 수x)
            answer=-1                   #반복문 중단
            break
            
        min2 = heapq.heappop(scoville)

        result = min1 + 2 * (min2)
        scoville.append(result)         #heapq.heappush(scoville,result)
        answer+=1
            
    return answer