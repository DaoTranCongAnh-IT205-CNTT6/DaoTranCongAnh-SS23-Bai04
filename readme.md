# THIẾT KẾ HỆ THỐNG TIỆN ÍCH HỌC TẬP RIKKEI ACADEMY

## 1. Cấu trúc thư mục

```text
rikkei_learning_tools/
│
├── main.py
│
├── data/
│   └── students.py
│
├── utils/
│   ├── __init__.py
│   ├── score_utils.py
│   ├── string_utils.py
│   └── random_utils.py
│
└── reports/
    ├── __init__.py
    └── report_generator.py
```

---

# 2. Thiết kế Module

## Module: data/students.py

### Vai trò

Lưu dữ liệu sinh viên ban đầu.

### Hàm chính

Không có.

### Kiểu import sử dụng

```python
from data.students import student_records
```

---

## Module: utils/score_utils.py

### Vai trò

Xử lý điểm số.

### Hàm chính

* calculate_average()
* classify_student()

### Kiểu import

```python
from utils.score_utils import calculate_average
```

---

## Module: utils/string_utils.py

### Vai trò

Chuẩn hóa dữ liệu chuỗi.

### Hàm chính

* normalize_student_names()

### Kiểu import

```python
import utils.string_utils as string_utils
```

---

## Module: utils/random_utils.py

### Vai trò

Sinh mã bài tập ngẫu nhiên.

### Hàm chính

* generate_assignment_code()

### Kiểu import

```python
from utils.random_utils import generate_assignment_code
```

---

## Module: reports/report_generator.py

### Vai trò

Hiển thị báo cáo và xuất file.

### Hàm chính

* display_student_scores()
* export_learning_report()

### Kiểu import

```python
import reports.report_generator as report_generator
```

---

# 3. Thiết kế các hàm nghiệp vụ

## calculate_average(scores)

### Input

Danh sách điểm.

### Output

Điểm trung bình kiểu float.

### Module

score_utils.py

### Pseudocode

```text
Nếu danh sách rỗng:
    trả về 0

Duyệt từng phần tử:
    nếu là số:
        cộng vào tổng
        tăng bộ đếm

Nếu không có điểm hợp lệ:
    trả về 0

Trả về tổng / số lượng
```

---

## classify_student(average)

### Input

Điểm trung bình.

### Output

Xếp loại.

### Module

score_utils.py

### Pseudocode

```text
Nếu average >= 8:
    Giỏi
Nếu average >= 6.5:
    Khá
Nếu average >= 5:
    Trung bình
Ngược lại:
    Yếu
```

---

## display_student_scores(records)

### Input

Danh sách sinh viên.

### Output

In danh sách sinh viên.

### Module

report_generator.py

### Pseudocode

```text
Nếu danh sách rỗng:
    thông báo

Duyệt từng sinh viên:
    tính điểm trung bình
    xếp loại
    hiển thị
```

---

## normalize_student_names(records)

### Input

Danh sách sinh viên.

### Output

Danh sách đã chuẩn hóa.

### Module

string_utils.py

### Pseudocode

```text
Nếu danh sách rỗng:
    thông báo

Duyệt từng sinh viên:
    strip()
    split()
    join()
    title()
```

---

## generate_assignment_code()

### Input

Không có.

### Output

Chuỗi dạng PY-XXXX

### Module

random_utils.py

### Pseudocode

```text
Tạo tập ký tự:
    A-Z + 0-9

Random 4 ký tự

Ghép:
    PY-XXXX
```

---

## export_learning_report(records)

### Input

Danh sách sinh viên.

### Output

File learning_report.txt

### Module

report_generator.py

### Pseudocode

```text
Tính:
    tổng số sinh viên
    đạt yêu cầu
    cần cải thiện

Lấy thời gian hiện tại

Ghi file txt

In thông báo màu xanh bằng colorama
```

---

## main()

### Input

Lựa chọn menu.

### Output

Điều hướng chương trình.

### Module

main.py

### Pseudocode

```text
while True

Hiển thị menu

Nhập lựa chọn

1 -> hiển thị điểm
2 -> chuẩn hóa tên
3 -> sinh mã
4 -> xuất báo cáo
5 -> thoát

Bắt ValueError
```
