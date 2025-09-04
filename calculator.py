print(" + - Add")
print(" - - subtract")
print(" * - multiply")
print(" // - divide")
option=str(input("choose an operation:"))

if(option in ['+','-','*','//']):

    num1= int(input("enter first number: "))
    num2= int(input("enter second number: "))

    if(option == '+'):
        result = num1 + num2
    elif(option == '-' ):
            result = num1 - num2
    elif(option == '*' ):
            result = num1 * num2
    elif(option == '//' ):
            result = num1// num2
   
else:
   print("invalid operation entered")

print("the result of the operation is {}".format(result))
