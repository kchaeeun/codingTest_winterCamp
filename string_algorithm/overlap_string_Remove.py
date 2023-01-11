def solution(my_string):
    overlap_rm=set(my_string) #' ' 슬롯까지 중복 삭제 해줌
    #print(overlap_rm)
    answer=''
    for s in my_string:
        for o in list(overlap_rm):
            if o==s:
                overlap_rm.discard(o)
                answer+=o

solution("people")
