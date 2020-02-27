def getX(A, b, n):
    r = (1 + b) ** n
    return A * r * b / (r - 1)

A = 430000
b = 5.635 / 12 / 100
n = 360

print(getX(A, b, n))
