import os
import logging
from pydub import AudioSegment
import whisper
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from config import MODEL_NAME, AUDIO_DIR, LOG_DIR

# Setup logging
logging.basicConfig(filename=os.path.join(LOG_DIR, 'stt.log'), level=logging.INFO)

# Load Whisper model
model = whisper.load_model(MODEL_NAME)

class AudioFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        filepath = event.src_path
        try:
            logging.info(f'Processing file: {filepath}')
            audio = AudioSegment.from_file(filepath)
            result = model.transcribe(audio)
            print(f'Transcription for {filepath}: {result["text"]}')
            os.remove(filepath)  # Delete the file after processing
        except Exception as e:
            logging.error(f'Error processing file {filepath}: {e}')

def monitor_directory(directory):
    event_handler = AudioFileHandler()
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=False)
    observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    monitor_directory(AUDIO_DIR)
