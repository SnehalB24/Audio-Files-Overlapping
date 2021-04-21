 # convert mp3 file to wav file

from pydub import AudioSegment
  
mp3_audio1 = "audio1.mp3"
wav_audio1 = "Sound1.wav"

mp3_audio2 = "audio2.mp3"
wav_audio2 = "Sound2.wav"
  
music1= AudioSegment.from_mp3(mp3_audio1)
music1.export(wav_audio1, format="wav")

music2= AudioSegment.from_mp3(mp3_audio2)
music2.export(wav_audio2, format="wav")

# Overlapping of audio

from pydub import AudioSegment

music1 = AudioSegment.from_file("Sound1.wav")
music2 = AudioSegment.from_file("Sound2.wav")

combined = music1.overlay(music2)

combined.export("Mixed.wav", format='wav')

# Play the music

from playsound import playsound
playsound('Mixed.wav')
