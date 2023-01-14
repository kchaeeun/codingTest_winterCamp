def solution(tickets):
    routes={}
    for t in tickets:
        routes[t[0]] = routes.get(t[0],[])+[t[1]]       #t[0]이 routes 디렉토리의 키 값, 즉 출발지
    #print(routes)

    for r in routes:
        routes[r].sort(reverse=True)                    #알파벳 역순으로 키 값을 정렬(역순의 수를 먼저 빼는 것이 더 효율적이다)
                                                        #O(nlogn)

    stack = ["ICN"]                                     #스택에 가장 먼저 가는 곳인 "ICN"을 넣어줌
    path = []

    while len(stack) > 0 :                              
        top = stack[-1]                                 #스택의 가장 윗 부분(=리스트의 가장 끝 부분)
        if top not in routes or len(routes[top]) == 0:  #routes안에 top이 없다는 것은 도착지의 역할은 하지만 출발지의 역할은 못한다.(연결된 선이 더 이상 없음)
            path.append(stack.pop())                    #routes[top]의 길이가 0인 이유는 더이상 도착지가 없는 경우
        else:                                           
            stack.append(routes[top][-1])               #갈수 있는 공항 중 마지막 공항(알파벳에서 가장 앞서는 부분)
            routes[top] = routes[top][:-1]              #stack에 저장해준 값을 routes내에서 지움.(pop를 사용해도 됨)
            #=routes[top].pop(-1)

    return path[::-1]                                   #stack에서 pop은 마지막 수 부터 제거되기에 path는 방문 반대로 저장되어 있음(역순으로 return)

t=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(t))