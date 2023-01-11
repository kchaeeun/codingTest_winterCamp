def solution(s):
    answer = ''
    dic={}
    lst=[]
    for my_string in s:
        if dic.get(my_string,0)==0:
            dic[my_string]=1
        else:
            dic[my_string]+=1

    for once_string, once in dic.items():
        if once ==1:
            lst.append(once_string)
    lst.sort()
    answer=''.join(lst)

    #for l in lst:
    #    answer+=l

    #print(answer)
    return answer            

res=solution('hello')
print(res)