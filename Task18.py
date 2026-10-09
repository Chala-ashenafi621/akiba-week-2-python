#TASK 18 — COUNT NUMBERS
number = int(input("Enter the number: "))
even_number = 0
odd_number = 0
total = 0
for i in range(1, number + 1):
    if i % 2 == 0:
        even_number += 1
    else:
        odd_number += 1
    total += i
print("Even numbers:", even_number)
print("Odd numbers:", odd_number)
print("Sum of all numbers:", total)