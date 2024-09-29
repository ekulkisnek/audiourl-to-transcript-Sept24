import ffmpeg
import requests
import io
import logging
from pydub import AudioSegment

class AudioProcessor:
    def __init__(self, url):
        self.url = url
        self.logger = logging.getLogger(__name__)

    def stream_audio(self):
        print("Starting audio streaming...")
        try:
            # Start a streaming request
            response = requests.get(self.url, stream=True)
            response.raise_for_status()

            # Set up ffmpeg command
            process = (
                ffmpeg
                .input('pipe:0')
                .output('pipe:1', format='wav', acodec='pcm_s16le', ac=1, ar='16k')
                .overwrite_output()
                .run_async(pipe_stdin=True, pipe_stdout=True, pipe_stderr=True)
            )

            print("Received response from URL, starting to process chunks...")
            buffer = io.BytesIO()
            for chunk in response.iter_content(chunk_size=4096):
                if chunk:
                    process.stdin.write(chunk)
                    buffer.write(process.stdout.read(4096))
                    print("Processed a chunk of audio data...")

                    if buffer.tell() > 32000:  # Process in ~2 second chunks
                        buffer.seek(0)
                        audio = AudioSegment.from_wav(buffer)
                        print("Yielding processed audio chunk...")
                        yield audio.raw_data
                        buffer.seek(0)
                        buffer.truncate()

            # Process any remaining audio
            if buffer.tell() > 0:
                buffer.seek(0)
                audio = AudioSegment.from_wav(buffer)
                print("Yielding processed audio chunk...")
                yield audio.raw_data

            print("Finished streaming and processing audio.")

        except requests.RequestException as e:
            self.logger.error(f"Error fetching content: {str(e)}")
            raise
        except ffmpeg.Error as e:
            self.logger.error(f"FFmpeg error: {str(e)}")
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error in audio processing: {str(e)}")
            raise
        finally:
            if 'process' in locals():
                process.stdin.close()
                process.wait()
