eng = int(input("Enter the Marks of English out of 100: "))
maths = int(input("Enter the Marks of Maths out of 100: "))
sci = int(input("Enter the Marks of Science out of 100: "))
Hist = int(input("Enter the Marks of History out of 100: "))
lang = int(input("Enter the Marks of Language out of 100: "))

result = int(eng + maths + sci + Hist + lang)/5

print(result)
if (result >= 40)and(result <= 50):
    print(f"Grade D")
elif (result >= 50 )and(result <= 70):
    print(f"Grade C")
elif(result >=70)and(result <= 80):
    print(f"Grade B")
elif(result >=80):
    print(f"Grade A")
else: 
    print(f"You are Fail")
