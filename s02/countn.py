#function for calculating the sum of n terms
def sumn(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res
print("the sum of the first 20 integer numbers", sumn(20))
print("the sum of the first 100 integer numbers", sumn(100))


