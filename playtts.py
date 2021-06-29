from gtts import gTTS


def playtts(whatosay, filetosaveto):
    while True:
        tts = gTTS(whatosay)
        tts.save(filetosaveto + '.mp3')
        quit()
