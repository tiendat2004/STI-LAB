import rclpy
from rclpy.node import Node
from custom_interfaces.srv import CustomService # Load service tùy chỉnh

class MinimalService(Node):
    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(CustomService, 'add_two_ints', self.add_two_ints_callback)
        self.get_logger().info('Ready to add two ints.')

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f'Incoming request\na: {request.a} b: {request.b}')
        self.get_logger().info(f'Sending back response: [{response.sum}]')
        return response

def main(args=None):
    rclpy.init(args=args)
    minimal_service = MinimalService()
    rclpy.spin(minimal_service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()