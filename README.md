# ROS-pressed-buttons
ROS-node publishing the current state of a keyboard with some given frequency. Messages are of the type sensors_msgs/Joy and they are published to the topic '/keyboard'. 

## Prerequisities
In order to run this program, you need to have installed:
* ROS (http://www.ros.org/) including 'joy' package (http://wiki.ros.org/joy) 
* Pygame Python package (https://www.pygame.org/news)
## Using the program
Once you run this code, the window 'Pressed keys' with the currently pressed buttons opens. Information about them is sent to the '/keyboard' topic with the frequency set to 20 Hz. The value of the frequency is an argument of KeyboardPublisher.talker function. 
The window 'Pressed keys' has to remain active, otherwise the buttons that you press will not be registered in the messages. Closing this window stops the program.

