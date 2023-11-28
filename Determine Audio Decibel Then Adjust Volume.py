from pydub import AudioSegment
import tkinter as tk
from tkinter import filedialog
import tempfile
import os

def check_and_adjust_audio_volume(audio_file_path, low_threshold=-30, high_threshold=-20):
    # Load the audio file
    audio = AudioSegment.from_file(audio_file_path)

    # Calculate the volume (dBFS)
    volume = audio.dBFS

    if volume < low_threshold:
        # Increase volume for low volume audio
        audio += abs(low_threshold - -10)
        result = "Low volume (adjusted)"
    elif volume > high_threshold:
        # Decrease volume for high volume audio
        audio -= abs(volume - -40)
        result = "High volume (adjusted)"
    else:
        result = "Normal volume"

    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Export the adjusted audio to a temporary file
    adjusted_audio_file_path = os.path.join(temp_dir, "adjusted_audio.wav")
    audio.export(adjusted_audio_file_path, format="wav")

    return result, adjusted_audio_file_path

def play_audio(audio_file_path):
    os.system(f'start {audio_file_path}')

def select_audio_file():
    root = tk.Tk()
    root.withdraw()
    audio_file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3 *.wav *.flac *.ogg")])
    return audio_file_path

def main():
    audio_file_path = select_audio_file()

    if audio_file_path:
        result, adjusted_audio_file_path = check_and_adjust_audio_volume(audio_file_path)
        print(f"The audio has {result}.")
        play_audio(adjusted_audio_file_path)
    else:
        print("No audio file selected.")

if __name__ == "__main__":
    main()
