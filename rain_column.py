import random
from colors import Colors
import pygame


class RainColumn:
    id = 0
    font_size = 24
    min_alpha = 10
    max_alpha = 200
    done = []
    characters = ['a', 'b', 'c', 'd', 'e', 'f']

    def __init__(self, size):
        self.id = RainColumn.id
        self.screenWidth, self.screenHeight = size
        self.max_length = self.screenHeight // RainColumn.font_size
        self.length = random.randint(1, self.max_length)
        self.pos = (
            random.randint(0, self.screenWidth - RainColumn.font_size),
            random.randint(0, self.screenHeight // 4)
        )
        self.font = pygame.font.SysFont(None, RainColumn.font_size)
        RainColumn.id += 1

    def next_pos(self):
        self.pos = self.pos[0], self.pos[1] + RainColumn.font_size

    def is_out(self):
        if self.pos[1] > (self.screenHeight + self.length * RainColumn.font_size):
            return True
        return False

    def draw(self, screen):
        for i in range(self.length):
            img = self.font.render(random.choice(RainColumn.characters), True, Colors.GREEN)
            img.set_alpha(random.randint(self.min_alpha, self.max_alpha))
            screen.blit(img, (self.pos[0], self.pos[1] - i * RainColumn.font_size))

    def render(self, screen):
        self.draw(screen)
        self.next_pos()

        if self.is_out():
            RainColumn.done.append(self.id)
