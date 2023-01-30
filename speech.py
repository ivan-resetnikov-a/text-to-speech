from pyttsx3   import init as TextToSpeech
from threading import Thread


TTS = TextToSpeech()

# asssign "male" to TTS's voice with id 0
# asssign "female" to TTS's voice with id 1
VOICES = {
	'male'  : TTS.getProperty('voices')[0],
	'female': TTS.getProperty('voices')[1]}



def say (text, voice:str='female', volume:int=1, rate:int=150) :
	# apply prefered settings
	TTS.setProperty('voice' , VOICES[voice])
	TTS.setProperty('volume', volume)
	TTS.setProperty('rate'  , rate)

	TTS.say(text)

	# say the text
	def say () :
		try : 
			TTS.runAndWait()
		except RuntimeError :
			print('Error: voice already in use')

	Thread(target=say).start()
	


def save (text, voice:str='female', volume:int=1, rate:int=200) :
	# apply prefered settings
	TTS.setProperty('voice' , VOICES[voice])
	TTS.setProperty('volume', volume)
	TTS.setProperty('rate'  , rate)

	# save as .mp3
	TTS.save_to_file('Hello World', f'{path}.mp3')



def quit () : TTS.stop()