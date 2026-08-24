import numpy as np
import wave
import struct

def synthesize_wav(engine, output_filepath, duration=2.0, sample_rate=44100, base_freq=220.0):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    
    # Scale x to match frequency: x = t * (2*L) * base_freq
    # So that fundamental frequency (n=1) corresponds to base_freq
    x = t * (2 * engine.L * base_freq)
    x = np.mod(x + engine.L, 2 * engine.L) - engine.L  # wrap into [-L, L]
    
    audio_signal = engine.evaluate(x)
    
    # Normalize to 16-bit range
    max_amp = np.max(np.abs(audio_signal))
    if max_amp > 0:
        audio_signal = audio_signal / max_amp
    
    audio_signal = np.int16(audio_signal * 32767)
    
    with wave.open(output_filepath, 'w') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        for s in audio_signal:
            wav_file.writeframesraw(struct.pack('<h', s))
