
def calculator(num1 ,num2):

    op = input("Please select the Arithmetic Operator among these : (+) (-) (*) (/) (**) (%)")
    if(op == "+"):
        result = num1 + num2
    elif(op == "-"):
        result = num1 - num2
    elif (op == "*"):
        result = num1 * num2
    elif(op == "**"):
        result = num1 ** num2
    elif(op == "%"):
        result = num1 % num2
    elif(op == "/"):
        if(num2 == 0):
            result ="infinte"
        else:
            result = num1 / num2
    else:
        result = "--------Invalid Input---------"

    return result

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
result =calculator(num1, num2)
print()
print()
print(result)
print()
print()

while (True):
    print("OPTION - 1 : Perform calculation for 2 different numbers other than previous numbers --  ")
    print("OPTION - 2 : Perform calculation for same numbers --  ")
    print("OPTION - 3 : Perform calculation on calculated result --  ")
    print("OPTION - 4 : Perform calculation for 1 different number and 1 same number  --  ")
    print("OPTION - 5 : close the calculator")
    print()
    print()
    n=int( input("Choose the correct option "))
    if n==1:
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
        result=calculator(num1,num2 )

    if n==2:
        result=calculator(num1,num2 )

    if n==3:
        print("OPTION - a : number 1 =  calculated result ")
        print("OPTION - b : number 2 =  calculated result ")
        x=input("Choose the correct option ")
        if(x== "a") :
            num2=int ( input("Enter the second number : "))
            result=calculator(result,num2 )

        elif(x== "b") :
            num1=int ( input("Enter the first number : "))
            result=calculator(num1,result)
    if n==4:
        print("OPTION - a : number 1 =  same ")
        print("OPTION - b : number 2 =  same ")
        x=input("Choose the correct option ")
        if(x== "a") :
            num2=int ( input("Enter the second number : "))
            result=calculator(num1,num2 )

        elif(x== "b") :
            num1=int ( input("Enter the first number : "))
            result=calculator(num1,num2 )

    if n == 5:
        print("-----THANK YOU user for using the computer---")
        print()
        print()
        print("-----shuting down-----")
        print(" ----shuting down----")
        print("  ---shuting down---")
        print("   --shuting down--")
        print("    -shuting down-")
        print("shuting down")
        break
    print(result)
    print()
    print()

