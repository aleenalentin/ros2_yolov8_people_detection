people_detector

Prerequisites:
 * Ubuntu 20.04 Focal Fossa (https://releases.ubuntu.com/20.04/)
 * ROS 2 foxy (https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html)
 ----------------------------------------------------------------------------------------------------------------------------
Installation:
 YOLOv8 via the ultralytics pip package for the latest stable release 
 (open new terminal)
 >> pip install ultralytics
 ----------------------------------------------------------------------------------------------------------------------------
To build the code:
   To build this package, you either need a ROS 2 workspace or create a new one. Here is the instructions to create a new ROS 2 workspace, build the package.
    (open new terminal)
 >> mkdir -p ~/ros2_ws/src
 >> cd  ~/ros2_ws/src

copy the package to src folder & go back to workspace directory & do colcon build
>>cd  ~/ros2_ws
>> colcon build

Set up your environment by sourcing the following file.

source ~/ros2_ws/install/setup.bash
------------------------------------------------------------------------------------------------------------------------------
To run your package:
>> ros2 launch people_detector people_detection.py

------------------------------------------------------------------------------------------------------------------------------




