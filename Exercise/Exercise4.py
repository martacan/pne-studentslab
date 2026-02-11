flag = True
while flag:
    score = float(input("please enter a score: "))
    flag = False
def letter_find(score):

    if 9.0 <= score <= 10.0:
        letter = "A"

    elif 7.0 <= score <= 8.9:
        letter = "B"
    elif 5.0 <= score <= 6.9:
        letter = "C"
    elif 3.0 <= score <= 4.9:
        letter = "D"
    elif 0.0 <= score <= 2.9:
        letter = "F"

    return letter

letter = letter_find(score)


print("Score ", score, "->", letter)

