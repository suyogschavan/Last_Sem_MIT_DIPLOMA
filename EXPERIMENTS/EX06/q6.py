list5 = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]

for i in range(len(list5)):
    if list5[i] == list5[i-1]:
        print("Common item in list : ",list5[i])
        break
    i = i + 1