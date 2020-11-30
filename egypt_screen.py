import pygame
import pygame.freetype
from pygame.sprite import Sprite
import UIelement
from UIelement import *
import gamestate
from gamestate import GameState

BLUE = (9, 5, 101)
WHITE = (255, 255, 255, 0)
WHITE_BTN = (255, 255, 255)
BLACK = (0, 0, 0)


def egypt_screen(screen):
    element = UIelement
    return_btn = element.UIElement(
        center_position=(140, 700),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE_BTN,
        text="Return to main menu",
        action=GameState.TITLE,
    )
    country_egypt_1 = element.UIElement(
        center_position=(250, 150),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="1",
        action=None
    )
    country_egypt_2 = element.UIElement(
        center_position=(400, 500),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="2",
        action=None
    )
    country_egypt_3 = element.UIElement(
        center_position=(500, 240),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="3",
        action=None
    )
    country_egypt_4 = element.UIElement(
        center_position=(610, 255),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="4",
        action=None
    )
    country_egypt_5 = element.UIElement(
        center_position=(610, 215),
        font_size=25,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="5",
        action=None
    )
    country_egypt_6 = element.UIElement(
        center_position=(650, 185),
        font_size=40,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="6",
        action=None
    )
    country_egypt_7 = element.UIElement(
        center_position=(630, 100),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="7",
        action=None
    )
    country_egypt_8 = element.UIElement(
        center_position=(570, 83),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="8",
        action=None
    )
    country_egypt_9 = element.UIElement(
        center_position=(690, 50),
        font_size=40,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="9",
        action=None
    )
    country_egypt_10 = element.UIElement(
        center_position=(710, 100),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="10",
        action=None
    )
    country_egypt_11 = element.UIElement(
        center_position=(750, 70),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="11",
        action=None
    )
    country_egypt_12 = element.UIElement(
        center_position=(760, 100),
        font_size=25,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="12",
        action=None
    )
    country_egypt_13 = element.UIElement(
        center_position=(760, 150),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="13",
        action=None
    )
    country_egypt_14 = element.UIElement(
        center_position=(840, 100),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="14",
        action=None
    )
    country_egypt_15 = element.UIElement(
        center_position=(830, 160),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="15",
        action=None
    )
    country_egypt_16 = element.UIElement(
        center_position=(960, 100),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="16",
        action=None
    )
    country_egypt_17 = element.UIElement(
        center_position=(980, 190),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="17",
        action=None
    )
    country_egypt_18 = element.UIElement(
        center_position=(820, 320),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="18",
        action=None
    )
    country_egypt_19 = element.UIElement(
        center_position=(710, 330),
        font_size=25,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="19",
        action=None
    )
    country_egypt_20 = element.UIElement(
        center_position=(770, 370),
        font_size=25,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="20",
        action=None
    )
    country_egypt_21 = element.UIElement(
        center_position=(885, 410),
        font_size=32,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="21",
        action=None
    )
    country_egypt_22 = element.UIElement(
        center_position=(885, 570),
        font_size=40,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="22",
        action=None
    )
    country_egypt_23 = element.UIElement(
        center_position=(1190, 450),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="23",
        action=None
    )
    buttons = [return_btn
        , country_egypt_1, country_egypt_2, country_egypt_3, country_egypt_4, country_egypt_5, country_egypt_6
        , country_egypt_7, country_egypt_8, country_egypt_9, country_egypt_10, country_egypt_11, country_egypt_12
        , country_egypt_13, country_egypt_14, country_egypt_15, country_egypt_16, country_egypt_17
        , country_egypt_18, country_egypt_19, country_egypt_20, country_egypt_21, country_egypt_22
        , country_egypt_23
               ]
    egyptmapimage = pygame.image.load(r'.\assets\egyptmapgame.png')

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)
        screen.blit(egyptmapimage, (50, 30))
        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()
