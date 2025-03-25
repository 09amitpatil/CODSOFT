def calculator():
    while True:
        print("Select operation + , - , * , % , Exit ")
        choice=input("Enter choice: ").lower()

        if choice =="exit":
            print("Exiting calculator...")
            break

        try:
            num1=int(input("Enter 1st number: "))
            num2=int(input("Enter 2nd number: "))

            if choice=="+":
                print("Result: ",num1+num2)
            elif choice=="-":
                print("Result: ",num1-num2)
            elif choice=="*":
                print("Result: ",num1*num2)
            elif choice=="%":
                print("Result: ",num1%num2)
            else:
                print("Invalid operation !!!")
        except ValueError:
            print("Invalid input !!!")
    
calculator()