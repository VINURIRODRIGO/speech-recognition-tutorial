# Install ffmpeg -> extract ffmpeg.7z file and add it to the c drive. then add the bin path to the edit environment variables path section.
from pydub import AudioSegment# pip install pydub (NOTE: first need to install ffmpeg)


audio = AudioSegment.from_wav("output.wav")

#increase the volume by 6dB
audio = audio + 6

audio = audio * 2

audio = audio.fade_in(2000)

audio.export("mashup.mp3", format="mp3")

audio2 = AudioSegment.from_mp3("mashup.mp3")
print("done")
