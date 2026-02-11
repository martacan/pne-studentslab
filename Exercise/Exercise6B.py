def classify_triangle(a, b, c):
    if a == b == c:
        result = ("Equilateral")
    elif a == b or b == c or a == c:
        result = ("Isosceles")
    else:
        result = ("Scalene")

    return result

a = int(input("Please enter the length of the first side: "))
b = int(input("Please enter the length of the second side: "))
c = int(input("Please enter the length of the third side: "))

print("classify_triangle", (a, b, c), "=", classify_triangle(a, b, c))