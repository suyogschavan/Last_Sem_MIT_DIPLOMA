
tuple1 = (2, 3, 4, 2, 4, 5, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

for i in range(len(tuple1)):
    if tuple1[i] == tuple1[i-1]:
        print("Common item in list : ",tuple1[i])
        break
    i = i + 1
    
