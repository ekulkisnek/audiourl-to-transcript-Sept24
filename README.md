
# Real-Time Audio Transcriber

A Python-based application that performs real-time transcription of streaming audio content using OpenAI's Whisper model.

## Features

- Real-time audio streaming from URLs
- Audio processing with ffmpeg
- Transcription using Whisper model
- Support for various audio formats
- Chunk-based processing for efficient memory usage

## Requirements

The project requires the following Python packages:
- openai-whisper
- pydub
- ffmpeg-python
- requests
- numpy

All dependencies are automatically managed through the Poetry package manager.

## Usage

Run the transcriber with a URL to an audio stream:

```bash
python main.py "YOUR_AUDIO_URL"
```

Example:
```bash
python main.py "https://samplelib.com/lib/preview/mp3/sample-3s.mp3"
```

## Project Structure

- `main.py` - Entry point of the application
- `audio_processor.py` - Handles audio streaming and processing
- `transcriber.py` - Manages the Whisper model and transcription
- `utils.py` - Contains utility functions like logging setup

## How It Works

1. The application takes an audio URL as input
2. Audio is streamed in chunks to minimize memory usage
3. Each chunk is processed using ffmpeg to ensure correct format
4. The Whisper model transcribes the processed audio
5. Transcription results are printed in real-time

## Error Handling

The application includes comprehensive error handling for:
- Network connection issues
- Audio processing errors
- Transcription failures
- Invalid URLs

## Logging

Detailed logging is implemented throughout the application, with logs showing:
- Audio processing status
- Transcription progress
- Error messages and exceptions

## Sample Test URL

You can test the application using this sample audio:
```
https://samplelib.com/lib/preview/mp3/sample-3s.mp3
```

## License

This project is open-source and available for use under standard open-source terms.
