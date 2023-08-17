from __future__ import print_function
import rclpy # Python library for ROS 2
from rclpy.node import Node # Handles the creation of nodes
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library
from ultralytics import YOLO
from ament_index_python.packages import get_package_share_directory

class VideoSubscriber(Node):
  """
  Create an VideoSubscriber class, which is a subclass of the Node class.
  """
  def __init__(self):
    """
    Class constructor to set up the node
    """
    # Initiate the Node class's constructor and give it a name
    super().__init__('video_subscriber')
    package_share_directory = get_package_share_directory('people_detector')
    self.br = CvBridge()
    
    path="/yolov8n.pt"
    full_path=package_share_directory + path
    print(full_path)
    self.model = YOLO(full_path)
    
    
    # Create the subscriber
    self.subscription = self.create_subscription(
      Image, 
      'video_frames', 
      self.listener_callback, 
      10)
      

  def listener_callback(self, data):
    """
    Callback function.
    """

    # Display the message on the console
    self.get_logger().info('Receiving video frame')
 
    # Convert ROS Image message to OpenCV image
    current_frame = self.br.imgmsg_to_cv2(data)
    

    results = self.model.predict(source=current_frame, save=True, save_txt=True)

    # Display image
    cv2.imshow("camera", current_frame)
    
    cv2.waitKey(1)
  
def main(args=None):
  
  # Initialize the rclpy library
  rclpy.init(args=args)
  
  # Create the node
  video_subscriber = VideoSubscriber()
  
  # Spin the node so the callback function is called.
  rclpy.spin(video_subscriber)

  # Destroy the node explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)
  video_subscriber.destroy_node()
  
  # Shutdown the ROS client library for Python
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()
