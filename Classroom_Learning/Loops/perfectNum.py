#Print all perfect Numbers between 1 and 500. A perfect number equals the sum of its proper divisions
for n in range(1,500):
    div_sum = 0
    for d in range(1,n):
        if n % d == 0:
            div_sum += d
    if div_sum==n:
        print(n,end=" ")