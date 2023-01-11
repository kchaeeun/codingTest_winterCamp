def dfs(n):
    if n not in visited:
        visited.append(n)
    for dest in range(V+1):
        if adf_matrix[n][dest] and dest not in visited:
            dfs(dest)

V,E = map(int,input().split())

adf_matrix = [[0]*(V+1) for _ in range(V+1)]

for _ in range(E):
    start, end = map(int, input().split())
    adf_matrix[start][end]=1
    adf_matrix[end][start]=1

visited=[]

dfs(1)
print('이동순서:',visited)
