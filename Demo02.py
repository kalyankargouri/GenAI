Number = list(map(int, input("Enter the list of numbers: ").split()))

even_count = 0
odd_count = 0

for num in Number:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Count of even numbers:", even_count)
print("Count of odd numbers:", odd_count)

