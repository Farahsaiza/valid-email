import re

def number(number):
    n=re.match(r'\d{2}-\d{3}-\d{4}', number )
    if n :
        return True
    else:
        return False
   


num=str(input("enter a number"))
n=number(num)
if n == True:
    print("number is correct")
else:
    print("the number is incorrect")
