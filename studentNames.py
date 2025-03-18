
studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]
for name in studentNames:
    print(name + " Evans")
new_name = input("Please enter another name to add to the list: ")
studentNames.append(new_name)
print("\nUpdated list of student names:")
for name in studentNames:
    print(name + " Evans")
