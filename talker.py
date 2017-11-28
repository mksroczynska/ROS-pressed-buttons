#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
import pygame, time, sys


class KeyboardPublisher(object):
    def __init__(self):
        # pygame screen which will print currently pressed buttons
        pygame.init()
        self.sc = pygame.display
        self.screen = self.sc.set_mode((500, 150), 0, 10)
        self.screen.fill((0, 0, 0))
        self.sc.set_caption("Pressed keys")
        self.f1 = pygame.font.SysFont("comicsansms", 24)
        self.text_x0 = 10
        self.text_y = 20
        self.text_dx = 20
        # topic "/keyboard"
        self.pub = rospy.Publisher('/keyboard', Joy, queue_size=10)
        # node named "pressed_keys"
        rospy.init_node('pressed_keys', anonymous=True)
        # message
        self.joyState = Joy()

    def callb(self, event):  # callback
        # rospy.loginfo(self.joyState) # can be used to check what is being published
        self.pub.publish(self.joyState)

    def print_letters(self, keysList):  # print currently pressed buttons on the screen
        x = self.text_x0
        for i in range(len(keysList)):
            if keysList[i] == 1:
                name = pygame.key.name(i)
                text = self.f1.render(name, True, (255, 255, 255))
                self.screen.blit(text, (x, self.text_y))
                x += self.text_dx
        self.sc.update()
        self.screen.fill((0, 0, 0))

    def talker(self, freqHz):
        rate = 1.000 / freqHz  # every #rate seconds publishes on topic
        # initialize callback
        callback_publish = rospy.Timer(rospy.Duration(rate), self.callb)
        while not rospy.is_shutdown():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            keys = pygame.key.get_pressed()
            self.print_letters(keys)
            self.joyState.buttons = keys
            callback_publish


if __name__ == '__main__':
    try:
        kp = KeyboardPublisher()
        kp.talker(20)
    except rospy.ROSInterruptException:
        pass
