# This script was written by Ibrahim Al-Shinnawi, shinnawi.com, on 2024-06-17. It is licensed under the MIT License, use at your own risk -- no warranties provided whatsoever.

import os
from pytube import YouTube
import subprocess
import sys

def download_audio_from_youtube(youtube_url, output_path="audio.mp3"):
    try:
        yt = YouTube(youtube_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(filename=output_path)
        return output_path
    except Exception as e:
        print(f"Failed to download audio from YouTube: {e}")
        sys.exit(1)

def transcribe_audio_with_whisper(audio_file_path):
    try:
        result = subprocess.run(['whisper', audio_file_path, '--model', 'base'], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Whisper transcription failed: {result.stderr}")
            sys.exit(1)
        return result.stdout
    except Exception as e:
        print(f"Failed to transcribe audio with Whisper: {e}")
        sys.exit(1)

def main():
    input_type = input("Do you want to provide a YouTube video link or a local file? (Enter 'yt' for YouTube, 'file' for local file): ").strip().lower()

    if input_type == 'yt':
        input_path_or_url = input("Enter the YouTube video link: ").strip()
        audio_file_path = download_audio_from_youtube(input_path_or_url)
    elif input_type == 'file':
        input_path_or_url = input("Enter the local audio file path: ").strip()
        audio_file_path = input_path_or_url
    else:
        print("Invalid input. Please enter 'yt' for YouTube or 'file' for local file.")
        return

    # Transcribe the audio using Whisper
    transcription = transcribe_audio_with_whisper(audio_file_path)

    # Print the transcription
    print("Transcription:\n", transcription)

    # Remove the downloaded audio file if it was downloaded
    if input_type == 'yt':
        os.remove(audio_file_path)

if __name__ == "__main__":
    main()
