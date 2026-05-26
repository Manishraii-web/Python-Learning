# Part 1/2
#Function that proccesses a list
def find_evens(numbers):
    evens = []
    for n in numbers:
       if n % 2 == 0:
           evens.append(n)
    return evens

#FUnctiom that builds a multiplication table
def times_table(n, limit=10):
    result = []
    for i in range(1,limit+1):
        result.append(f"{n} * {i} = {n*i}")
    return result

#2/2
#function to flatten nested list (AI data use)

def flatten(nested):
    flat = []
    for sublist in nested:
        for item in sublist:
            flat.append(item)
    return flat

data = [1,2,3,4,5,6,7,8,9,10]
matrix = [[1,2,3],[4,5,6],[7,8,9,]]

print(find_evens(data))
print(times_table(3,5))
print(flatten(matrix))