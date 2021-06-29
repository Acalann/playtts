from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from os import remove


def savetts(whatosay, filetosaveto):
    tts = gTTS(whatosay)
    tts.save(filetosaveto + '.mp3')
    quit()


def playtts(whatosay):
    tts = gTTS(whatosay)
    tts.save('tmp.mp3')
    sound = AudioSegment.from_mp3('tmp.mp3')
    play(sound)
    remove('tmp.mp3')
    quit()
