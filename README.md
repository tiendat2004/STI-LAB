# STI-LAB

Kho lưu trữ các bài thực hành, bài tập và sản phẩm trong quá trình tìm hiểu lập trình robot, phát triển giao diện và lập trình hệ thống.

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
- Kết nối ROS2 với cảm biến, cơ cấu chấp hành và các ứng dụng robot.

Ví dụ lệnh khởi tạo workspace:

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build
source install/setup.bash
```

### 2. Python

[Tìm hiểu về Python](https://docs.python.org/3/), ngôn ngữ được sử dụng để phát triển nhanh các ứng dụng và node ROS2:

- Biến, kiểu dữ liệu, cấu trúc điều khiển và hàm.
- Lập trình hướng đối tượng và module.
- Đọc/ghi tệp, xử lý dữ liệu và quản lý ngoại lệ.
- Môi trường ảo, `pip` và tổ chức project.
- Viết node ROS2 bằng `rclpy`.

### 3. PyQt5

[Tìm hiểu về PyQt5](https://www.riverbankcomputing.com/software/pyqt/), framework xây dựng giao diện đồ họa bằng Python:

- Thiết kế cửa sổ, widget và layout.
- Signal/slot và xử lý sự kiện người dùng.
- Làm việc với bảng, biểu mẫu, hộp thoại và biểu đồ.
- Kết nối giao diện PyQt5 với node ROS2.
- Tách phần giao diện và phần xử lý để dễ bảo trì.

### 4. C/C++

[Tìm hiểu về C](https://en.cppreference.com/w/c) và [C++](https://en.cppreference.com/w/cpp) để xây dựng các chương trình hiệu năng cao:

- Cú pháp, con trỏ, bộ nhớ và cấu trúc dữ liệu.
- Hàm, struct, file I/O và quản lý tài nguyên.
- Lập trình hướng đối tượng trong C++.
- STL, template và xử lý lỗi.
- Viết node ROS2 bằng `rclcpp`.

## Lộ trình đề xuất

1. Nắm chắc kiến thức cơ bản về C/C++ và Python.
2. Thực hành các bài toán xử lý dữ liệu và điều khiển cơ bản.
3. Xây dựng giao diện bằng PyQt5.
4. Tìm hiểu kiến trúc và công cụ của ROS2.
5. Kết hợp ROS2 với Python, C++ và PyQt5 trong các dự án nhỏ.
6. Hoàn thiện, kiểm thử và ghi lại kết quả của từng bài thực hành.

## Công cụ đề xuất

- Ubuntu Linux
- Python 3
- CMake và GCC/G++
- ROS2
- Qt Designer và PyQt5
- Visual Studio Code hoặc Qt Creator
- Git và GitHub

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

## Tài liệu tham khảo

- [ROS2 Documentation](https://docs.ros.org/)
- [Python Documentation](https://docs.python.org/3/)
- [Qt for Python / PyQt](https://www.riverbankcomputing.com/software/pyqt/)
- [cppreference](https://en.cppreference.com/)
- [CMake Documentation](https://cmake.org/documentation/)

## Bản quyền

Repository được phát hành theo [MIT License](LICENSE).
