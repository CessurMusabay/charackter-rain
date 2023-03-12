import pygame
from character_rain import CharacterRain

if __name__ == '__main__':
    pygame.init()
    code_rain = CharacterRain()
    code_rain.main_loop()
    pygame.quit()
