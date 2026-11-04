import sys
import rclpy
from rclpy.node import Node
from custom_interfaces.srv import CustomService

class MinimalClientAsync(Node):
    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(CustomService, 'add_two_ints')
        
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        
        self.req = CustomService.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main(args=None):
    rclpy.init(args=args)
    minimal_client = MinimalClientAsync()
    
    # Truyền sẵn tham số để test (a=10, b=20)
    a = 10
    b = 20
    
    response = minimal_client.send_request(a, b)
    minimal_client.get_logger().info(
        f'Result of add_two_ints: for {a} + {b} = {response.sum}')

    minimal_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()