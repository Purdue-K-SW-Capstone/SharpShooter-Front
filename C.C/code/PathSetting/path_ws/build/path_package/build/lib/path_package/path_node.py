import time
import socket
import rclpy
from rclpy.node import Node

from std_msgs.msg import String

HOST = socket.gethostbyname(socket.gethostname()) # find address based on host name
PORT = 6000 # port number
STORE_DIR = "/home/pi/C.C/test/PathSetting/path_info/" # where to store the data
PATH_FILE = "coordinates.json" # what name to store

class locationPublisher(Node):
    '''
    Receiving GPS coordinates of start location, end location, and dumpster's location
    '''
    def __init__(self, socket, buf_size=4096, store_dir=STORE_DIR):
        # socket: socket class for connection
        # buf_size: how many bytes to get; 4096 bytes by default
        # store_dir: where to store received data; STORE_DIR by default
        super().__init__('location_publisher')
        self.publisher_ = self.create_publisher(String, 'location', 100)

        self.i = 0 # counter for connection attempts
        self.store_dir = store_dir
        self.buf_size = buf_size

        socket.settimeout(3) # set socket maximum waiting time as 3 seconds
        self.socket = socket
        self.socket.listen() # ready for connection

        timer_period = 0.01  # seconds for cycle calling callback function
        self.timer = self.create_timer(timer_period, self.timer_callback) # timer create

    def timer_callback(self):
        # callback fuction receiving data from app

        # for checking operation
        msg = String()
        msg.data = 'callback [%d]' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: %s' % msg.data)

        try:
            conn, addr = self.socket.accept() # new connection
            data = conn.recv(self.buf_size) # wait for data of defined buffer size
            # write received data as a file
            with conn:
                with open(self.store_dir + PATH_FILE, "wb") as f:
                    f.write(data)
        
        except socket.timeout: # no connection for more than 3 seconds
            print("timeout {}".format(self.i))

        self.i += 1 # increase counter


def main(args=None): # entry point for ROS2
    # set socket to get data
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind((HOST, PORT))

    # node initialization
    rclpy.init(args=args)
    location_publisher = locationPublisher(tcp_socket)

    rclpy.spin(location_publisher) # run node

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    location_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
