names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
scores = [92, 78, 95, 84, 67]

grade_book = dict(zip(names, scores))
float_scores = map(float, grade_book.values())

total_score = 0
for score in float_scores:
    total_score += score

average = total_score / len(grade_book)
print(f"Class Average: {average:.2f}")

top_student = max(grade_book, key=grade_book.get)
bottom_student = min(grade_book, key=grade_book.get)

print(f"Top Scorer: {top_student} ({grade_book[top_student]})")
print(f"Bottom Scorer: {bottom_student} ({grade_book[bottom_student]})")

search_name = input("\nEnter a student's name to look up their grade: ").strip()
result = grade_book.get(search_name, f"Sorry, '{search_name}' was not found in the grade book.")

{result}
