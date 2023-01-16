import sys
from api_communication import *

# upload


filename = sys.argv[1]

audio_url = upload(filename)
save_transcript(filename, audio_url)
