# YOLOv8-people-detection_ROS2

# Prerequisites
 * Ubuntu 20.04 Focal Fossa (https://releases.ubuntu.com/20.04/)
 * ROS 2 foxy (https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html)
 # Installation:
 YOLOv8 via the ultralytics pip package for the latest stable release 
 (open new terminal)
 ```
 pip install ultralytics
   ```
# To build the code
 To build this package, you either need a ROS 2 workspace or create a new one. Here is the instructions to create a new ROS 2 workspace, build the package.
 ```
mkdir -p ~/ros2_ws/src

cd  ~/ros2_ws/src

git clone https://github.com/aleenalentin/YOLOv8-people-detection_ROS2.git

cd ~/ros2_ws

colcon build 

 . install/setup.bash
```


# To run the code
   ```
   cd ~/ros2_ws
   . install/setup.bash
    ros2 launch people_detector people_detection.py
   ```


