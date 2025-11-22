import csv
def get_assignment_name():
    while True:
        name = input("Enter Assignment Name: ").strip()
        if name:
            return name
        print("Assignment name cannot be empty.")


def get_category():
    while True:
        category = input("Enter Category (FA/SA): ").strip().upper()
        if category in ["FA", "SA"]:
            return category
        print("Invalid category! Must be FA or SA.")


def get_grade():
    while True:
        try:
            grade = float(input("Enter Grade (0-100): "))
            if 0 <= grade <= 100:
                return grade
            print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Grade must be a number.")


def get_weight():
    while True:
        try:
            weight = float(input("Enter Weight (positive number): "))
            if weight > 0:
                return weight
            print("Weight must be a positive number.")
        except ValueError:
            print("Invalid input! Weight must be a number.")


assignments = []

print("----- Grade Generator Calculator -----")

while True:
    print("\nEnter Assignment Details:")
    name = get_assignment_name()
    category = get_category()
    grade = get_grade()
    weight = get_weight()

    assignments.append({
        "Assignment": name,
        "Category": category,
        "Grade": grade,
        "Weight": weight
    })

    more = input("Add another assignment? (y/n): ").strip().lower()
    if more != 'y':
        break

# Calculations
total_FA = sum((a["Grade"] / 100) * a["Weight"] for a in assignments if a["Category"] == "FA")
total_SA = sum((a["Grade"] / 100) * a["Weight"] for a in assignments if a["Category"] == "SA")

final_grade = total_FA + total_SA
gpa = (final_grade / 100) * 5.0

# Pass/Fail Logic
FA_weight_total = sum(a["Weight"] for a in assignments if a["Category"] == "FA")
SA_weight_total = sum(a["Weight"] for a in assignments if a["Category"] == "SA")

required_FA = FA_weight_total * 0.5
required_SA = SA_weight_total * 0.5

passed_FA = total_FA >= required_FA
passed_SA = total_SA >= required_SA

status = "PASS" if passed_FA and passed_SA else "FAIL"

# Console Summary
print("\n------ FINAL SUMMARY ------")
print(f"Total Formative Score: {total_FA:.2f} / {FA_weight_total}")
print(f"Total Summative Score: {total_SA:.2f} / {SA_weight_total}")
print(f"Final Grade: {final_grade:.2f}%")
print(f"GPA Equivalent: {gpa:.2f}")
print(f"Status: {status}")

print("\nAssignments Entered:")
for a in assignments:
    print(f"- {a['Assignment']} ({a['Category']}): Grade={a['Grade']}, Weight={a['Weight']}")

# Generate CSV
with open("grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Assignment", "Category", "Grade", "Weight"])
    for a in assignments:
        writer.writerow([a["Assignment"], a["Category"], a["Grade"], a["Weight"]])

print("\ngrades.csv has been created successfully!")
