num1 = 7
num2 = 0
#print(num1/num2)

try:
    print (num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occurred")
    print("due to zero division")

##############################

try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Error occurred")    

##############################

try:
    word = "spam"
    print(word / 0)
except: # Cattura tutti gli errori
    print("An error occurred")    

##############################
# finally #
try:
    print("Hello")
    print(1 / 0)
except ZeroDivisionError:
    print("Divided by zero")
finally:
    print("This code will run no matter what")    


##############################
# RAISE #
name = "123"
raise NameError("Invalid name!")    