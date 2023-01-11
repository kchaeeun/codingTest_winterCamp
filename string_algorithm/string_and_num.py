#각 숫자에 대응되는 영단어 -> dictionary 사용
def solution(s):
    #answer = 0
    nums={"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    
    for num in nums:
        #print(num)
        s=s.replace(num,nums[num]) #계속 반복해서 처리해줘야함!
        #print(s)

    return int(s)

#res=solution("one3four8")
#print(res)