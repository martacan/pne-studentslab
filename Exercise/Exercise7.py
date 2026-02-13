student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}

print("Name: ", student["name"] )
print("Number of subjects: ", len(student["subjects"]))

def pne_in():

    if "PNE" in student["subjects"]:
        result = True
    else:
        result = False
    return result

print("Enrolled in PNE: ", pne_in())

print("Databases grade: ", student["grades"]["Databases"])

def average():
    result = round(sum(student["grades"].values())/ len(student["grades"]), 2)
    return result
print("Average grade: ", average())

for key, value in student["grades"].items():
    print(key, value)
