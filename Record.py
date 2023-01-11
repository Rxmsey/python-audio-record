import os
import pyaudio
import wave

# Obtain the directory of the current Python file
dirname = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dirname, 'recorded.wav')

# Define the recording parameters
CHUNK = 1024  # number of samples per frame
FORMAT = pyaudio.paInt16  # audio format (16-bit signed integer)
CHANNELS = 2  # number of channels
RATE = 44100  # samples per second
RECORD_SECONDS = 5  # duration of the recording

# Create a PyAudio object
p = pyaudio.PyAudio()

# Open a stream to record audio
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Start recording
print("Recording...")
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

# Stop recording
stream.stop_stream()
stream.close()
p.terminate()

# Save the recorded audio to a file
wf = wave.open(filename, "wb")
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b"".join(frames))
wf.close()
print(f"Recording Done! the file is saved at {filename}")
