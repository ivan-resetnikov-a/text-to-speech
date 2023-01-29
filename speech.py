from pyttsx3   import init as TextToSpeech



TTS = TextToSpeech()
TTS.voices = TTS.getProperty('voices')

# asssign "male" to TTS's voice with id 0
# asssign "female" to TTS's voice with id 1
VOICES = {'male': TTS.voices[0], 'female': TTS.voices[1]}



def say (text, voice:str='female', volume:int=1, rate:int=150) :
	# apply prefered settings
	TTS.setProperty('voice' , VOICES[voice])
	TTS.setProperty('volume', volume)
	TTS.setProperty('rate'  , rate)

	# say the text
	TTS.say(text)
	Thread(target=TTS.runAndWait).start()


def sayAndSave (text, voice:str='female', volume:int=1, rate:int=200) :
	# apply prefered settings
	TTS.setProperty('voice' , VOICES[voice])
	TTS.setProperty('volume', volume)
	TTS.setProperty('rate'  , rate)

	# save as .mp3
	TTS.save_to_file('Hello World', f'{path}.mp3')