student_score = int(input())
max_score = int(input())


def calculate_percentage(student_score, max_score):
    percentage = student_score / max_score * 100
    return percentage


def assign_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage < 60:
        return "F"


print(assign_grade(calculate_percentage(student_score, max_score)))
