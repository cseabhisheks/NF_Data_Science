# 1. Write a program to check whether a year is a leap year or not. 
year=2030
if (year%4==0 and (year%100!=0 or year%400==0 )):
    print("leap year")
else:
    print("not leap year")
# 2. Write a program to find the largest among three numbers using nested conditional statements. 
x=41
y=5
z=41
if x>y and x>z:
    print("largest is :",x)
    if x<z:
        print("largesr is: ",z)
else:
    if y>z:
        print("largest is: ",y)
    else:
        print("largest is:",z)
# 3. Write a program to check whether a character is an uppercase letter, lowercase letter, digit, or special character. 
char='Sad234235'
if char>='a' and char<='z':
    print("lowercase letter")
elif char>='0' and char<='9':
    print("digit")
elif char>='A' and char<='Z':
    print("uppercase letter")
else:
    print("special character")
# 4. Write a program to calculate electricity bill using different unit slabs. 
slab1=5
slab2=7
slab3=10
unit=456
if unit<=100:
    print(f"total bill is {unit}*{slab1}={unit*slab1}")
elif unit<=200:
    t1=100*slab1
    t2=(unit-100)*slab2
    print(f"total bill is {100}*{slab1}+{(unit-100)}*{slab2}={t1+t2}")
else:
    t1=100*slab1
    t2=(unit-100)*slab2
    t3=(unit-200)*slab3
    print(f"total bill is {100}*{slab1}+{(unit-100)}*{slab2}+{(unit-200)}*{slab3}={t1+t2+t3}")

# 5. Write a program to determine whether a triangle is Equilateral, Isosceles, or Scalene. 
s1=5
s2=6
s3=5
if s1==s2 and s2==s3:
    print("equilaterial triangle")
elif s1==s2 or s2==s3 or s1==s3:
    print("isosceles triangle")
else:
    print("scalene triangle")
# 6. Write a program to create a simple calculator using if-elif-else. 
operand1=3
opearnd2=8
operator='*'
if operator=='+':
    print("sum: ",operand1+opearnd2)
elif operator=='-':
      print("sub: ",operand1-opearnd2)
elif operator=='*':
      print("product: ",operand1*opearnd2)
elif operator=='/':
      print("div: ",operand1/opearnd2)

# 7. Write a program to calculate income tax according to salary ranges. 

# 8. Write a program to check login authentication using username and password conditions. 
# 9. Write a program to determine whether a point lies in First quadrant, Second quadrant, Third 
# quadrant, Fourth quadrant, On axis, or At origin. 
x=-5
y=-4
if x==0 and y==0:
    print('origin')
elif x==0 or y==0:
    print('axis')
elif x>0 and y>0:
    print('first quadrant')
elif x<0 and y>0:
    print('second quadrant')
elif x<0 and y<0:
    print('third quadrant')
else:
    print("fourth quadrant")
# 10. Write a program to assign grades based on marks and display distinction for high scores. 