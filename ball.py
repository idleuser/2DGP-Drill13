from pico2d import *
import game_world
import game_framework
import random

import server


class Ball:
    image = None

    def __init__(self, x=None, y=None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(30, 1800)
        self.y = y if y else random.randint(30, 1050)

    def draw(self):
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom

        self.image.draw(sx, sy)
        # draw_rectangle(*self.get_bb())

    def update(self):
        self.x = clamp(25.0, self.x, server.background.w - 25.0)
        self.y = clamp(30.0, self.y, server.background.h - 45.0)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        if group == 'boy:ball':
            game_world.remove_object(self)