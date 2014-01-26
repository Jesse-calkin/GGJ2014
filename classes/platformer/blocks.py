from pygame import Surface
from pygame.sprite import Sprite, Group
from pygame.transform import scale

import Queue
import random

import constants
from vector import V2

BLOCK_VELOCITY = V2(-60, 0)


class Block(Sprite):

    def __init__(self):
        Sprite.__init__(self)

        self.image = Surface([10, 10])
        self.image.fill(random.choice(constants.TASTE_THE_RAINBOW))
        self.rect = self.image.get_rect()

    def update(self, scroll_speed, delta_time):
        change = scroll_speed * BLOCK_VELOCITY.x * delta_time

        self.rect.x += scroll_speed * BLOCK_VELOCITY.x * delta_time

        if self.rect.right < 0:
            self.mgr.recycle_block()
        #TODO(caleb) XXX: not really sure what's going on, but here's a hack.
        elif self.rect.x < 0:
             self.rect.x += -1


class BlockManager(object):

    MAX_QUEUE_SIZE = 6

    MAX_GAP_X = 100
    MAX_GAP_Y = 15

    MIN_WIDTH = 150
    MIN_HEIGHT = 30

    MAX_WIDTH = 300
    MAX_HEIGHT = 50

    start_position = [0, constants.SCREEN_HEIGHT]
    next_position = [0, 0]

    obstacle_group = Group()

    def __init__(self):
        self.queue = Queue.Queue(self.MAX_QUEUE_SIZE)

        for _ in range(self.MAX_QUEUE_SIZE):
            block = Block()
            block.mgr = self
            self.obstacle_group.add(block)
            self.queue.put(block)

        self.next_position = self.start_position

        for _ in range(self.MAX_QUEUE_SIZE):
            self.recycle_block()

    def recycle_block(self):
        width = random.randint(self.MIN_WIDTH, self.MAX_WIDTH)
        height = random.randint(self.MIN_HEIGHT, self.MAX_HEIGHT)

        position = self.next_position

        block = self.queue.get()

        block.rect.w = width
        block.rect.h = height
        block.rect.x = position[0]
        block.rect.y = position[1] - height

        block.image = scale(block.image, [block.rect.w, block.rect.h])

        self.queue.put(block)

        x_gap = random.randint(0, self.MAX_GAP_X)
        y_gap = random.randint(0, self.MAX_GAP_Y)

        self.next_position[0] += x_gap + width
        self.next_position[1] = constants.SCREEN_HEIGHT - y_gap

    def update(self, speed, delta_time):
        self.next_position[0] += speed * BLOCK_VELOCITY.x * delta_time
        self.obstacle_group.update(speed, delta_time)

    def on_draw(self, surface):
        self.obstacle_group.draw(surface)
