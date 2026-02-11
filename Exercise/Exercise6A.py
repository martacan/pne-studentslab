number = float(input("please enter a number: "))
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
is_even(number)
print("is_even", (number), "=", is_even(number))

