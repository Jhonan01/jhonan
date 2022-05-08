Published in LARS-2021 (IEEE Latin American Robotics Symposium) paper https://ieeexplore.ieee.org/document/9605432 

K. J. de Jesus, H. J. Kobs, A. R. Cukla, M. A. de Souza Leite Cuadros and D. F. T. Gamarra, "Comparison of Visual SLAM Algorithms ORB-SLAM2, RTAB-Map and SPTAM in Internal and External Environments with ROS," 2021 Latin American Robotics Symposium (LARS), 2021 Brazilian Symposium on Robotics (SBR), and 2021 Workshop on Robotics in Education (WRE), 2021, pp. 216-221, doi: 10.1109/LARS/SBR/WRE54079.2021.9605432.

# Robot for research involving visual SLAM using ROS with RGB-D and stereo camera
Robot differencial drive on ROS with RGB-D and stereo camera
![robot](https://user-images.githubusercontent.com/44379869/134515135-fe3c73ca-b777-48ba-820b-dfe1c67e1965.png)
This robot it's a robot built for realize simulations on ROS (Robot Operating System) with the kinetic distribution in order to make simulations with VISUAL SLAM (vSLAM) using RGB-D and stereo camera. 

Please cite the following paper if you use this project in your research: https://ieeexplore.ieee.org/document/9605432

# 1. Quick Start

The project has been tested on Ubuntu 16.04 (ROS Kinetic). Please create and initialize a ROS workspace. We assume that your workspace is named catkin_ ws. Then, run the following commands to clone this repo and build it:


`$ mkdir -p ~/catkin_ws/src`

`$ cd ~/catkin_ws/src`

`$ git clone https://github.com/Jhonan01/jhonan.git`

`$ catkin_init_workspace`

`$ cd ~/catkin_ws`

`$ catkin_make`


Finally, open a new terminal and start a simulation:

`$ source devel/setup.bash`

`$ roslaunch jhonan world.launch`

Open another terminal you can install a algorithm for control the robot but after that let's install it:

`$ sudo apt-get install ros-kinetic-teleop-twist-keyboard`

`$ rosrun teleop_twist_keyboard teleop_twist_keyboard.py`

If to find troubles or to have questions -> my Email: kesse_jonatas85@hotmail.com


