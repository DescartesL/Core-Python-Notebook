while(True):
    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program")
    user_input = input(": ")
    if user_input=='quit':
        break
    elif user_input =='add':
        num1 = float(input('please input a num:'))
        num2 = float(input('please input another num:'))
        result = str(num1+num2)
        print('the result is '+result)
    elif user_input=='subtract':
        num1 = float(input('please input a num:'))
        num2 = float(input('please input another num:'))
        result = str(num1-num2)
        print('the result is '+result)
    elif user_input=='multiply':
        num1 = float(input('please input a num:'))
        num2 = float(input('please input another num:'))
        result = str(num1*num2)
        print('the result is '+result)
    elif user_input =='divide':
        num1 = float(input('please input a num:'))
        num2 = float(input('please input another num:'))
        if num2==0:
            print(' num2 can\'t be 0' )
        else:
            result = str(num1/num2)
            print('the result is '+result)