# num2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = []
# print("List : ",num2)

# for i in range(len(num2)):
#     if num2[i] % 2 == 0:
#         even.append(num2[i])

# print("even numbers in the list : ", even)

def add(*a):
    total = 0
    for i in a:
        total = total +i
    print(total)


add(1, 5, 3, 4, 5, 6, 7, 8, 9, 10)