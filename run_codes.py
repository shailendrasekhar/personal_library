from pl import *
m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))
print("Sum of {} and {} = {}".format(m,n,add(m,n)))
print("Difference of {} and {} = {}".format(m,n,sub(m,n)))
print("Product of {} and {} = {}".format(m,n,mul(m,n)))
print("Quotient of {} and {} = {}".format(m,n,quo(m,n)))
print("Integer Quotient of {} and {} = {}".format(m,n,quo_int(m,n)))
print("Remainder of {} and {} = {}".format(m,n,rem(m,n)))
print("{} to the power {} = {}".format(m,n,pow(m,n)))
print("Greatest Common Divisor of {} and {} = {}".format(m,n,euclid_algorithm(m,n)))