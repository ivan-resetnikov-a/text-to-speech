import speech

from tkinter import ttk as gui, Tk, Text, StringVar



class Application :
	def __init__ (self) :
		self.root = Tk()
		self.root.resizable(0, 0)
		self.root.title('Text To Speech | V 1.0')

		self.voices = ['female', 'male', 'female']
		self.voice  = StringVar()


	def say (self) :
		speech.say(
			text=self.text.get('1.0', 'end-1c'),
			voice=self.voice.get())


	def save (self) :
		pass


	def start (self) :
		self.text = Text(width=50, height=10, font=('Century Gothic', 10))
		self.text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


		self.speakFrame = gui.LabelFrame(text='speak')
		self.speakFrame.grid(row=1, column=0, padx=10, pady=10)

		self.settingsFrame = gui.LabelFrame(text='settings')
		self.settingsFrame.grid(row=1, column=1, padx=10, pady=10)
		

		gui.Button(self.speakFrame, text='Say', width=25, command=self.say).grid(row=0, column=0, padx=10, pady=10)
		gui.Button(self.speakFrame, text='Save as mp3', width=25, command=self.save).grid(row=1, column=0, padx=10, pady=10)
		

		gui.OptionMenu(self.settingsFrame, self.voice, *self.voices).grid(row=0, column=0, padx=10, pady=10)

		self.root.mainloop()



if __name__ == '__main__' :
	Application().start()
	speech.quit()