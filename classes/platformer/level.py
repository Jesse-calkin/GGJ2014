import pygame

class Level(object):
    # Gameplay
    gravity = pygame.math.Vector2(0, 0)
    powerups_goal = 1

    # Images

    # Sounds
    move_sound_id = None
    move_sound_filename = "../../resources/sounds/swish.ogg"

    # Level progression.
    def next_level(self):
        next_level = None

        all_levels = Level.all_levels()
        number_of_levels = len(all_levels)

        current_level_index = all_levels.index(self)
        next_level_index = current_level_index + 1

        if (next_level_index < number_of_levels):
            next_level = all_levels[next_level_index]

        return next_level

    # Factories

    @classmethod
    def all_levels(cls):
        all_levels = [Level.amoeba_level(), Level.fish_level(), Level.dinosaur_level(), Level.dragon_level()]
        return all_levels

    @classmethod
    def amoeba_level(cls):
        amoeba_level = Level()

        amoeba_level.gravity = pygame.math.Vector2(0, 0)
        amoeba_level.powerups_goal = 5

        amoeba_level.move_sound_id = "amoeba_move_sound_id"

        return amoeba_level

    @classmethod
    def fish_level(cls):
        fish_level = Level()

        fish_level.gravity = pygame.math.Vector2(0, -1)
        fish_level.powerups_goal = 10

        fish_level.move_sound_id = "fish_move_sound_id"

        return fish_level

    @classmethod
    def dinosaur_level(cls):
        dinosaur_level = Level()

        dinosaur_level.gravity = pygame.math.Vector2(0, 3.5)
        dinosaur_level.powerups_goal = 15

        dinosaur_level.move_sound_id = "dinosaur_move_sound_id"

        return dinosaur_level

    @classmethod
    def dragon_level(cls):
        dragon_level = Level()

        dragon_level.gravity = pygame.math.Vector2(0, 1)
        dragon_level.powerups_goal = 20

        dragon_level.move_sound_id = "dragon_move_sound_id"

        return dragon_level
