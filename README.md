# Speech_Recognition-in-Python

This Python script provides a simple interface to interact with the AssemblyAI API for audio transcription. It allows you to upload an audio file, initiate transcription, and save the resulting transcript to a text file.

Prerequisites
Python 3.x
Requests library (pip install requests)
AssemblyAI API key (obtainable from AssemblyAI)
Usage
Clone this repository:

bash
Copy code
git clone https://github.com/your-username/assemblyai-transcription-script.git
Install the required dependencies:

bash
Copy code
pip install requests
Obtain an AssemblyAI API key from AssemblyAI.

Create a file named api_id.py in the project directory and define your API key:

python
Copy code
# api_id.py
API_KEY_ASSEMBLYAI = 'your-assemblyai-api-key'
Run the script with the audio file you want to transcribe:

bash
Copy code
python transcription_script.py your_audio_file.mp3
Functions
1. upload(filename)
Uploads an audio file in chunks and returns the upload URL.

2. transcribe(audio_url)
Initiates transcription using the provided audio URL.

3. poll_transcription_status(transcript_id)
Polls the transcription status using the transcript ID.

4. get_transcription_result_url(url)
Initiates transcription and waits for completion or error, then returns the transcription data or error.

5. save_transcript(url, title)
Saves the transcript to a text file.

Configuration
CHUNK_SIZE: Adjust the chunk size for uploading the audio file in the script.
HEADERS_AUTH_ONLY: Use this header for uploading.
HEADERS: Use this header for transcription requests.
Notes
Ensure proper handling of API key security.
Check the AssemblyAI API documentation for any updates or changes.
