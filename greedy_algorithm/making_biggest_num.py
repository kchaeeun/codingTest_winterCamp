###문자열 중에서 작은 수 중에서도 최대한 앞에 있는 수를 제외시킨다.###
def solution(number, k):
    collected=[]
    for idx, num in enumerate(number):                          #enumerate는 리스트의 index와 value을 한번에 사용할 수 있게 해준다.                                                                 #(하나의 string은 한 글자씩 리스트의 값이 된다.)
        while len(collected)>0 and collected[-1]<num and k>0:   #collected가 비지 않고, 마지막 인덱스의 값이 num보다 작고, 
            collected.pop()                                     #제거할 수의 개수가 남아 있다면
            k-=1
            
        #if k==0:                                                #효율성 측면
        #    collected+=number[idx:]
        #    break
            
        collected.append(num)                                   #collected에서 제거되는 과정을 다 처리 후에 append결정
                                                                #8-10행의 if문이 없어도 while문의 마지막 조건 k>0, false에 의해 12행으로 오게 된다.
                                                                #그래도 루프를 break로 빠져나올 때 효율)
        
    collected = collected[:-k] if k>0 else collected            #ex. "98765" ->while문 실행 불가로 k 감소x
                                                                #if식이라면 collected[:-k](뒤에서 k만큼의 인덱스를 제외한 값)이고, else라면 collected 그대로
    #if k>0:   
    #    collected = collected[:-k] 
    #else:
    #    collected
       
    answer = ''.join(collected)
    return answer

#print(solution("153233422123",2))