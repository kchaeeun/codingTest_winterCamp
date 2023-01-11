letters=['a','b','c']

for i in range(1 << len(letters)):
    selected=[]
    for j in range(len(letters)):
        if i & (1<<j):
            #print(letters[j])
            selected.append(letters[j])

    print(selected)
