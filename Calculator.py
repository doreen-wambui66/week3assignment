num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation(+,-,/,*): ")

if operation =="+":
    results = num1 + num2
    print(f"{num1} +{num2} ={results}")  
elif operation == "-": 
    results = num1 - num2 
    print(f"{num1}-{num2}={results}")
   
elif operation == "*":
    results = num1 * num2 
    print(f"{num1}*{num2}={results}")    
elif operation == "/":
   if num2 != 0:
    results = num1 / num2

    print(f"{num1}/{num2}={results}") 
   else:   
    print("Error: cannot divide by 0")
else:
    print("Invalid operation please enter +,-,/,*,")