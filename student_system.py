import os

def add_student(students, name, age, grade):
    students.append({"name": name, "age": age, "grade": grade})

def average_grade(students):
    if not students:
        return 0
    return sum(s["grade"] for s in students) / len(students)

def best_student(students):
    if not students:
        return None
    return max(students, key=lambda s: s["grade"])

def failing_students(students, threshold):
    return [s for s in students if s["grade"] < threshold]

def group_by_age(students):
    groups = {}
    for s in students:
        age = s["age"]
        groups[age] = groups.get(age, 0) + 1
    return groups

def print_summary(students):
    if not students:
        print("No students to display.")
        return
    print("Name       Age  Grade")
    print("---------------------")
    for s in students:
        print(f"{s['name']:<10} {s['age']}   {s['grade']:.2f}")

def save_to_file(students, filename="students.txt"):
    try:
        with open(filename, "w") as f:
            for s in students:
                f.write(f"{s['name']},{s['age']},{s['grade']}\n")
        print("Data saved to", filename)
        print("Current working directory:", os.getcwd())
    except Exception as e:
        print("Error while saving:", e)

def load_from_file(filename="students.txt"):
    students = []
    try:
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    name, age, grade = parts
                    students.append({"name": name, "age": int(age), "grade": float(grade)})
        print("Data loaded from", filename)
    except FileNotFoundError:
        print("File", filename, "not found.")
    return students

def main():
    students = []
    while True:
        print("\n=== MENU ===")
        print("1. Add students")
        print("2. Show summary")
        print("3. Show best student")
        print("4. Show failing students")
        print("5. Save to file")
        print("6. Load from file")
        print("7. Exit")
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            while True:
                name = input("Name (type 'done' to stop): ")
                if name.lower() == "done":
                    break
                try:
                    age = int(input("Age: "))
                    grade = float(input("Grade: "))
                    add_student(students, name, age, grade)
                    print("Student added.")
                except ValueError:
                    print("Error: age and grade must be valid numbers.")
                    continue

        elif choice == "2":
            print("\n--- Sorted by grade (descending) ---")
            print_summary(sorted(students, key=lambda s: s["grade"], reverse=True))
            print("\n--- Sorted by name (alphabetical) ---")
            print_summary(sorted(students, key=lambda s: s["name"]))
            print("Average grade:", round(average_grade(students), 2))
            print("Number of students by age:", group_by_age(students))

        elif choice == "3":
            best = best_student(students)
            if best:
                print("Best student:", best["name"], "(Grade:", best["grade"], ")")
            else:
                print("No students available.")

        elif choice == "4":
            try:
                threshold = float(input("Failing threshold (e.g., 10): "))
                fails = failing_students(students, threshold)
                if fails:
                    print("Students below", threshold, ":")
                    for s in fails:
                        print("-", s["name"], "(", s["grade"], ")")
                else:
                    print("No failing students.")
            except ValueError:
                print("Error: please enter a valid number.")

        elif choice == "5":
            save_to_file(students)

        elif choice == "6":
            students = load_from_file()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1 and 7.")

if __name__ == "__main__":
    main()
