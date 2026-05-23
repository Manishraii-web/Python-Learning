nums = [ 3,1,4,1,5,9,2,6,5,1,5]
uniques=[]
for n in nums:
    if n not in uniques:
     uniques.append(n)
print(uniques)