def solution(numbers):
    numbers=[str(x) for x in numbers]                         #numbers안에 수들을 string형으로 변경          
    numbers.sort(key=lambda x : (x*4)[:4],reverse=True)       #slicing은 문자열에서(ex.'s','t','r')가능하다. int형을 slice할 수는 없다.
                                                              #앞에서 부터 4글자까지 끊어진 수를 기준으로 sort진행(즉, ()안의 내용은 sort조건을 의미), 내림차순(큰 것 우선으로)
                                                              #+lambda 함수의 식에 해당되는 key값이 정렬되어진다
                                                              
    if numbers[0] == '0':                                     #정렬 후에 가장 크게 만드는 값, 즉 index가 0인 값이 '0'이면 '000'이런식으로 연결될 수 있기에 '0'으로 return 되게 설정한다.
        answer='0'
    else:
        answer=''.join(numbers)                               #numbers 리스트 값을 앞에서부터 차례대로 join(연결)해준다.
        
    return answer