import threading
import pygame
from rain_column import RainColumn, Colors


class CharacterRain:
    max_rains = 100

    def __init__(self):
        self.running = True
        self.size = (800, 600)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("character rain")
        self.rain_columns = []

    def clear(self):
        for rain_column in self.rain_columns:
            if rain_column.id in RainColumn.done:
                self.rain_columns.remove(rain_column)

    def new_columns(self):
        for _ in range(CharacterRain.max_rains - len(self.rain_columns)):
            self.rain_columns.append(RainColumn(self.size))

    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.clear()
            self.new_columns()

            self.screen.fill(Colors.BG)

            for rain_column in self.rain_columns:
                threading.Thread(target=rain_column.render, args=(self.screen,)).start()

            pygame.display.flip()
            self.clock.tick(10)
