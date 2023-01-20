data=[0,20,6,12,2,4]
index = len(data)
item = 30#루트노드는 인덱스 1
data.append(item)
while (index // 2) > 0:                         
    parent = index // 2
    if item> data[parent]:    #why? self.data[index] 대신 item을 사용할 수는 없을까?
                                            #고정값인 item이 변하는 것이지 변동하는 리스트의 값이 변하는 것이 아니기 때문에 기존 위치에 있는 item값이 리스트 맨 끝에 남아 있을 것!                                               
        data[parent], data[index] = data[index], data[parent]
        index = parent                          #index가 item의 바뀌는 위치를 알려주기 때문에 item대신 self.data[index]로 비교
    else:
        break
print(data)