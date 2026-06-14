from pydub import AudioSegment
import numpy as np
import pyaudio

# Load the audio file
audio = AudioSegment.from_mp3("C:\song proj")

# Function to create 8D audio effectfrom pydub import AudioSegment
import numpy as np
import pyaudio

# Load the audio file
audio = AudioSegment.from_mp3("C:\song proj")

# Function to create 8D audio effect
def create_8d_audio(audio_segment, pan_frequency=2):
    # Convert audio to numpy array
    samples = np.array(audio_segment.get_array_of_samples())
    
    # Create a stereo effect by panning
    left_channel = samples.copy()
    right_channel = samples.copy()
    
    # Apply panning effect
    for i in range(len(samples)):
        pan = np.sin(2 * np.pi * pan_frequency * i / (len(samples) / 2))  # Create a sine wave for panning
        left_channel[i] = samples[i] * (1 - pan)  # Left channel
        right_channel[i] = samples[i] * (1 + pan)  # Right channel
    
    # Combine channels
    combined = np.column_stack((left_channel, right_channel)).flatten()
    
    # Create a new AudioSegment from the combined array
    output_audio = AudioSegment(
        combined.tobytes(),
        frame_rate=audio_segment.frame_rate,
        sample_width=audio_segment.sample_width,
        channels=2
    )
    
    return output_audio

# Create 8D audio
audio_8d = create_8d_audio(audio, pan_frequency=4)

# Save the 8D audio to a file
audio_8d.export("output_8d.mp3", format="mp3")

# Play the 8D audio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=2, rate=audio_8d.frame_rate, output=True)
stream.write(audio_8d.raw_data)
stream.stop_stream()
stream.close()
p.terminate()
def create_8d_audio(audio_segment, pan_frequency=2):
    """
    Creates an 8D audio effect by panning the audio signal.

    Args:
        audio_segment (AudioSegment): The input audio segment.
        pan_frequency (float, optional): The frequency of the panning effect. Defaults to 2.

    Returns:
        AudioSegment: The output audio segment with the 8D effect.
    """
    # Convert audio to numpy array
    samples = np.array(audio_segment.get_array_of_samples())
    
    # Create a stereo effect by panning
    left_channel = samples.copy()
    right_channel = samples.copy()
    
    # Apply panning effect
    for i in range(len(samples)):
        pan = np.sin(2 * np.pi * pan_frequency * i / (len(samples) / audio_segment.frame_rate))  # Create a sine wave for panning
        left_channel[i] = samples[i] * (1 - pan)  # Left channel
        right_channel[i] = samples[i] * (1 + pan)  # Right channel
    
    # Combine channels
    combined = np.column_stack((left_channel, right_channel)).flatten()
    
    # Create a new AudioSegment from the combined array
    output_audio = AudioSegment(
        combined.tobytes(),
        frame_rate=audio_segment.frame_rate,
        sample_width=audio_segment.sample_width,
        channels=2
    )
    
    return output_audio

def play_audio(audio_segment):
    """
    Plays the given audio segment.

    Args:
        audio_segment (AudioSegment): The audio segment to play.
    """
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=audio_segment.channels, rate=audio_segment.frame_rate, output=True)
    stream.write(audio_segment.raw_data)
    stream.stop_stream()
    stream.close()
    p.terminate()

# Load the audio file
audio = AudioSegment.from_mp3("C:\\song proj")

# Create 8D audio
audio_8d = create_8d_audio(audio, pan_frequency=4)

# Save the 8D audio to a file
audio_8d.export("output_8d.mp3", format="mp3")

# Play the 8D audio
play_audio(audio_8d)
from pydub import AudioSegment
import numpy as np
import pyaudio

# Load the audio file
audio = AudioSegment.from_mp3("C:\song proj")

# Function to create 8D audio effect
def create_8d_audio(audio_segment, pan_frequency=2):
    """
    Creates an 8D audio effect by panning the audio signal.

    Args:
        audio_segment (AudioSegment): The input audio segment.
        pan_frequency (float, optional): The frequency of the panning effect. Defaults to 2.

    Returns:
        AudioSegment: The output audio segment with the 8D effect.
    """
    # Convert audio to numpy array
    samples = np.array(audio_segment.get_array_of_samples())
    
    # Create a stereo effect by panning
    left_channel = samples.copy()
    right_channel = samples.copy()
    
    # Apply panning effect
    for i in range(len(samples)):
        pan = np.sin(2 * np.pi * pan_frequency * i / (len(samples) / 2))  # Create a sine wave for panning
        left_channel[i] = samples[i] * (1 - pan)  # Left channel
        right_channel[i] = samples[i] * (1 + pan)  # Right channel
    
    # Combine channels
    combined = np.column_stack((left_channel, right_channel)).flatten()
    
    # Create a new AudioSegment from the combined array
    output_audio = AudioSegment(
        combined.tobytes(),
        frame_rate=audio_segment.frame_rate,
        sample_width=audio_segment.sample_width,
        channels=2
    )
    
    return output_audio

# Create 8D audio
audio_8d = create_8d_audio(audio)

# Save the 8D audio to a file
audio_8d.export("output_8d.mp3", format="mp3")

# Play the 8D audio
def play_audio(audio_segment):
    """
    Plays the given audio segment.

    Args:
        audio_segment (AudioSegment): The audio segment to play.
    """
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=audio_segment.channels, rate=audio_segment.frame_rate, output=True)
    stream.write(audio_segment.raw_data)
    stream.stop_stream()
    stream.close()
    p.terminate()

play_audio(audio_8d)
def create_8d_audio(audio_segment):
    # Convert audio to numpy array
    samples = np.array(audio_segment.get_array_of_samples())
    
    # Create a stereo effect by panning
    left_channel = samples.copy()
    right_channel = samples.copy()
    
    # Apply panning effect
    for i in range(len(samples)):
        pan = np.sin(2 * np.pi * i / (len(samples) / 2))  # Create a sine wave for panning
        left_channel[i] = samples[i] * (1 - pan)  # Left channel
        right_channel[i] = samples[i] * (1 + pan)  # Right channel
    
    # Combine channels
    combined = np.column_stack((left_channel, right_channel)).flatten()
    
    # Create a new AudioSegment from the combined array
    output_audio = AudioSegment(
        combined.tobytes(),
        frame_rate=audio.frame_rate,
        sample_width=audio.sample_width,
        channels=2
    )
    
    return output_audio

# Create 8D audio
audio_8d = create_8d_audio(audio)

# Save the 8D audio to a file
audio_8d.export("output_8d.mp3", format="mp3")

# Play the 8D audio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=2, rate=audio_8d.frame_rate, output=True)
stream.write(audio_8d.raw_data)
stream.stop_stream()
stream.close()
p.terminate()