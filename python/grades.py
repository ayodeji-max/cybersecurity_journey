Students =["Ayodeji", "Tunde", "Chidi", "Emeka"]
grades = [85, 92, 78, 65]

print("Student Results:")
for i in range(len(Students)):
    print(f"{Students[i]} - {grades[i]}%")

print(f"\nClass average: {sum(grades) / len(grades):.1f}%")
print(f"Highest grade: {max(grades)}%")
print(f"Lowest grade: {min(grades)}%")
