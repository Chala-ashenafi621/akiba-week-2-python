# TASK 12 — LARGEST OF THREE
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

if first_number == second_number and second_number == third_number:
    print("All three numbers are equal.")
elif first_number == second_number and first_number > third_number:
    print("The first and second numbers are equal and largest.")
elif first_number == third_number and first_number > second_number:
    print("The first and third numbers are equal and largest.")
elif first_number > second_number and first_number > third_number:
    print("The largest number is:", first_number)

elif second_number > first_number and second_number > third_number:
    print("The largest number is:", second_number)

elif third_number > first_number and third_number > second_number:
    print("The largest number is:", third_number)

elif second_number == third_number and second_number > first_number:
    print("The second and third numbers are equal and largest.")