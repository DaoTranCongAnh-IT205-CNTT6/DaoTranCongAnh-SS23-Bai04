from datetime import datetime

from colorama import Fore, Style

from ulits.score_utils import (
    calculate_average,
    classify_student
)


def display_student_scores(records):

    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("\n--- DANH SÁCH ĐIỂM SINH VIÊN ---")

    for index, student in enumerate(records, start=1):

        average = calculate_average(
            student["scores"]
        )

        rank = classify_student(average)

        print(
            f"{index}. "
            f"[{student['student_id']}] "
            f"{student['name']} | "
            f"Điểm: {student['scores']} | "
            f"ĐTB: {average:.2f} - {rank}"
        )

    print("---------------------------------")


def export_learning_report(records):

    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    total_students = len(records)

    passed = 0
    failed = 0

    for student in records:

        average = calculate_average(
            student["scores"]
        )

        if average >= 5:
            passed += 1
        else:
            failed += 1

    report_time = datetime.now()

    with open(
        "learning_report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            f"REPORT TIME: {report_time}\n"
        )

        file.write(
            f"TOTAL STUDENTS: "
            f"{total_students}\n"
        )

        file.write(
            f"PASSED: {passed}\n"
        )

        file.write(
            f"NEED IMPROVEMENT: {failed}\n"
        )

    print("\n--- XUẤT BÁO CÁO HỌC TẬP ---")
    print(f"Tổng số sinh viên: {total_students}")
    print(f"Số sinh viên đạt yêu cầu: {passed}")
    print(f"Số sinh viên cần cải thiện: {failed}")

    print(">> Đã xuất báo cáo ra file learning_report.txt" )