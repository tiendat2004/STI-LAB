import math
import threading
import time
#Ham
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#Class
class Robot:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0

    def move(self, command):
        match command:
            case "UP":
                self.y += 1
            case "DOWN":
                self.y -= 1
            case "LEFT":
                self.x -= 1
            case "RIGHT":
                self.x += 1
            case _:
                print("Lệnh không hợp lệ!")
    def show(self):
        print(f"{self.name}: ({self.x}, {self.y})")
#Ke thua
class AGV(Robot):
    def __init__(self, name):
        super().__init__(name)
        self.status = "STOP"

    def run(self):
        self.status = "MOVING"

        while True:
            command = input("Nhập lệnh (UP/DOWN/LEFT/RIGHT/EXIT): ").upper()

            if command == "EXIT":
                self.status = "STOP"
                break

            self.move(command)
            self.show()

def monitor(robot):
    while robot.status != "STOP":
        print("Trạng thái:", robot.status)
        time.sleep(2)


agv = AGV("AGV-01")
thread = threading.Thread(target=monitor, args=(agv,))
thread.start()
#Thread
agv.run()
thread.join()

print("Goal(5, 5):",
      distance(agv.x, agv.y, 5, 5))