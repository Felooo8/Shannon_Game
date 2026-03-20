"""Pygame window management for the Shannon game."""

from __future__ import annotations

import os
from pathlib import Path

try:
    import pygame
except ModuleNotFoundError:  # pragma: no cover - exercised in minimal CI environments
    pygame = None

FPS = 20
WINDOW_SIZE = 450
WINDOW_TITLE = "Shannon Game by Felo"
ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREY = (220, 220, 220)


if pygame is None:
    class _DummyRect:
        def collidepoint(self, _pos) -> bool:
            return False

    class Window:
        """Minimal fallback used when pygame is unavailable during tests."""

        def __init__(self) -> None:
            self._pawns_image_size = int(WINDOW_SIZE / 5) - 6
            self._bg_size = WINDOW_SIZE

        def handle_events(self, board, human_move_now):  # noqa: ARG002
            return None

        def draw_main_window(self, board, human_player_value, pc_player_value):  # noqa: ARG002
            for row in board.array:
                for pawn in row:
                    pawn.set_rect(_DummyRect())

        def draw_start_window(self, board_size, ai_level, name, input_active):
            return False, name, board_size, ai_level, input_active

        def draw_end(self, winner_name, board, human_player_value, pc_value):  # noqa: ARG002
            return None

        def set_bg(self, board_size):
            self.pawn_image_size(board_size)

        def _bg_width(self):
            return self._bg_size

        def _bg_height(self):
            return self._bg_size

        def pawn_coords(self, row, column):
            image_size = self._pawns_image_size
            start = 3
            placement_correction = 6
            x = start + column * (image_size + placement_correction)
            y = start + row * (image_size + placement_correction)
            return x, y

        def pawn_image_size(self, board_size):
            radius = self._bg_width() / board_size
            self._pawns_image_size = int(radius - 6)

else:
    def _configure_headless_environment() -> None:
        """Use pygame's dummy video driver when no display is available."""
        if os.name != "nt" and "DISPLAY" not in os.environ:
            os.environ.setdefault("SDL_VIDEODRIVER", "dummy")


    class Window:
        """Manage rendering and event handling for the game window."""

        def __init__(self) -> None:
            _configure_headless_environment()
            pygame.init()
            pygame.font.init()

            self.clock = pygame.time.Clock()
            self.images_smaller_than_place = 6
            self._load_assets()
            self._BG = self.backgrounds[5]
            self._pawns_image_size = self._default_pawn_image_size(5)

        def _asset_path(self, name: str) -> str:
            return str(ASSETS_DIR / name)

        def _load_assets(self) -> None:
            self.backgrounds = {
                size: pygame.transform.scale(
                    pygame.image.load(self._asset_path(f"board_{size}.png")),
                    (WINDOW_SIZE, WINDOW_SIZE),
                )
                for size in (5, 7, 9)
            }
            self.bg_blur = pygame.transform.scale(
                pygame.image.load(self._asset_path("board_blur.png")),
                (WINDOW_SIZE, WINDOW_SIZE),
            )

            icon_size = (64, 64)
            program_icon = pygame.transform.scale(
                pygame.image.load(self._asset_path("icon.png")), icon_size
            )

            self.WIN = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
            pygame.display.set_caption(WINDOW_TITLE)
            pygame.display.set_icon(program_icon)

            self.font = pygame.font.Font(self._asset_path("COMIC.TTF"), 40)
            self.font_small = pygame.font.Font(self._asset_path("COMIC.TTF"), 30)
            self.font_big = pygame.font.Font(self._asset_path("COMIC.TTF"), 80)

            self.input_surface = pygame.transform.scale(
                pygame.image.load(self._asset_path("input.png")),
                (WINDOW_SIZE - 50, 70),
            )
            self.play_base = pygame.image.load(self._asset_path("play.png"))
            self.settings_base = pygame.image.load(self._asset_path("settings.png"))
            self.light_base = pygame.image.load(self._asset_path("piece_light.png"))
            self.dark_base = pygame.image.load(self._asset_path("piece_dark.png"))
            self.blank_base = pygame.image.load(self._asset_path("piece_blank.png"))

            default_size = self._default_pawn_image_size(5)
            self._set_scaled_images(default_size)

        def _default_pawn_image_size(self, board_size: int) -> int:
            radius = WINDOW_SIZE / board_size
            return int(radius - self.images_smaller_than_place)

        def _set_scaled_images(self, size: int) -> None:
            self.play_image = pygame.transform.scale(self.play_base, (size, size))
            self.settings_image = pygame.transform.scale(self.settings_base, (size, size))
            self.light_circle = pygame.transform.scale(self.light_base, (size, size))
            self.dark_circle = pygame.transform.scale(self.dark_base, (size, size))
            self.blank_circle = pygame.transform.scale(self.blank_base, (size, size))

        def handle_events(self, board, human_move_now):
            """Handle player input during gameplay and return a chosen pawn if any."""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and human_move_now:
                    pos = pygame.mouse.get_pos()
                    for row in board:
                        for pawn in row:
                            rectangle = pawn.rectangle()
                            if rectangle.collidepoint(pos) and pawn.value == "":
                                return pawn
            return None

        def draw_main_window(self, board, human_player_value, pc_player_value):
            self.clock.tick(FPS)
            board_size = board.size()

            size = self._default_pawn_image_size(board_size)
            self._set_scaled_images(size)
            self.WIN.blit(self._BG, (0, 0))

            for i, row in enumerate(board.array):
                for j, pawn in enumerate(row):
                    pawn_coords = self.pawn_coords(i, j)
                    if pawn.value == pc_player_value:
                        new_pawns_rectangle = self.WIN.blit(self.dark_circle, pawn_coords)
                    elif pawn.value == human_player_value:
                        new_pawns_rectangle = self.WIN.blit(self.light_circle, pawn_coords)
                    else:
                        new_pawns_rectangle = self.WIN.blit(self.blank_circle, pawn_coords)
                    pawn.set_rect(new_pawns_rectangle)

            pygame.display.update()

        def draw_start_window(self, board_size, ai_level, name, input_active):
            self.clock.tick(FPS)
            self.WIN.blit(self.bg_blur, (0, 0))

            middle = WINDOW_SIZE / 2

            enter_name_y = 40
            draw_text_name = self.font_small.render("Enter your name:", True, BLACK)
            text_rect_name = draw_text_name.get_rect()
            text_rect_name.center = (middle, enter_name_y)
            self.WIN.blit(draw_text_name, text_rect_name)

            input_image_y = enter_name_y + 30
            input_box = self.WIN.blit(
                self.input_surface, (middle - self.input_surface.get_width() / 2, input_image_y)
            )

            input_y = 100
            draw_text_input_active = self.font.render(f" {name} ", True, BLACK)
            text_rect_input_active = draw_text_input_active.get_rect()
            text_rect_input_active.center = (middle, input_y)
            self.WIN.blit(draw_text_input_active, text_rect_input_active)

            choose_board_y = 160
            draw_text_size = self.font_small.render("Choose board size:", True, BLACK)
            text_rect_size = draw_text_size.get_rect()
            text_rect_size.center = (middle, choose_board_y)
            self.WIN.blit(draw_text_size, text_rect_size)

            board_size_y = 210
            board_size_x_distance = 70

            draw_text_size_5 = self.font.render("5", True, BLACK)
            text_rect_size_5 = draw_text_size_5.get_rect()
            text_rect_size_5.center = (middle - board_size_x_distance, board_size_y)
            self.WIN.blit(draw_text_size_5, text_rect_size_5)

            draw_text_size_7 = self.font.render("7", True, BLACK)
            text_rect_size_7 = draw_text_size_7.get_rect()
            text_rect_size_7.center = (middle, board_size_y)
            self.WIN.blit(draw_text_size_7, text_rect_size_7)

            draw_text_size_9 = self.font.render("9", True, BLACK)
            text_rect_size_9 = draw_text_size_9.get_rect()
            text_rect_size_9.center = (middle + board_size_x_distance, board_size_y)
            self.WIN.blit(draw_text_size_9, text_rect_size_9)

            choose_ai_y = 260
            draw_text_ai = self.font_small.render("Choose AI level:", True, BLACK)
            text_rect_ai = draw_text_ai.get_rect()
            text_rect_ai.center = (middle, choose_ai_y)
            self.WIN.blit(draw_text_ai, text_rect_ai)

            ai_level_y = 310
            draw_text_ai_easy = self.font.render("Easy", True, BLACK)
            text_rect_ai_easy = draw_text_ai_easy.get_rect()
            text_rect_ai_easy.center = (middle - draw_text_ai_easy.get_width() / 2 - 20, ai_level_y)
            self.WIN.blit(draw_text_ai_easy, text_rect_ai_easy)

            draw_text_ai_hard = self.font.render("Hard", True, BLACK)
            text_rect_ai_hard = draw_text_ai_hard.get_rect()
            text_rect_ai_hard.center = (middle + draw_text_ai_easy.get_width() / 2 + 20, ai_level_y)
            self.WIN.blit(draw_text_ai_hard, text_rect_ai_hard)

            play_button_y = 360
            play = self.WIN.blit(self.play_image, (middle - self.play_image.get_width() / 2, play_button_y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if input_box.collidepoint(pos):
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

                if event.type == pygame.KEYDOWN and input_active:
                    if event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        input_edge = 55
                        if not text_rect_input_active.left < input_edge:
                            name += event.unicode

            pygame.display.update()
            return False, name, board_size, ai_level, input_active

        def draw_end(self, winner_name, board, human_player_value, pc_value):
            self.clock.tick(FPS)
            self.draw_main_window(board, human_player_value, pc_value)

            middle_y = self._bg_height() / 2
            middle_x = self._bg_width() / 2

            text_ending = self.font_big.render(f"{winner_name} won!", True, BLACK)
            draw_ending = text_ending.get_rect()

            if draw_ending.width > self._bg_width():
                text_ending_name = self.font_big.render(f"{winner_name}", True, BLACK)
                draw_ending_name = text_ending_name.get_rect()
                text_ending_won = self.font_big.render("won!", True, BLACK)
                draw_ending_won = text_ending_won.get_rect()
                text_placement_y = 40
                draw_ending_name.center = middle_x, middle_y - text_placement_y
                draw_ending_won.center = middle_x, middle_y + text_placement_y
                self.WIN.blit(text_ending_name, draw_ending_name)
                self.WIN.blit(text_ending_won, draw_ending_won)
            else:
                draw_ending.center = middle_x, middle_y
                self.WIN.blit(text_ending, draw_ending)

            margin_y = 20
            margin_x = 20
            settings_x = middle_x - margin_x - self.settings_image.get_width()
            play_x = middle_x + margin_x
            both_y = self._bg_height() - margin_y - self.play_image.get_height()
            settings = self.WIN.blit(self.settings_image, (settings_x, both_y))
            play = self.WIN.blit(self.play_image, (play_x, both_y))

            if_new_settings = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if settings.collidepoint(pos):
                        if_new_settings = True
                    elif play.collidepoint(pos):
                        if_new_settings = False

            pygame.display.update()
            return if_new_settings

        def set_bg(self, board_size):
            """Set the board background and pawn sizes for the selected board."""
            self._BG = self.backgrounds.get(board_size, self.backgrounds[5])
            self.pawn_image_size(board_size)

        def _bg_width(self):
            return self._BG.get_width()

        def _bg_height(self):
            return self._BG.get_height()

        def pawn_coords(self, row, column):
            """Return image coordinates for the pawn at the given row and column."""
            image_size = self._pawns_image_size
            start = 3
            placement_correction = 6
            x = start + column * (image_size + placement_correction)
            y = start + row * (image_size + placement_correction)
            return x, y

        def pawn_image_size(self, board_size):
            """Cache a pawn image size based on the current board size."""
            size = self._default_pawn_image_size(board_size)
            self._pawns_image_size = size
            self._set_scaled_images(size)
