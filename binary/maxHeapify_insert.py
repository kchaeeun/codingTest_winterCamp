class MaxHeap:                          #제일 큰 값이 인덱스 앞 쪽에 위치 (배열 큐라 생각)
                                        #index를 내가 찾아서 구해야함
    def __init__(self):
        self.data = [None]


    def insert(self, item):                             #배열에 item값을 먼저 넣어두고, 힙 과정 시작!    
        index = len(self.data)                          #루트노드는 인덱스 1
        self.data.append(item)
        
        while (index // 2) > 0:                         
            parent = index // 2
            if item > self.data[parent]:    #why? self.data[index] 대신 item을 사용할 수는 없을까?
                                            #item이 교환으로 인해 정확히 리스트내 어느 인덱스에 위치해 있는지 알기 어려움 -> 리스트 내 교환을 위해 필요                                                 
                self.data[parent], self.data[index] = self.data[index], self.data[parent]
                index = parent                          #index가 item의 바뀌는 위치를 알려주기 때문에 item대신 self.data[index]로 비교
            else:
                break
            
                
def solution(x):
    return 0