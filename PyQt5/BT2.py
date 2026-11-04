import os
import socket
import subprocess
import sys

for variable in (
    "GTK_PATH",
    "GTK_MODULES",
    "GIO_MODULE_DIR",
    "GDK_PIXBUF_MODULEDIR",
    "GDK_PIXBUF_MODULE_FILE",
    "GTK_IM_MODULE_FILE",
):
    os.environ.pop(variable, None)
os.environ["QT_ACCESSIBILITY"] = "0"
os.environ["QT_IM_MODULE"] = "none"
os.environ["GSETTINGS_BACKEND"] = "memory"
os.environ["GSETTINGS_SCHEMA_DIR"] = "/usr/share/glib-2.0/schemas"

import rclpy
from rclpy.executors import ExternalShutdownException, SingleThreadedExecutor
from rclpy.impl.implementation_singleton import rclpy_implementation
from rclpy.node import Node
from std_msgs.msg import String

from PyQt5 import uic
from PyQt5.QtCore import QDate, QTime, QTimer, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QDialog


STATUS_TOPIC = "/button_status"
NAME_TOPIC = "/user_name"
UI_FILE = os.path.join(os.path.dirname(__file__), "bt2.ui")
IMAGE_FILE = os.path.join(os.path.dirname(__file__), "images.jpeg")


class RosNode(Node):
    def __init__(self):
        super().__init__("qt_bt2")
        self.status_publisher = self.create_publisher(
            String, STATUS_TOPIC, 10
        )
        self.status_subscription = self.create_subscription(
            String, STATUS_TOPIC, self.on_status_received, 10
        )
        self.name_subscription = self.create_subscription(
            String, NAME_TOPIC, self.on_name_received, 10
        )
        self.gui = None

    def on_status_received(self, message):
        if self.gui is not None:
            self.gui.status_received.emit(message.data)

    def on_name_received(self, message):
        if self.gui is not None:
            self.gui.name_received.emit(message.data)


class App(QDialog):
    status_received = pyqtSignal(str)
    name_received = pyqtSignal(str)

    def __init__(self, node):
        super().__init__()
        uic.loadUi(UI_FILE, self)
        self.node = node

        self.box_date.setReadOnly(True)
        self.box_wifi.setReadOnly(True)
        self.box_name.setReadOnly(True)
        self.box_stt.setReadOnly(True)
        self.lineEdit_9.setReadOnly(True)
        self.stt_progress.setRange(0, 100)

        self.pus_button.setIcon(QIcon(IMAGE_FILE))
        self.pus_button.setIconSize(self.pus_button.sizeHint())
        self.set_button_released_style()
        self.update_status("ĐÃ NHẢ")

        self.pus_button.pressed.connect(self.on_button_pressed)
        self.pus_button.released.connect(self.on_button_released)
        self.pus_exit.clicked.connect(self.close)
        self.status_received.connect(self.update_status)
        self.name_received.connect(self.update_name)

        self.info_timer = QTimer(self)
        self.info_timer.timeout.connect(self.update_system_info)
        self.info_timer.start(1000)
        self.update_system_info()

    def publish_status(self, status):
        if not rclpy.ok():
            return
        message = String()
        message.data = status
        self.node.status_publisher.publish(message)
        self.update_status(status)

    def on_button_pressed(self):
        self.set_button_pressed_style()
        self.publish_status("ĐANG NHẤN")

    def on_button_released(self):
        self.set_button_released_style()
        self.publish_status("ĐÃ NHẢ")

    def update_status(self, status):
        is_pressed = status == "ĐANG NHẤN"
        self.pus_status.setPlainText(status)
        self.box_stt.setText("ON" if is_pressed else "OFF")
        self.stt_progress.setValue(100 if is_pressed else 0)
        if is_pressed:
            self.box_stt.setStyleSheet(
                "color: white; background-color: #16a34a;"
            )
        else:
            self.box_stt.setStyleSheet(
                "color: white; background-color: #2563eb;"
            )

    def set_button_pressed_style(self):
        self.pus_button.setStyleSheet(
            "QPushButton { background-color: #16a34a; color: white; }"
        )

    def set_button_released_style(self):
        self.pus_button.setStyleSheet(
            "QPushButton { background-color: #2563eb; color: white; }"
        )

    def update_name(self, name):
        self.box_name.setText(name)

    def update_system_info(self):
        self.box_date.setDate(QDate.currentDate())
        self.timeEdit.setTime(QTime.currentTime())
        self.box_wifi.setText(self.get_wifi_ip())
        self.lineEdit_9.setText(self.get_ping())

    @staticmethod
    def get_wifi_ip():
        try:
            result = subprocess.run(
                ["ip", "-4", "route", "get", "1.1.1.1"],
                check=True,
                capture_output=True,
                text=True,
                timeout=1,
            )
        except (OSError, subprocess.SubprocessError):
            return "N/A"

        fields = result.stdout.split()
        if "src" not in fields:
            return "N/A"
        address_index = fields.index("src") + 1
        return fields[address_index] if address_index < len(fields) else "N/A"

    @staticmethod
    def get_ping():
        try:
            result = subprocess.run(
                ["ping", "-c", "1", "-W", "1", "1.1.1.1"],
                check=True,
                capture_output=True,
                text=True,
                timeout=2,
            )
        except (OSError, subprocess.SubprocessError):
            return "N/A"

        for field in result.stdout.split():
            if field.startswith("time="):
                return f"{field.removeprefix('time=')} ms"
        return "N/A"


def main():
    rclpy.init()
    app = QApplication(sys.argv)
    node = RosNode()
    window = App(node)
    node.gui = window

    executor = SingleThreadedExecutor()
    executor.add_node(node)

    def spin_ros_once():
        if not rclpy.ok():
            ros_timer.stop()
            return
        try:
            executor.spin_once(timeout_sec=0)
        except (
            ExternalShutdownException,
            rclpy_implementation.RCLError,
        ):
            ros_timer.stop()

    ros_timer = QTimer()
    ros_timer.timeout.connect(spin_ros_once)
    ros_timer.start(10)

    window.show()
    exit_code = app.exec_()

    ros_timer.stop()
    executor.shutdown()
    node.destroy_node()
    if rclpy.ok():
        rclpy.shutdown()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
