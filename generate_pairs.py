# Kuidas seda skripti käivitada:
# --------------------------------
# Käivita terminalis:
#     python generate_pairs.py
# Eeldab, et samas kaustas on olemas fail 'students.json'.
# Skript loob faili 'student_pairs.md' ja prindib paarid ka konsooli.

import json
import random

def load_students():
    with open('students.json', 'r') as file:
        data = json.load(file)
        return data['students']

def generate_review_circle(students):
    # Create a copy of the list to shuffle
    students_copy = students.copy()
    random.shuffle(students_copy)
    
    pairs = []
    # Create a circle where each student reviews the next student's code
    for i in range(len(students_copy)):
        reviewer = students_copy[i]
        # If it's the last student, they review the first student's code
        reviewee = students_copy[(i + 1) % len(students_copy)]
        pairs.append((reviewer, reviewee))
    
    return pairs

def format_pairs_markdown(pairs):
    markdown = "# Code Review Pairs\n\n"
    markdown += "Format: Reviewer -> Reviewee (reviewer vaatab reviewee koodi)\n\n"
    for i, (reviewer, reviewee) in enumerate(pairs, 1):
        markdown += f"{i}. {reviewer} -> {reviewee}\n"
    return markdown

def main():
    students = load_students()
    pairs = generate_review_circle(students)
    markdown = format_pairs_markdown(pairs)
    
    # Write to a markdown file
    with open('student_pairs.md', 'w') as file:
        file.write(markdown)
    
    # Also print to console
    print(markdown)

if __name__ == "__main__":
    main() 