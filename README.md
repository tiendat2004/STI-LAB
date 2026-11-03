# STI-LAB

Kho lưu trữ các bài thực hành, bài tập và sản phẩm trong quá trình tìm hiểu lập trình robot, phát triển giao diện và lập trình hệ thống.
Link Docs: https://docs.google.com/spreadsheets/d/1qHSIAwnbe4TpMnCxN6Wdh9UVDbcfW4Atv8iZBbyf4UM/edit?gid=0#gid=0

## Mục tiêu

- Làm quen với quy trình phát triển phần mềm cho robot.
- Rèn luyện tư duy lập trình từ cơ bản đến ứng dụng thực tế.
- Kết hợp Python, C/C++ và các công cụ trực quan để xây dựng chương trình hoàn chỉnh.
- Lưu trữ tài liệu, mã nguồn và kết quả thực hành theo từng chủ đề.

## Nội dung tìm hiểu

### 1. ROS2

[Tìm hiểu về ROS2](https://docs.ros.org/en/jazzy/index.html), nền tảng middleware mã nguồn mở cho robot:

- Khái niệm node, topic, service, action và message.
- Tạo package bằng Python và C++.
- Giao tiếp giữa các node bằng publisher/subscriber.
- Sử dụng parameter, launch file và công cụ dòng lệnh của ROS2.

Ví dụ lệnh khởi tạo workspace:

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build
source install/setup.bash
```

### 2. Python

[Tìm hiểu về Python](https://docs.python.org/3/), ngôn ngữ được sử dụng để phát triển nhanh các ứng dụng và node ROS2:

1. Lập trình cơ bản
2. Mở rộng
3. Bài tập

### 3. PyQt5

[Tìm hiểu về PyQt5](https://www.riverbankcomputing.com/software/pyqt/), framework xây dựng giao diện đồ họa bằng Python:

1. Tìm hiểu phần mềm thiết kế QT designer 5
2. Lập trình python với QT5 designer
3. ROS

### 4. C/C++

[Tìm hiểu về C](https://en.cppreference.com/w/c) và [C++](https://en.cppreference.com/w/cpp) để xây dựng các chương trình hiệu năng cao:

1. Lập trình cơ bản

## Lab

1. Nắm chắc kiến thức cơ bản về C/C++ và Python.
2. Thực hành các bài toán xử lý dữ liệu và điều khiển cơ bản.
3. Xây dựng giao diện bằng PyQt5.
4. Tìm hiểu kiến trúc và công cụ của ROS2.
5. Kết hợp ROS2 với Python, C++ và PyQt5 trong các dự án nhỏ.
6. Hoàn thiện, kiểm thử và ghi lại kết quả của từng bài thực hành.

## Cấu trúc repository

Các bài thực hành có thể được sắp xếp theo nhóm chủ đề:

```text
STI-LAB/
├── ROS2/
├── Python/
├── PyQt5/
├── C-C++/
├── LICENSE
└── README.md
```
## Bản quyền

Repository được phát hành theo [MIT License](LICENSE).
