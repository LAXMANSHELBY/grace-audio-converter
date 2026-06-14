from pydub import AudioSegment
import numpy as np

def create_8d_audio(input_file, output_file, chunk_duration_ms=100, pan_frequency=0.5):
    """
    Create 8D audio effect by applying a sinusoidal panning effect over chunks of the audio.
    
    Parameters:
    - input_file: path to input audio file
    - output_file: path to save processed audio
    - chunk_duration_ms: duration of each chunk in milliseconds
    - pan_frequency: frequency of panning oscillation in Hz
    """
    try:
        audio = AudioSegment.from_file(input_file)
    except Exception as e:
        print(f"Error loading audio file: {e}")
        return
    
    output_audio = AudioSegment.empty()
    total_chunks = len(audio) // chunk_duration_ms + 1
    
    for i in range(total_chunks):
        start_ms = i * chunk_duration_ms
        end_ms = min((i + 1) * chunk_duration_ms, len(audio))
        chunk = audio[start_ms:end_ms]
        
        # Calculate pan value between -1 (left) and 1 (right)
        pan = np.sin(2 * np.pi * pan_frequency * (start_ms / 1000.0))
        
        # Apply panning to chunk
        chunk = chunk.pan(pan)
        
        output_audio += chunk
    
    output_audio.export(output_file, format="mp3")
    print(f"8D audio created and saved to {output_file}")

if __name__ == "__main__":
    create_8d_audio(r"C:\song proj\Fear.mp3", "output_8d.mp3")
