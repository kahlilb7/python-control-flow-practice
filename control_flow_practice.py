"""
Python Control Flow Practice

This program demonstrates core Python concepts including loops,
conditionals, and basic data processing through several small tools.

Features:
- Collatz sequence generator
- Prime number checker
- Multiplication table
- Statistics dashboard

Author: Kahlil Batieste
"""

# --- Collatz Sequence ---

while True:
    try:
        start_number = int(input("Enter starting number: "))
        break
    except ValueError:
        print("Please enter a valid number.")


current = start_number
steps = 0

print("Sequence:", current, end=" ")

while current != 1:
    if current % 2 == 0:
        current = current // 2
    else:
        current = 3 * current + 1

    print(current, end=" ")
    steps += 1

print()
print("Steps:", steps)

# --- Prime Number Checker ---

number = int(input("Enter a number: "))

print(f"Testing divisors from 2 to {number - 1}...")

is_prime = True
first_divisor = 0

for divisor in range(2, number):
    if number % divisor == 0 and first_divisor == 0:
        is_prime = False
        first_divisor = divisor

if is_prime:
    print(f"{number} is prime!")
else:
    print(f"{number} is not prime (divisible by {first_divisor})")


# --- Multiplication Table ---

print("Multiplication Table:")

print("  ", end="")
for col in range(1, 11):
    print(f"{col:4}", end="")
print()

for row in range(1, 11):
    print(f"{row:2}", end="")
    for col in range(1, 11):
        product = row * col
        print(f"{product:4}", end="")
    print()


# --- Statistics Dashboard ---
print("=== Statistics Dashboard ===")
print("Enter positive numbers (enter -1 to finish):")

numbers = []
count = 0
total = 0
minimum = 0
maximum = 0

while True:
    user_input = int(input("Enter number: "))

    if user_input == -1:
        break

    numbers.append(user_input)
    count += 1
    total += user_input

    if count == 1:
        minimum = user_input
        maximum = user_input
    else:
        if user_input < minimum:
            minimum = user_input
        if user_input > maximum:
            maximum = user_input

print()
print("=== Statistics ===")

average = total / count

labels = ["Count", "Sum", "Average", "Minimum", "Maximum"]
values = [f"{count} numbers", total, f"{average:.1f}", minimum, maximum]

for i in range(len(labels)):
    print(f"{labels[i]}: {values[i]}")

print()
print("=== Bar Chart ===")

for number in numbers:
    print(f"{number}: ", end="")
    for i in range(number):
        print("*", end="")
    print()
