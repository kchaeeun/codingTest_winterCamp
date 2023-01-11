matrix = [[3, 7, 9],
		  [4, 2, 6],
		  [8, 1, 5]]

for r in range(3):
    for c in range(3):
        #if r > c: # r < c로 해도 됩니다.
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

for i in range(3):
    print(matrix[i])
# zip을 활용한 전치하기 => 원소가 튜플이 됩니다.
zipped_matrix = list(zip(matrix))
print(zipped_matrix) # [(3, 4, 8), (7, 2, 1), (9, 6, 5)]

# 전치 완료 후, 원소를 리스트로 활용하고 싶을 때
transposed_matrix = list(map(list, zip(matrix)))
print(transposed_matrix)
# [[3, 4, 8], [7, 2, 1], [9, 6, 5]]
# [1, 7, 5]
# [8, 3, 2]
# [4, 9, 6]