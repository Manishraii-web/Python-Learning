#Given a list of integers, count how many are even and how many are odd using a single foor loop
nums = [1,2,3,4,5,6,7,8,9]
even_count = 0
ood_count = 0
for n in nums:
    if n%2  == 0:
        even_count += 1
    else:
        ood_count += 1

print("Event count: ", even_count)
print("odd count: ", ood_count)