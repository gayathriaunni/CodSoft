'''Design a simple calculator with basic arithmetic operations. Prompt the user to input two numbers and an operation choice. Perform the 
calculation and display the result.'''

n1 = int(input())
n2 = int(input())


print("Select Operation:")
print("\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division")
operation = input("Enter the operation to be performed: ")

if operation== "1":
    print(n1+n2)
elif operation== "2":
    print(n1-n2)
elif operation== "3":
    print(n1*n2)
elif operation== "4":
    print(n1/n2)
