import os
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
from PyQt5.QtCore import QTime, QTimer, pyqtSignal
from PyQt5.QtWidgets import QApplication, QDialog


TOPIC = "/button_status"
UI_FILE = os.path.join(os.path.dirname(__file__), "bt1.ui")


class RosNode(Node):
    def __init__(self):
        super().__init__("qt_bt1")
        self.publisher = self.create_publisher(String, TOPIC, 10)
        self.subscription = self.create_subscription(
            String, TOPIC, self.on_status_received, 10
        )
        self.gui = None

    def on_status_received(self, message):
        if self.gui is not None:
            self.gui.status_received.emit(message.data)


class App(QDialog):
    status_received = pyqtSignal(str)

    def __init__(self, node):
        super().__init__()
        uic.loadUi(UI_FILE, self)
        self.node = node

        self.timeEdit.setReadOnly(True)
        self.pus_status.setReadOnly(True)
        self.pus_status.setPlainText("ĐÃ NHẢ")

        self.pus_button.pressed.connect(
            lambda: self.publish_status("ĐANG NHẤN")
        )
        self.pus_button.released.connect(
            lambda: self.publish_status("ĐÃ NHẢ")
        )
        self.pus_exit.clicked.connect(self.close)
        self.status_received.connect(self.update_status)

        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self.update_time)
        self.clock_timer.start(1000)
        self.update_time()

    def publish_status(self, status):
        if not rclpy.ok():
            return
        message = String()
        message.data = status
        self.node.publisher.publish(message)
        self.update_status(status)

    def update_status(self, status):
        self.pus_status.setPlainText(status)

    def update_time(self):
        self.timeEdit.setTime(QTime.currentTime())


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
