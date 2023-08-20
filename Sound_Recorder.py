# CIPHER BYTE TECHNOLOGY
# INTERNSHIP
# PYTHON
'''RECORD YOUR VOICE
Python can be used to perform a variety of tasks. 
One of them is creating a voice recorder. We can use python’s sounddevice module to record and play audio.
 This module along with the wavio or the scipy module provides a way to save recorded audio.'''
#Source code

import sounddevice as sd
import wavio

def record_audio(filename, duration, sample_rate):
    print("Recording...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2)
    sd.wait()  # Wait until recording is finished
    wavio.write(filename, audio_data, sample_rate, sampwidth=2)  # Save recorded audio as WAV file
    print(f"Audio saved as '{filename}'")

def main():
    filename = input("Enter the name of the audio file to save (e.g., recording.wav): ")
    duration = float(input("Enter the duration of the recording (in seconds): "))
    sample_rate = 44100  # You can adjust the sample rate as needed
    
    record_audio(filename, duration, sample_rate)

if __name__ == "__main__":
    main()

#output format
'''Enter the name of the audio file to save(e.g., recording.wav): recording3.wav
Enter the duration of the recording ( in seconds): 2
Recording...
Audio saved as 'recording3.wav' '''
