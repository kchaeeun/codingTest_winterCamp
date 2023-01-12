numbers=[2,4,123,45,67]
numbers.sort(key=lambda x : (x*4)[:4], reverse=True) #앞에서 부터 4글자까지 끊어냄, 내림차순(큰 것 우선으로)

