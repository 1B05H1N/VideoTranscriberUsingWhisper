# VideoTranscriberUsingWhisper

This script allows you to transcribe audio from either a YouTube video link or a local audio file using the `openai-whisper` library installed via Homebrew.

## Requirements

- Python 3.6+
- `pytube` library for downloading YouTube videos
- `openai-whisper` installed via Homebrew

## Installation

### 1. Install the required Python packages

```sh
pip install -r requirements.txt
```

### 2. Install the `openai-whisper` library via Homebrew

```sh
brew install openai-whisper
```

## Usage

Run the script and follow the prompts to either provide a YouTube video link or a local audio file path.

```sh
python VideoTranscriberUsingWhisper.py
```

### Example

1. When prompted, enter `yt` to provide a YouTube video link or `file` to provide a local file path.
2. If you selected `yt`, enter the YouTube video link.
3. If you selected `file`, enter the path to your local audio file.
4. The script will download (if necessary) and transcribe the audio, then print the transcription.

### Additional Notes

- Make sure the `whisper` command-line tool is available in your PATH after installing via Homebrew.
- This script relies on the `openai-whisper` library for transcription, which needs to be installed separately using Homebrew as shown above.
