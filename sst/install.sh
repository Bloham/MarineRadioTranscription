#!/bin/bash

# Update and install system dependencies
sudo apt-get update
sudo apt-get install -y ffmpeg

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Download Whisper model
# Instead of running a command that expects an audio argument, we download the model using the correct method
python -c "import whisper; whisper.load_model('tiny')"

echo "Installation complete."
