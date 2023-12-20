import sys
import requests
from api import *

filename = sys.argv[1]
audio_url = upload(filename)

save_transcript(audio_url, 'file_title')