from google.cloud import speech
from google.cloud import speech
import io
import os

# Set up Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "your-key-file.json"

def transcribe_audio(audio_file_path):
    """
    Transcribes an audio file using Google Cloud Speech-to-Text API.

    Args:
        audio_file_path (str): Path to the audio file to transcribe.

    Returns:
        str: The transcribed text from the audio file.
    """
import io
import os

# Set the Google Cloud key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "your-key-file.json"

def transcribe_audio(audio_file):
    client = speech.SpeechClient()

    with io.open(audio_file, "rb") as audio:
        content = audio.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)
    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript

    return transcript