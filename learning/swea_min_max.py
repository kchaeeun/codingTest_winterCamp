T = int(input())
result=[]
#n1,n2,n3=map(int,input().split)
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
      cnt = int(input())
      #for i in range(1,cnt +1):
      n=list(map(int,input().split()))
      min=999999999
      max=0
      for i in n:   
            if min>i:
                  min=i
            if max<i:
                  max=i
      print(min,max)
      result.append(max-min)

for test_case in range(1, T + 1):
      print('#',test_case,result[test_case-1])
      