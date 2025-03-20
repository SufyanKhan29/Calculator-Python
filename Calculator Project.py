# "Calculator"

print(f"1: Add")
print(f"2: Sub")
print(f"3: Multi")
print(f"4: Div")

run=True
while run:

    def addition():
        sum=usernum1+usernum2
        return sum

    def subtraction():
        remain=usernum1-usernum2
        return remain
        
    def multiplication():
        product=usernum1*usernum2
        return product

    def division():
        end=usernum1/usernum2
        return end

    user_choice=int(input("Choose any of the above operation : "))
    usernum1=int(input("Enter your first value : "))
    usernum2=int(input("Enter your second value : "))

    if user_choice == 1:
        print(addition())
    elif user_choice== 2:
        print(subtraction())
    elif user_choice== 3:
        print( multiplication())       
    elif user_choice == 4:
        print(division())  

    exit=input("Type 'yes' to terminate the program or type 'no' to continue : ")
    if exit.lower() == 'yes':
        run=False
print("Thanks for using calculator , Goodbye")
    
      


