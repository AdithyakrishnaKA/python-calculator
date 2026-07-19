count=int(input("number of numbers to be entered:"))
if count ==2:
 a=float(input("enter the first number:"))
 b=float(input("enter the second number:"))
else:
   print("error : only two numbers are allowed")

operator=input("enter the operator (+,-,*,/):")

if operator=="+":
    print("result:",a+b)
elif operator=="-":
     print("result:",a-b)
elif operator=="*":
     print("result:",a*b)
elif operator=="/":
    if b==0:
     print("error: division by zero is not allowed")
    else:
     print("result:",a/b)
else:
     print("error: invalid operator")