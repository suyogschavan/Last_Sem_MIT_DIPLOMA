
# #  ---------1-------------
# def a():
#     for i in range (4):
#         for j in range(i):
#             print("*", end="")
#         print("*")

# a()
    
# ----------2--------------
def b():
    i = 4
    for i in range (4, -1): 
        while (i>1):
            print("#", end="")
            i = i - 1
        print("*")

b()

# ----------3--------------
# def c():
#     for i in range(5):
#         for j in range(i):
#             print("*", end="") 
#         print("1")
# c() 