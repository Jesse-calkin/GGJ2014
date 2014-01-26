import pygame

class Level(object):
    def __init__(self):
        super(Level, self).__init__()

        # Gameplay
        self.gravity = pygame.math.Vector2(0, 0)
        self.powerups_goal = 1

        # Images
        self.near_background_image_name = "../../resources/backgrounds/testforeground.png"
        self.far_background_image_name = "../../resources/backgrounds/primordial.jpg"

        # Sounds
        self.move_sound_id = None
        self.move_sound_filename = "../../resources/sounds/swish.ogg"

    # Level progression

    @classmethod
    def first_level(cls):
        all_levels = Level.all_levels()
        first_level = all_levels[0]
        return first_level

    @classmethod
    def last_level(cls):
        all_levels = Level.all_levels()
        number_of_levels = len(all_levels)
        last_level_index = number_of_levels - 1
        last_level = all_levels[last_level_index]
        return last_level

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

    _amoeba_level = None
    @classmethod
    def amoeba_level(cls):
        if (cls._amoeba_level == None):
            cls._amoeba_level = Level()
            cls._amoeba_level.gravity = pygame.math.Vector2(0, 0)
            cls._amoeba_level.powerups_goal = 5
            cls._amoeba_level.move_sound_id = "amoeba_move_sound_id"
        return cls._amoeba_level

    _fish_level = None
    @classmethod
    def fish_level(cls):
        if (cls._fish_level == None):
            cls._fish_level = Level()
            cls._fish_level.gravity = pygame.math.Vector2(0, -1)
            cls._fish_level.powerups_goal = 10
            cls._fish_level.move_sound_id = "fish_move_sound_id"
        return cls._fish_level

    _dinosaur_level = None
    @classmethod
    def dinosaur_level(cls):
        if (cls._dinosaur_level == None):
            cls._dinosaur_level = Level()
            cls._dinosaur_level.gravity = pygame.math.Vector2(0, 3.5)
            cls._dinosaur_level.powerups_goal = 15
            cls._dinosaur_level.move_sound_id = "dinosaur_move_sound_id"
        return cls._dinosaur_level

    _dragon_level = None
    @classmethod
    def dragon_level(cls):
        if (cls._dragon_level == None):
            cls._dragon_level = Level()
            cls._dragon_level.gravity = pygame.math.Vector2(0, 1)
            cls._dragon_level.powerups_goal = 20
            cls._dragon_level.move_sound_id = "dragon_move_sound_id"
        return cls._dragon_level

if __name__ == '__main__':
    level = Level.first_level()
    while (True):
        print(level)
        level = level.next_level()
        if (level == None):
            break
