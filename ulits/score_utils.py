def calculate_average(scores):
    if not scores:
        return 0

    valid_scores = [
        score for score in scores
        if isinstance(score, (int, float))
    ]

    if not valid_scores:
        return 0

    return sum(valid_scores) / len(valid_scores)


def classify_student(average):
    if average >= 8:
        return "Giỏi"
    elif average >= 6.5:
        return "Khá"
    elif average >= 5:
        return "Trung bình"
    else:
        return "Yếu"