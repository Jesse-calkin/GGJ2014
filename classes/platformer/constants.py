"""
Global constants
"""

#Global Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FRAME_RATE = 60

#Colors!
BLACK = (000, 000, 000)
WHITE = (255, 255, 255)
RED = (255, 000, 000)
ORANGE = (255, 165, 000)
YELLOW = (255, 255, 000)
GREEN = (000, 255, 000)
BLUE = (000, 000, 255)
INDIGO = (75, 000, 130)
VIOLET = (143, 000, 255)
TASTE_THE_RAINBOW = [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET]

# Sounds
sound_id_eat = "eat"
sound_tuple_eat = (sound_id_eat, "resources/sounds/chomp.wav", 1)

sound_id_evolve = "evolve"
sound_tuple_evolve = (sound_id_evolve, "resources/sounds/evolve.wav", 2)

# Die sounds
sound_id_amoeba_die = "amoeba_die"
sound_tuple_amoeba_die = (sound_id_amoeba_die, "resources/sounds/Ameoba_dies.wav", 3)

sound_id_fish_die = "fish_die"
sound_tuple_fish_die = (sound_id_fish_die, "resources/sounds/ameoba_move_2.wav", 3)

sound_id_dinosaur_die = "dinosaur_die"
sound_tuple_dinosaur_die = (sound_id_dinosaur_die, "resources/sounds/ameoba_move_2.wav", 3)

sound_id_dragon_die = "dragon_die"
sound_tuple_dragon_die = (sound_id_dragon_die, "resources/sounds/ameoba_move_2.wav", 3)

# Move sounds
sound_id_amoeba_move = "amoeba_move"
sound_tuple_amoeba_move = (sound_id_amoeba_move, "resources/sounds/ameoba_move_2.wav", 4)

sound_id_fish_move = "fish_move"
sound_tuple_fish_move = (sound_id_fish_move, "resources/sounds/Fish_move_1.wav", 4)

sound_id_dinosaur_move = "dinosaur_move"
sound_tuple_dinosaur_move = (sound_id_dinosaur_move, "resources/sounds/dino_jump_4.wav", 4)

sound_id_dragon_move = "dragon_move"
sound_tuple_dragon_move = (sound_id_dragon_move, "resources/sounds/Dragon_move_wingbeat_roar.wav", 4)

all_sounds_to_load = [sound_tuple_eat, sound_tuple_evolve, sound_tuple_amoeba_die, sound_tuple_fish_die, sound_tuple_dinosaur_die, sound_tuple_dragon_die, sound_tuple_amoeba_move, sound_tuple_fish_move, sound_tuple_dinosaur_move, sound_tuple_dragon_move]
