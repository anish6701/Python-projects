'''
#Convert Text to Speech in Python
'''
# Import the required module for text
# to speech conversion
from gtts import gTTS
# This module is imported so that we can
# play the converted audio
import os
# The text that you want to convert to audio
mytext = input('Enter the text you want to hear : ')
# Language in which you want to convert
language = 'en'
# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
input(myobj.save("Testing.mp3"))