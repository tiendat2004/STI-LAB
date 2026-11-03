# STI-LAB

## ROS 2 CLI Cheat Sheet

### 1. Nodes
```bash
ros2 node list
```
Liệt kê các node đang chạy.

```bash
ros2 node info <node_name>
```
Xem thông tin node: topics, services, actions và parameters.

### 2. Topics
```bash
ros2 topic list
```
Liệt kê các topic đang hoạt động.

```bash
ros2 topic info <topic_name> --verbose
```
Xem message type, số publisher/subscriber và QoS.

```bash
ros2 topic echo <topic_name>
```
Hiển thị dữ liệu đang được publish.

```bash
ros2 topic hz <topic_name>
```
Đo tần số publish của topic (Hz).

```bash
ros2 topic bw <topic_name>
```
Đo băng thông dữ liệu của topic.

```bash
ros2 topic pub --once /cmd_vel geometry_msgs/msg/Twist \
"{linear: {x: 0.2}, angular: {z: 0.0}}"
```
Publish một message vận tốc đến `/cmd_vel`.

### 3. Services
```bash
ros2 service list
```
Liệt kê các service.

```bash
ros2 service type <service_name>
```
Xem kiểu request/response của service.

```bash
ros2 service call <service_name> <srv_type> '<args>'
```
Gửi request đến service và nhận response.

### 4. Parameters
```bash
ros2 param list
```
Liệt kê parameters của các node.

```bash
ros2 param get <node_name> <param_name>
```
Đọc giá trị parameter.

```bash
ros2 param set <node_name> <param_name> <value>
```
Thay đổi parameter khi node đang chạy.

```bash
ros2 param dump <node_name>
```
Lưu parameters của node ra file YAML.

### 5. Actions
```bash
ros2 action list
```
Liệt kê các action.

```bash
ros2 action info <action_name>
```
Xem thông tin action và các endpoint.

```bash
ros2 action send_goal <action_name> <action_type> '<args>'
```
Gửi goal để thực hiện tác vụ dài hạn và nhận feedback/result.

### 6. Interfaces
```bash
ros2 interface show <interface_type>
```
Xem cấu trúc message, service hoặc action.

Ví dụ:
```bash
ros2 interface show sensor_msgs/msg/LaserScan
```

### 7. Launch
```bash
ros2 launch <package_name> <launch_file>
```
Khởi chạy nhiều node cùng lúc theo file launch.

```bash
ros2 pkg list
```
Liệt kê các package đã được tìm thấy.

### 8. ROS 2 Bag
```bash
ros2 bag record /scan /odom /tf
```
Ghi dữ liệu từ các topic vào bag.

```bash
ros2 bag info <bag_name>
```
Xem thông tin file bag.

```bash
ros2 bag play <bag_name>
```
Phát lại dữ liệu đã ghi.

### 9. DDS & Middleware
```bash
echo $RMW_IMPLEMENTATION
```
Kiểm tra middleware DDS đang sử dụng.

```bash
echo $ROS_DOMAIN_ID
```
Kiểm tra Domain ID hiện tại.

```bash
export ROS_DOMAIN_ID=10
```
Thiết lập Domain ID cho terminal hiện tại.

```bash
ros2 doctor --report
```
Kiểm tra và báo cáo trạng thái ROS 2.

### 10. QoS (Quality of Service)

```bash
ros2 topic info /scan --verbose
```
Kiểm tra QoS của publisher và subscriber trên topic.

Các chính sách QoS:
- **Reliability:** `RELIABLE` đảm bảo giao nhận; `BEST_EFFORT` ưu tiên tốc độ.
- **Durability:** `VOLATILE` không lưu dữ liệu cũ; `TRANSIENT_LOCAL` giữ dữ liệu cho subscriber mới.
- **History:** `KEEP_LAST` giữ số mẫu giới hạn; `KEEP_ALL` giữ tất cả mẫu trong khả năng tài nguyên.
- **Depth:** Số message được lưu trong hàng đợi.

QoS giữa publisher và subscriber phải tương thích để giao tiếp thành công.
