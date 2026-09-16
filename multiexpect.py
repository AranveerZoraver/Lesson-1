try:
    num1, num2 = eval(input("enter two numbers separated by a comma : "))
    
    result = num1 / num2
    print("result is", result )

except ZeroDivisionError:
    print("division by zero is not possible!!!!")

except SyntaxError:
    print("comma is missing, please enter a comma like this separated like this 1, 2")

except:
    print("wrong input")

else:
    print("no expectations")

finally:
    print("this will execute no matter what")