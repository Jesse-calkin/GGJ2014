import pygame


"Public"

# 'sounds' - a list of tuples of the format (sound ID, sound filename)
# Result - 'loaded_sounds' is populated with sound data for the given 'sounds'
def load_sounds(sounds):
    global loaded_sounds

    loaded_sounds = {}

    for sound_tuple_to_load in sounds:
        sound_id = sound_tuple_to_load[sound_tuple_index_sound_id]
        sound_filename = sound_tuple_to_load[sound_tuple_index_sound_filename]
        sound = pygame.mixer.Sound(sound_filename)

        loaded_sounds[sound_id] = (sound_id, sound_filename, sound)

def play_sound_for_sound_id(sound_id):
    sound = sound_for_sound_id(sound_id)
    sound.play()

def stop_sound_for_sound_id(sound_id):
    sound = sound_for_sound_id(sound_id)
    sound.stop()


"Private"

# keys - sound IDs
# values - sound tuples of the format (sound ID, sound filename, Sound object)
loaded_sounds = {}

# sound tuple value indices
sound_tuple_index_sound_id       = 0
sound_tuple_index_sound_filename = 1
sound_tuple_index_sound          = 2

def start():
    pygame.mixer.init()

def stop():
    pygame.mixer.quit()

def sound_tuple_for_sound_id(sound_id):
    sound_tuple = loaded_sounds[sound_id]
    return sound_tuple

def sound_for_sound_id(sound_id):
    sound_tuple = sound_tuple_for_sound_id(sound_id)
    sound = sound_tuple[sound_tuple_index_sound]
    return sound


"Test"

def test_sounds():
    sound_id = "test"
    sound_filename = "../../resources/sounds/test.ogg"
    sounds = [(sound_id, sound_filename)]
    load_sounds(sounds)
    play_sound_for_sound_id(sound_id)
    for x in xrange(1,50000000):
        pass


"Main"

start()
test_sounds()
stop()
