import argparse
import logging
from audio_processor import AudioProcessor
from transcriber import Transcriber
from utils import setup_logging

def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description="Real-time transcription of streaming video/audio content.")
    parser.add_argument("url", help="URL of the video/audio stream")
    args = parser.parse_args()

    try:
        audio_processor = AudioProcessor(args.url)
        transcriber = Transcriber()

        for audio_chunk in audio_processor.stream_audio():
            transcription = transcriber.transcribe(audio_chunk)
            if transcription:
                print(transcription, end='', flush=True)

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
