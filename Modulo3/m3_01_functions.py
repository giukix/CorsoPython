def my_func():
    print("spam")
    print("spam")
    print("spam")

my_func()

print("*******************")

def print_with_exclamation(word):
   print(word + "!")
    
print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")

print("*******************")

def print_sum_twice(x, y):
   print(x + y)
   print(x + y)

print_sum_twice(5, 8)

print("*******************")

def max(x, y):
    if x >=y:
        return x
    else:
        return y
        
print(max(4, 7))
z = max(8, 5)
print(z)

### Functions as objects
def multiply(x, y):
    return x * y

a = 4
b = 7
operation = multiply
print(operation(a, b))

### Functions as arguments

def add(x, y):
    return x + y

def do_twice(func, x, y):
    return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b))

#outer function
def outer_function():
    print("Hello from the outer function")

    #inner function
    def inner_function():
        print("Hello from the inner function")

    inner_function()

outer_function()

###### DECORATOR
def uppercase(func):
    def wrapper():
        orig_message = func()
        modified_message = orig_message.upper()
        return modified_message
    return wrapper

@uppercase
def greet():
    return "Welcome!"

# Using the decorated function
print(greet())

########## args e kwargs ###########
def total(*args):
  result = 0
  for arg in args:
    result += arg
  return result

print(total(1, 2, 3, 4, 5))
print(total(1, 2, 3, 4, 5, 6, 7))
print(total(1, 2, 3))

def show_items(category, *items):
  print("Category: " + category)
  for item in items:
    print(item)

show_items("Electronics", "Laptop", "Smartphone", "Tablet")

##### **kwargs is a dictionary
def display_info(**kwargs):
  #kwargs.items() returns the key:valie pairs
  for key, value in kwargs.items():
    print(key, ":", value)

display_info(name="Alice", age=30, city="New York")