import whisper
import numpy as np
import logging

class Transcriber:
    def __init__(self, model_name="base"):
        self.model = whisper.load_model(model_name, device="cpu", download_root=None, weights_only=True)
        self.logger = logging.getLogger(__name__)

    def transcribe(self, audio_chunk):
        try:
            # Convert raw audio data to numpy array
            audio_array = np.frombuffer(audio_chunk, dtype=np.int16).astype(np.float32) / 32768.0

            # Transcribe the audio chunk
            result = self.model.transcribe(audio_array)
            
            return result["text"]
        except Exception as e:
            self.logger.error(f"Error during transcription: {str(e)}")
            return ""
