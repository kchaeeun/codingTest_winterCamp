V,E = map(int,input().split())

adj_matrix = [[0] * (V+1) for _ in range(V+1)]

for _ in range(E):
    start, end = map(int, input().split())
    adj_matrix[start][end]=1
    adj_matrix[end][start]=1
for i in range(V+1):
    print(adj_matrix[i])