import pygame

class Sound(object):

    # 'sounds' - a list of tuples of the format (sound ID, sound filename)
    # Result - 'loaded_sounds' is populated with sound data for the given 'sounds'
    @classmethod
    def load_sounds(cls, sounds):
        cls.loaded_sounds.clear()

        for sound_tuple_to_load in sounds:
            sound_id = sound_tuple_to_load[cls.sound_tuple_index_sound_id]
            sound_filename = sound_tuple_to_load[cls.sound_tuple_index_sound_filename]
            sound = pygame.mixer.Sound(sound_filename)

            cls.loaded_sounds[sound_id] = (sound_id, sound_filename, sound)

    @classmethod
    def play_sound_for_sound_id(cls, sound_id):
        sound = cls.sound_for_sound_id(sound_id)
        sound.play()

    @classmethod
    def stop_sound_for_sound_id(cls, sound_id):
        sound = cls.sound_for_sound_id(sound_id)
        sound.stop()

    # keys - sound IDs
    # values - sound tuples of the format (sound ID, sound filename, Sound object)
    loaded_sounds = {}

    # sound tuple value indices
    sound_tuple_index_sound_id       = 0
    sound_tuple_index_sound_filename = 1
    sound_tuple_index_sound          = 2

    @classmethod
    def start(cls):
        pygame.mixer.init()

    @classmethod
    def stop(cls):
        pygame.mixer.quit()

    @classmethod
    def sound_tuple_for_sound_id(cls, sound_id):
        sound_tuple = cls.loaded_sounds[sound_id]
        return sound_tuple

    @classmethod
    def sound_for_sound_id(cls, sound_id):
        sound_tuple = cls.sound_tuple_for_sound_id(sound_id)
        sound = sound_tuple[cls.sound_tuple_index_sound]
        return sound

    @classmethod
    def test_sounds(cls):
        sound_id = "test"
        sound_filename = "../../resources/sounds/test.ogg"
        sounds = [(sound_id, sound_filename)]
        cls.load_sounds(sounds)
        cls.play_sound_for_sound_id(sound_id)
        for x in xrange(1,50000000):
            pass

if __name__ == '__main__':
    Sound.start()
    Sound.test_sounds()
    Sound.stop()
