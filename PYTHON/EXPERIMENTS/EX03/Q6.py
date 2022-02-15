# write a program to calculate surface volume and area of a cylinder

hight = int(input("Enter the hight of the cylinder: "))
r = int(input("Enter the radius of the cylinder: "))

pi = 3.14
Area = pi*r*r
Volume = pi*r*r*hight

print(f'''Area of the cylinder : {round(Area,2)}
Volume of the cylinder : {round(Volume, 2)} \n''' )
