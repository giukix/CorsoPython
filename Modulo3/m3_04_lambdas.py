#High order function
def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))


# Pure function
def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)


# Lambda
def my_func(f, arg):
  return f(arg)

my_func(lambda x: 2*x*x, 5)


x = lambda price, count :  price * count
print(x(2,10))


########## MAP ############
def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

######### FILTER #######
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)
