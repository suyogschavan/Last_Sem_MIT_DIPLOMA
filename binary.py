num = int(input("Enter the number : "))

arr = []

# 8 bit system 

if(num>= 128):  
    num = num - 128
    arr.append(1)
else: #
    arr.append(0)
if(num>=64):
    num = num - 64
    arr.append(1)
else: #
    arr.append(0)
if(num>=32):
    num = num - 32
    arr.append(1)
else: #
    arr.append(0)
if(num>=16):
    num = num - 16
    arr.append(1)
else: #
    arr.append(0)
if(num>=8):
    num = num - 8
    arr.append(1)
else: #
    arr.append(0)
if(num>=4):
    num = num - 4
    arr.append(1)
else: #
    arr.append(0)
if(num>=2):
    num = num - 2
    arr.append(1)
else: #
    arr.append(0)
if(num>=1):
        num = num - 1
        arr.append(1)
else: #
    arr.append(0)

print (arr)