n = 49

# find the smallest divisor of the number n
d = 2
while d < n:
    if n%d == 0:
        print(n, "can be divided by", d)
        break
    d += 1  
else:
    print(n, "is prime")