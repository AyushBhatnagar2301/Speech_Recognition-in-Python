import requests
import time
from api_id import API_KEY_ASSEMBLYAI

UPLOAD_ENDPOINT = 'https://api.assemblyai.com/v2/upload'
TRANSCRIPT_ENDPOINT = 'https://api.assemblyai.com/v2/transcript'

HEADERS_AUTH_ONLY = {'authorization': API_KEY_ASSEMBLYAI}

HEADERS = {
    "authorization": API_KEY_ASSEMBLYAI,
    "content-type": "application/json"
}

CHUNK_SIZE = 5_242_880  # 5MB


def read_file_chunks(filename, chunk_size):
    with open(filename, 'rb') as f:
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            yield data


def upload(filename):
    upload_response = requests.post(
        UPLOAD_ENDPOINT,
        headers=HEADERS_AUTH_ONLY,
        data=read_file_chunks(filename, CHUNK_SIZE)
    )
    return upload_response.json()['upload_url']


def transcribe(audio_url):
    transcript_request = {'audio_url': audio_url}
    transcript_response = requests.post(
        TRANSCRIPT_ENDPOINT,
        json=transcript_request,
        headers=HEADERS
    )
    return transcript_response.json()['id']


def poll_transcription_status(transcript_id):
    polling_endpoint = f'{TRANSCRIPT_ENDPOINT}/{transcript_id}'
    polling_response = requests.get(polling_endpoint, headers=HEADERS)
    return polling_response.json()


def get_transcription_result_url(url):
    transcript_id = transcribe(url)
    
    while True:
        data = poll_transcription_status(transcript_id)
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data['error']
        
        print("Waiting for 30 seconds")
        time.sleep(30)


def save_transcript(url, title):
    data, error = get_transcription_result_url(url)
    
    if data:
        filename = f'{title}.txt'
        with open(filename, 'w') as f:
            f.write(data['text'])
        print('Transcript saved')
    elif error:
        print("Error!!!", error)
