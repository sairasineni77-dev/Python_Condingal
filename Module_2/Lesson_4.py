# Recursive
def factorial_1(x):
  """this is a recursive function"""

  if x==0 or x==1:
   return 1
  else:
   return x*factorial_1(x-1)

print("the factorial of 1:", factorial_1(1))
print("the factorial of 2:", factorial_1(2))
print("the factorial of 5:", factorial_1(5))
print("the factorial of 10:", factorial_1(10))