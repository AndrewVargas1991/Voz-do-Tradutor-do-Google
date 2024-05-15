#pip install gtts
from gtts import gTTS
import os

def voz():
	texto = input('Digite o que você quer ouvir: ')
	audio = gTTS(text=texto, lang="pt-br", slow=False)
	audio.save("áudio.mp3")
	os.system("áudio.mp3")

while True:
	voz()