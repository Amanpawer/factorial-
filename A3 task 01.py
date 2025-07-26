def factorial(a):
  if a<2:
    return 1
  else:
    return a*(factorial(a-1))
result=factorial(int(input("enter your number for factorial: ")))
print("factorial of your number is :  ",result)