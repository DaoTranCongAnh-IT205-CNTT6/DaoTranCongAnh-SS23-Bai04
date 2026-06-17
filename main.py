from data.student import student_records
from ulits.random_utils import generate_assignment_code
import ulits.string_utils as string_utils
import ulits.show_students as report_generator

def main():
    while True:

        print('''===== HỆ THỐNG TIỆN ÍCH HỌC TẬP RIKKEI ACADEMY =====
        1. Xem danh sách sinh viên và điểm trung bình
        2. Chuẩn hóa tên sinh viên
        3. Sinh mã bài tập ngẫu nhiên
        4. Xuất báo cáo học tập
        5. Thoát chương trình
        ===================================================''')

        choice = input("Nhập vào lựa chọn của bạn: ")

        match choice:
            case "1":
                report_generator.display_student_scores(student_records)
            case "2":
                string_utils.normalize_student_names(student_records)
            case "3":
                print("--- SINH MÃ BÀI TẬP ---")
                print("Mã bài tập của bạn là:",generate_assignment_code())
            case "4":
                 report_generator.export_learning_report(student_records)
            case "5":
                print("Thoát")
                break
            case _:
                print("Nhập vào sai lựa chọn, vui lòng nhập lại")

if __name__ == "__main__":
    main()

