#Return a single vlaue

# def square(n):
#     return n ** 2

# #Return multiple vlaues (tuple unpacking)
# def min_max(nums):
#     return min(nums), max(nums)

#Return ends the function immediately
def check_age(age):
    
    age = 24
    if age < 0:
        return "Minor"
    if age < 18:
         return "Adult"