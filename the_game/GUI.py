"""
This file handles GUI (everything visual).
Sets images, texts, fonts, window size etc.
Handles events.
"""

import pygame
import os
import sys


pygame.init()
pygame.font.init()
pygame.display.list_modes()

clock = pygame.time.Clock()

# VARIABLES

FPS = 20

WINDOW_SIZE = 450

# BACKGROUND
BG_IMAGE_5 = pygame.image.load(os.path.join('assets/board_5.png'))
BG_IMAGE_7 = pygame.image.load(os.path.join('assets/board_7.png'))
BG_IMAGE_9 = pygame.image.load(os.path.join('assets/board_9.png'))

BG = pygame.transform.scale(BG_IMAGE_5, (WINDOW_SIZE, WINDOW_SIZE))
BG_BLUR_IMAGE = pygame.image.load(os.path.join('assets/board_blur.png'))
BG_BLUR = pygame.transform.scale(BG_BLUR_IMAGE, (WINDOW_SIZE, WINDOW_SIZE))

# IMAGES SIZES
radius = WINDOW_SIZE / 5

images_smaller_than_place = 6
image_radius = radius - images_smaller_than_place

WIDTH, HEIGHT = WINDOW_SIZE, WINDOW_SIZE

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shannon Game by Felo")
icon_size = (64, 64)
programIcon = pygame.transform.scale(
    pygame.image.load(os.path.join('assets/icon.png')), icon_size)
pygame.display.set_icon(programIcon)

PLAY_IMAGE = pygame.image.load(
    os.path.join('assets/play.png'))
PLAY = pygame.transform.scale(PLAY_IMAGE, (image_radius, image_radius))

SETTINGS_IMAGE = pygame.image.load(
    os.path.join('assets/settings.png'))
SETTINGS = pygame.transform.scale(SETTINGS_IMAGE, (image_radius, image_radius))

WINDOW_SMALLER_THAN_WINDOW = 50
INPUT_SIZE = WINDOW_SIZE - WINDOW_SMALLER_THAN_WINDOW, 70
INPUT_IMAGE = pygame.image.load(
    os.path.join('assets/input.png'))
INPUT = pygame.transform.scale(INPUT_IMAGE, INPUT_SIZE)

LIGHT_CIRCLE_IMAGE = pygame.image.load(
    os.path.join('assets/piece_light.png'))
LIGHT_CIRCLE = pygame.transform.scale(
    LIGHT_CIRCLE_IMAGE, (image_radius, image_radius))

DARK_CIRCLE_IMAGE = pygame.image.load(
    os.path.join('assets/piece_dark.png'))
DARK_CIRCLE = pygame.transform.scale(
    DARK_CIRCLE_IMAGE, (image_radius, image_radius))

BLANK_CIRCLE_IMAGE = pygame.image.load(
    os.path.join('assets/piece_blank.png'))
BLANK_CIRCLE = pygame.transform.scale(
    BLANK_CIRCLE_IMAGE, (image_radius, image_radius))

# FONTS
font_path = 'assets/COMIC.TTF'

FONT = pygame.font.Font(font_path, 40)
FONT_SMALL = pygame.font.Font(font_path, 30)
FONT_BIG = pygame.font.Font(font_path, 80)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREY = (220, 220, 220)


class Window:
    """
    Class Window.
    Manages GUI of the game.
    Contains attributes:\n
        :param BG: represents background image of the window\n
    """

    def __init__(self) -> None:
        self._BG = BG

    def handle_events(self, board, human_move_now):
        """
        Handles users interactions with the game, such as:\n
            :quiting the game\n
            :making a move (mouse click on the free pawn)
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # checks if player clicked a mouse
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                # checks if it is his move now
                if human_move_now:
                    pos = pygame.mouse.get_pos()
                    for row in board:
                        for pawn in row:
                            rectangle = pawn.rectangle()
                            if rectangle.collidepoint(pos):
                                if pawn.value == '':
                                    return pawn

    def draw_main_window(self, board, human_player_value, pc_player_value):
        clock.tick(FPS)
        board_size = board.size()

        radius = WINDOW_SIZE / board_size
        size = radius - images_smaller_than_place
        LIGHT_CIRCLE = pygame.transform.scale(
            LIGHT_CIRCLE_IMAGE, (size, size))
        DARK_CIRCLE = pygame.transform.scale(DARK_CIRCLE_IMAGE, (size, size))
        BLANK_CIRCLE = pygame.transform.scale(BLANK_CIRCLE_IMAGE, (size, size))
        WIN.blit(self._BG, (0, 0))

        # draws pawns
        for i, row in enumerate(board.array):
            for j, pawn in enumerate(row):
                pawn_coords = self.pawn_coords(i, j)
                if pawn.value == pc_player_value:
                    new_pawns_rectangle = WIN.blit(DARK_CIRCLE,
                                                   pawn_coords)
                elif pawn.value == human_player_value:
                    new_pawns_rectangle = WIN.blit(LIGHT_CIRCLE,
                                                   pawn_coords)
                else:
                    new_pawns_rectangle = WIN.blit(BLANK_CIRCLE,
                                                   pawn_coords)
                pawn.set_rect(new_pawns_rectangle)

        pygame.display.update()

    def draw_start_window(self, board_size, ai_level, name, input_active):
        clock.tick(FPS)

        WIN.blit(BG_BLUR, (0, 0))

        middle = WIDTH / 2

        enter_name_y = 40
        draw_text_name = FONT_SMALL.render('Enter your name:', True, BLACK)
        text_rect_name = draw_text_name.get_rect()
        text_rect_name.center = (middle, enter_name_y)
        WIN.blit(draw_text_name, text_rect_name)

        input_image_y = enter_name_y + 30
        input = WIN.blit(INPUT, (middle - INPUT.get_width()/2, input_image_y))

        input_y = 100
        draw_text_input_active = FONT.render(
            f' {name} ', True, BLACK)
        text_rect_input_active = draw_text_input_active.get_rect()
        text_rect_input_active.center = (middle, input_y)
        WIN.blit(draw_text_input_active, text_rect_input_active)

        choose_board_y = 160
        draw_text_size = FONT_SMALL.render(
            'Choose board size:', True, BLACK)
        text_rect_size = draw_text_size.get_rect()
        text_rect_size.center = (middle, choose_board_y)
        WIN.blit(draw_text_size, text_rect_size)

        board_size_y = 210
        board_size_x_distane = 70

        draw_text_size_5 = FONT.render('5', True, BLACK)
        text_rect_size_5 = draw_text_size_5.get_rect()
        text_rect_size_5.center = (middle - board_size_x_distane, board_size_y)
        WIN.blit(draw_text_size_5, text_rect_size_5)

        draw_text_size_7 = FONT.render('7', True, BLACK)
        text_rect_size_7 = draw_text_size_7.get_rect()
        text_rect_size_7.center = (middle, board_size_y)
        WIN.blit(draw_text_size_7, text_rect_size_7)

        draw_text_size_9 = FONT.render('9', True, BLACK)
        text_rect_size_9 = draw_text_size_9.get_rect()
        text_rect_size_9.center = (middle + board_size_x_distane, board_size_y)
        WIN.blit(draw_text_size_9, text_rect_size_9)

        choose_ai_y = 260
        draw_text_ai = FONT_SMALL.render('Choose AI level:', True, BLACK)
        text_rect_ai = draw_text_ai.get_rect()
        text_rect_ai.center = (middle, choose_ai_y)
        WIN.blit(draw_text_ai, text_rect_ai)

        ai_level_y = 310

        draw_text_ai_easy = FONT.render('Easy', True, BLACK)
        text_rect_ai_easy = draw_text_ai_easy.get_rect()
        text_rect_ai_easy.center = (
            middle - draw_text_ai_easy.get_width() / 2 - 20, ai_level_y)
        WIN.blit(draw_text_ai_easy, text_rect_ai_easy)

        draw_text_ai_hard = FONT.render('Hard', True, BLACK)
        text_rect_ai_hard = draw_text_ai_hard.get_rect()
        text_rect_ai_hard.center = (
            middle + draw_text_ai_easy.get_width() / 2 + 20, ai_level_y)
        WIN.blit(draw_text_ai_hard, text_rect_ai_hard)

        play_button_y = 360
        play = WIN.blit(PLAY, (middle - PLAY.get_width() / 2, play_button_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                pos = pygame.mouse.get_pos()
                if input.collidepoint(pos):
                    input_active = not input_active
                elif text_rect_size_5.collidepoint(pos):
                    board_size = 5
                    input_active = False
                elif text_rect_size_7.collidepoint(pos):
                    board_size = 7
                    input_active = False
                elif text_rect_size_9.collidepoint(pos):
                    board_size = 9
                    input_active = False
                elif text_rect_ai_easy.collidepoint(pos):
                    ai_level = 0
                    input_active = False
                elif text_rect_ai_hard.collidepoint(pos):
                    ai_level = 1
                    input_active = False
                elif play.collidepoint(pos):
                    return True, name, board_size, ai_level, input_active

            if event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        input_edge = 55
                        if not text_rect_input_active.left < input_edge:
                            name += event.unicode

        pygame.display.update()
        return False, name, board_size, ai_level, input_active

    def draw_end(self, winner_name, board, human_player_value, pc_value):
        clock.tick(FPS)

        self.draw_main_window(board, human_player_value, pc_value)

        middle_y = self._bg_height() / 2
        middle_x = self._bg_width() / 2

        text_ending = FONT_BIG.render(f'{winner_name} won!', True, BLACK)
        draw_ending = text_ending.get_rect()

        # if text is widther than screen split it
        if draw_ending.width > self._bg_width():
            text_ending_name = FONT_BIG.render(f'{winner_name}', True, BLACK)
            draw_ending_name = text_ending_name.get_rect()
            text_ending_won = FONT_BIG.render('won!', True, BLACK)
            draw_ending_won = text_ending_won.get_rect()
            text_placement_y = 40
            draw_ending_name.center = middle_x, middle_y - text_placement_y
            draw_ending_won.center = middle_x, middle_y + text_placement_y
            WIN.blit(text_ending_name, draw_ending_name)
            WIN.blit(text_ending_won, draw_ending_won)
        else:
            draw_ending.center = middle_x, middle_y
            WIN.blit(text_ending, draw_ending)

        margin_y = 20
        margin_x = 20
        settings_x = middle_x - margin_x - SETTINGS.get_width()
        play_x = middle_x + margin_x
        both_y = self._bg_height() - margin_y - PLAY.get_height()
        settings = WIN.blit(
            SETTINGS, (settings_x, both_y))
        play = WIN.blit(
            PLAY, (play_x, both_y))

        if_new_settings = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                pos = pygame.mouse.get_pos()
                if settings.collidepoint(pos):
                    if_new_settings = True
                elif play.collidepoint(pos):
                    if_new_settings = False

        pygame.display.update()
        return if_new_settings

    def set_bg(self, board_size):
        """
        Sets background image and pawn's images sizes based on the BG.
        """
        if board_size == 7:
            self._BG = pygame.transform.scale(
                BG_IMAGE_7, (WINDOW_SIZE, WINDOW_SIZE))
        elif board_size == 9:
            self._BG = pygame.transform.scale(
                BG_IMAGE_9, (WINDOW_SIZE, WINDOW_SIZE))
        else:
            self._BG = pygame.transform.scale(
                BG_IMAGE_5, (WINDOW_SIZE, WINDOW_SIZE))
        self.pawn_image_size(board_size)

    def _bg_width(self):
        return self._BG.get_width()

    def _bg_height(self):
        return self._BG.get_height()

    def pawn_coords(self, row, column):
        """
        Returns pawn's image coordinations based on it's row and column numbers
        """
        image_size = self._pawns_image_size

        start = 3
        placement_correction = 6

        x = start + column * (image_size + placement_correction)
        y = start + row * (image_size + placement_correction)
        return x, y

    def pawn_image_size(self, board_size):
        """
        Sets a pawn image size based on the board size.
        """
        radius = self._bg_width() / board_size
        size = radius - images_smaller_than_place

        self._pawns_image_size = size
