#Return a single vlaue

# def square(n):
#     return n ** 2

# #Return multiple vlaues (tuple unpacking)
# def min_max(nums):
#     return min(nums), max(nums)

#Return ends the function immediately
def check_age(age):
    if age < 0:
        return "Invalid age"
    if age < 18:
        return "Minor"
    return "Adult"