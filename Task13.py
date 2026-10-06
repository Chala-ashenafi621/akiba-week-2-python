#TASK 13 — PRIME NUMBER CHECKER
number=int(input("Enter the number:"))
if number<2:
    print("The number is not prime")
else:
    pr=True
    # We do not need to check 1 because every number
    # is divisible by 1. We also do not need to check
    # the number itself because every number is divisible by itself.
    for i in range(2,number):
        if number%i==0:
            pr=False
            break
    if pr is True:
        print("The number is prime")
    else:
        print("The number is not prime")