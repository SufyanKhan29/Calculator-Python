# "My Info"

# def info():
#     user_input=input("Enter your name")
#     print(f"My name is : {user_input}")
#     print("I am from Peshawar")
#     print("I belong from daudzai tribe")
#     print("I like to work on technical projects")

# info()    

# def total():
#     num1=int(input("Enter your value"))
#     num2=int(input("Enter your value"))
#     sum=num1+num2
#     print(sum)
    
# total()    



# Add two numbers and multiply them by 5 and divide the answer by 5.

# def addition(num1,num2):
#     sum=num1+num2
#     return sum

# def multiplication(sum):
#     product=sum*5
#     return product

# def division(product):
#     end=product/5
#     return end

# num1=int(input("Enter value"))
# num2=int(input("Enter value"))

# result=addition(num1,num2)
# product=multiplication(result)
# end=division(product)

# print(result)
# print(product)
# print(end)


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
    
      


