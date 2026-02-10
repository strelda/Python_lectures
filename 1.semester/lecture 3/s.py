x, y = 16, 24

while y > 0:
    x, y = y, x%y

print(x)