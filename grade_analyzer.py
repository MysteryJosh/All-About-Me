
scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]

a_count = 0
b_count = 0
c_count = 0
d_count = 0
f_count = 0


for score in scores:
    if score >= 90:
        a_count += 1
    elif score >= 80:
        b_count += 1
    elif score >= 70:
        c_count += 1
    elif score >= 60:
        d_count += 1
    else: 
        f_count += 1


#Calculation
total = len(scores)
average = sum(scores) / total
highest = max(scores)
loweset = min(scores)

passing = 0
failing = 0

for score in scores:
    if score >= 60:
        passing += 1
    else:
        failing += 1


#Display
print("===== Grade Analyzer =====")
print(f"Total scores: {total}")
print(f"Average score: {average:.1f}")
print(f"Highest score: {highest}")
print(f"Lowest score: {loweset}")
print(f"Passing scores: {passing} (80.0%)")
print(f"Failing scores: {failing} (20.0%)")

print("\nGrade Distribution:")
print(f"A: {a_count} students")
print(f"B: {b_count} studnets")
print(f"C: {c_count} students")
print(f"D: {d_count} students")
print(f"F: {f_count} students\n")

#Add a score


while True:
    add_score = input("Enter a score (or 'done' to finish): ")
    if add_score.lower() == "done":
        break 
    try:
        new_score = float(add_score)
        scores.append(new_score)
        new_average = sum(scores) / len(scores)
        print(f"\nUpdated Average: {new_average:.1f}")
        continue
    except ValueError:
        print("Enter a number or type 'done'.")
        break


print(f"\nFinal Average: {sum(scores) / len(scores):.1f}")
        

        



