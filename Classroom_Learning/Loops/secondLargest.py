# Find second largest without sort() or max()

nums = [12, 45, 7, 89, 56, 34]

first = float("-inf")
second = float("-inf")

for n in nums:
    if n > first:
        second = first
        first = n

    elif n > second and n != first:
        second = n

print("Second largest:", second)