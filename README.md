# MarineRadioTranscription

## Project Goal
Create a system using a Raspberry Pi 5 with an RTL-SDR to scan marine radio channels, record audio, transcribe the audio using OpenAI's Whisper model, and display the transcriptions in the cockpit of a vessel using SignalK's notification system.

## Components and Structure

### Hardware Setup:
- **Raspberry Pi 5** with 8GB RAM
- **RTL-SDR v4** for scanning marine radio channels

### Software Setup:
- **OpenPlotter OS** (based on Raspbian)
- **SignalK** for data display and notifications
- **Python environment** for running Whisper model and handling transcriptions
- **RTL-SDR tools** for scanning and recording (e.g., `rtl_fm`, `gqrx`)
- **SoX** for audio processing (if needed)

### SDR Setup and Audio Recording:
- Use `rtl_fm` or `gqrx` to continuously scan marine radio channels.
- Record audio when speech is detected.
- Store audio files on the M.2 SSD for processing.

### Speech-to-Text (STT) Processing:
- Utilize OpenAI's Whisper model for transcribing audio recordings.
- Optimize for real-time or near-real-time processing by choosing an appropriate model size (e.g., Whisper base or tiny).

### Transcription Display with SignalK:
- Integrate with SignalK to display transcriptions as notifications in the cockpit.
- Use a Python script to send transcriptions to SignalK via API calls over UDP.

### Performance Optimization:
- Use smaller Whisper models (e.g., Whisper base or tiny) to reduce computational load.
- Limit resources using CPU affinity (`taskset`), nice levels (`nice`), and cgroups.


## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Bloham/MarineRadioTranscription
   cd MarineRadioTranscription/stt

2. Run the install script to set up the environment:
   ./install.sh


### 1 Ensure the virtual environment is activated:

    ```bash
    source venv/bin/activate

### 2 Start the main script:

    ```bash
    python main.py