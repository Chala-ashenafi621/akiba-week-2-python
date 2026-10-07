# TASK 15 — SUM OF DIGITS
nums = int(input("Enter the digits: "))
sum_digit = 0
while nums > 0:
    digit = nums % 10
    sum_digit += digit
    nums //= 10
print("The sum of the digits is:", sum_digit)
