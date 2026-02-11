temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]

print("Wednesday: ", temperatures[2])
def max_temp():
    max = 0
    for t in temperatures:
        if t >= max:
            max = t
    return max
print("Max: ", max_temp())

def min_temp():
    min = None
    for t in temperatures:
        if min == None or t <= min:
            min = t
    return min
print("Min: ", min_temp())
average = sum(temperatures)/ len(temperatures)
print("Average: ", round(average , 1))

def days_adove():
    count = 0
    temp = 17
    for t in temperatures:
        if t >= temp:
            count += 1
    return count
print("Days Adove: ", days_adove())

print("Sorted: ", sorted(temperatures))