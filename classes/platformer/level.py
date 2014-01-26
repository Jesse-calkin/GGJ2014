import pygame

class Level(object):
    def __init__(self):
        super(Level, self).__init__()

        # Gameplay
        self.gravity = pygame.math.Vector2(0, 0)
        self.target_score = 1
        self.has_blocks = False
        self.hazard_start_location = None

        # Images
        self.background_filepath = "resources/backgrounds/testforeground.png"
        self.foreground_filepath = "resources/backgrounds/primordial.jpg"
        self.hazard_filepath = None

        # Sounds
        self.move_sound_id = None
        self.move_sound_filename = "resources/sounds/swish.ogg"

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
        else:
            next_level = Level.first_level()

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
            cls._amoeba_level.target_score = 10
            cls._amoeba_level.move_sound_id = "amoeba_move_sound_id"
            cls._amoeba_level.background_filepath = 'resources/backgrounds/primordial.jpg'
            cls._amoeba_level.foreground_filepath = 'resources/backgrounds/amoebaforeground.png'
            cls._amoeba_level.player_sprite_filepath = 'resources/sprites/Amoeba.png'
            cls._amoeba_level.player_textmap_filepath = 'resources/sprites/Amoeba.json'
        return cls._amoeba_level

    _fish_level = None
    @classmethod
    def fish_level(cls):
        if (cls._fish_level == None):
            cls._fish_level = Level()
            cls._fish_level.gravity = pygame.math.Vector2(0, -1)
            cls._fish_level.target_score = 15
            cls._fish_level.hazard_start_location = 'bottom'
            cls._fish_level.move_sound_id = "fish_move_sound_id"
            cls._fish_level.background_filepath = 'resources/backgrounds/sea_modernearth.jpg'
            cls._fish_level.foreground_filepath = 'resources/backgrounds/bubblesforeground.png'
            cls._fish_level.player_sprite_filepath='resources/sprites/Fish.png'
            cls._fish_level.hazard_filepath = 'resources/sprites/pac.png'
            cls._fish_level.player_textmap_filepath='resources/sprites/Fish.json'
        return cls._fish_level

    _dinosaur_level = None
    @classmethod
    def dinosaur_level(cls):
        if (cls._dinosaur_level == None):
            cls._dinosaur_level = Level()
            cls._dinosaur_level.gravity = pygame.math.Vector2(0, 3.5)
            cls._dinosaur_level.target_score = 20
            cls._dinosaur_level.has_blocks = True
            cls._dinosaur_level.move_sound_id = "dinosaur_move_sound_id"
            cls._dinosaur_level.background_filepath = 'resources/backgrounds/land_earlyearth.jpg'
            cls._dinosaur_level.foreground_filepath = 'resources/backgrounds/mountains.png'
            cls._dinosaur_level.player_sprite_filepath='resources/sprites/Dinosaur.png'
            cls._dinosaur_level.player_textmap_filepath='resources/sprites/Dinosaur.json'
        return cls._dinosaur_level

    _dragon_level = None
    @classmethod
    def dragon_level(cls):
        if (cls._dragon_level == None):
            cls._dragon_level = Level()
            cls._dragon_level.gravity = pygame.math.Vector2(0, 1)
            cls._dragon_level.target_score = 25
            cls._dragon_level.has_blocks = True
            cls._dragon_level.hazard_start_location = 'bottom_rotate'
            cls._dragon_level.move_sound_id = "dragon_move_sound_id"
            cls._dragon_level.background_filepath = 'resources/backgrounds/aerial.jpg'
            cls._dragon_level.foreground_filepath = 'resources/backgrounds/cloudforeground.png'
            cls._dragon_level.player_sprite_filepath='resources/sprites/Proto.png'
            cls._dragon_level.hazard_filepath = 'resources/sprites/pac.png'
            cls._dragon_level.player_textmap_filepath='resources/sprites/Proto.json'
        return cls._dragon_level
