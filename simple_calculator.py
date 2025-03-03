# sub = x - y
# print("x - y == ", sub)
# product = x * y
# print("x * y == ", product)
# div = x / y
# print("x / y == ", div)
# mod = x % y
# print("x % y == ", mod)

# choice = int(input("Enter Choice: "))
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))

# if choice == 1:
#     sum = x + y
#     print("x + y == ", sum)
# elif choice == 2:
#     sub = x - y
#     print("x - y == ", sub)
# elif choice == 3:
#     product = x * y
#     print("x * y == ", product)
# elif choice == 4:
#     div = x // y
#     print("x // y == ", div)
# elif choice == 5:
#     mod = x % y
#     print("x % y == ", mod)
# else:
#     print("Please! Enter the correct Choice")



option =int(input("Enter option: "))
x = int(input("Enter x: "))
y = int(input("Enter y: "))

def simple_ca(x,y):
    # addition function 
    if option == 1:
        sum = x + y 
        print("x + y == ", sum)
    elif option == 2: 
        #subtraction function
        sub = x - y 
        print("x - y == ", sub)
    elif option == 3:
        # multiplication function
        product = x * y 
        print("x * y == ", product)
    elif option == 4:
        # integer division function
        div = x // y 
        print("x // y == ", div)
    elif option == 5:
        # float-division function 
        float_div = x / y
        print("x / y == ", float_div)
    elif option == 6:
        #modulus function
        module = x % y 
        print("x % y == ", module)
    elif option == 7:
        # average function
        avr = (x + y)/2
        print("(x + y)/2 == ")
    elif option == 8:
        # to display larger number 
        if x > y:
            print(" x is larger")
        else:
            print("y is larger")
    elif option == 9:
        # to display odd or even number 
        if x % 2 == 0:
            print("x is even")
        else:
            print("x is odd")
    elif option == 10:
        # factorial function
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)
        n = int(input("Enter n: "))
        N = factorial(n)
        print(N)
    else: 
        print("Unexpected option")
simple_ca(x,y)
