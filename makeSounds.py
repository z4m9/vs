# https://github.com/chrisking1981/Aider-AI-Arkanoid-with-Multiplayer/commit/d7248a9998fd2ec1035093534690d7c3045d9dde
# This will generate the sounds internally and use them in the game without needing external sound files.
import pgzrun
import pygame
import random
import numpy
import time

wave = numpy.array([[1,1], [2,2], [3,3]], dtype="int8")
pygame.sndarray.make_sound(wave)

# Generate sounds
def generate_sound(frequency, duration, volume=0.5, sample_rate=44100):
    t = numpy.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 32767 * volume * numpy.sin(2 * numpy.pi * frequency * t)
    sound_array1 = numpy.array(wave, dtype=numpy.int8)
    #audio = np.sin(2 * np.pi * 1800 * t)
    audio = numpy.repeat(sound_array1.reshape(sound_array1.shape[0], 1), 2, axis=1)
    return pygame.sndarray.make_sound(audio)

print('mixer init=', pygame.mixer.get_init())


paddle_hit_sound = generate_sound(440, 0.1)
brick_hit_sound = generate_sound(880, 0.1)
game_over_sound = generate_sound(220, 0.5)



#https://stackoverflow.com/questions/64950167/trying-to-play-a-sound-wave-on-python-using-pygame
pygame.mixer.init(frequency=44100, size=-16, channels=1)

size = 44100
buffer = numpy.random.randint(-32768, 32767, size)
buffer = numpy.repeat(buffer.reshape(size, 1), 2, axis = 1)
# alternate
#buffer = np.random.randint(-32768, 32767, size*2)
#buffer = buffer.reshape(size, 2)

#sound = pygame.sndarray.make_sound(buffer)
# sound.play()
#pygame.time.wait(int(sound.get_length() * 1000))

#https://discuss.python.org/t/pygame-valueerror-array-must-be-2-dimensional-for-stereo-mixer/42437
#You can force the mixer to use mono by calling:
pygame.mixer.pre_init(channels=1, allowedchanges=0)

def generate_beep(freq, duration, samplerate=44100):
    t = numpy.linspace(0, duration, int(samplerate * duration))
    audio = numpy.sin(2 * numpy.pi * freq * t)
    audio = numpy.repeat(audio.reshape(audio.shape[0], 1), 2, axis=1)
    return audio.astype(numpy.int16)

while True:
    beep = generate_beep(440, 0.25, 44100)
    sound = pygame.sndarray.make_sound(beep)
    sound.play()
    time.sleep(1)


pgzrun.go()
