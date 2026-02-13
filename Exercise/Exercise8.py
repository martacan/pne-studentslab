students = [
    {"name": "Ana", "grades": [8.5, 7.0, 9.0]},
    {"name": "Luis", "grades": [5.0, 4.5, 6.0]},
    {"name": "Maria", "grades": [9.5, 9.0, 10.0]},
    {"name": "Pedro", "grades": [3.0, 4.0, 2.5]},
    {"name": "Sofia", "grades": [7.0, 7.5, 8.0]},
]
def average():
    result = round(sum(grades)/ len(grades), 1)
    return result

def get_status():
    if avg >= 5:
        return "PASS"
    else:
        return "FAIL"
passed = 0
failed = 0
for student in students:
    name = student["name"]
    grades = student["grades"]
    avg = average()
    status = get_status()
    if status == "PASS":
        passed += 1
    else:
        failed += 1

    print(name, ":", avg, "-->", status)

print("Results", passed, "passed", failed, "failed")


