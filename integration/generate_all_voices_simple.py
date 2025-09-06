#!/usr/bin/env python3
"""
Generate all character voices using Windows TTS (Windows compatible)
"""

import pyttsx3
import os
from pathlib import Path

# Character texts and voice settings
CHARACTERS = {
    "brennis": {
        "text": "The law is clear. The fine is five silver. Order must be maintained at all costs.",
        "voice_idx": 1,  # Microsoft David (male)
        "rate": 180,
        "volume": 0.9
    },
    "elara": {
        "text": "True justice is achieved through order and virtue. We must be the exemplars of the law we wish to see.",
        "voice_idx": 2,  # Microsoft Zira (female)
        "rate": 170,
        "volume": 0.9
    },
    "kael": {
        "text": "Their laws weren't written to protect us. The only justice we get is the justice we take.",
        "voice_idx": 2,  # Microsoft Zira (female) - we'll speed it up for street-smart feel
        "rate": 200,
        "volume": 0.95
    },
    "gorok": {
        "text": "I make no pretty speeches about justice. I take what I want from those too weak to stop me.",
        "voice_idx": 1,  # Microsoft David (male) - we'll slow it down for menacing feel
        "rate": 150,
        "volume": 1.0
    },
    "pellor": {
        "text": "I am merely a humble servant of the realm, Your Grace. Let me handle these tedious details.",
        "voice_idx": 1,  # Microsoft David (male) - normal rate for bureaucratic feel
        "rate": 175,
        "volume": 0.8
    },
    "valerius": {
        "text": "I never asked for this crown. Perhaps someone else would wear it better than I.",
        "voice_idx": 1,  # Microsoft David (male) - slower and quieter for hesitant feel
        "rate": 160,
        "volume": 0.7
    }
}

def generate_character_voice(character, data):
    """Generate voice for a single character"""
    try:
        engine = pyttsx3.init()
        
        # Get available voices
        voices = engine.getProperty('voices')
        
        if len(voices) > data['voice_idx']:
            engine.setProperty('voice', voices[data['voice_idx']].id)
        
        # Set properties
        engine.setProperty('rate', data['rate'])
        engine.setProperty('volume', data['volume'])
        
        # Generate audio file
        output_file = f"../audio/characters/{character}-sample.wav"
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Generate
        engine.save_to_file(data['text'], output_file)
        engine.runAndWait()
        
        if Path(output_file).exists():
            file_size = Path(output_file).stat().st_size
            print(f"SUCCESS {character.title()}: Generated {output_file} ({file_size} bytes)")
            return True
        else:
            print(f"FAILED {character.title()}: No audio file created")
            return False
            
    except Exception as e:
        print(f"ERROR {character.title()}: {e}")
        return False

def main():
    """Generate all character voices"""
    print("Generating All Character Voices")
    print("=" * 50)
    
    success_count = 0
    
    for character, data in CHARACTERS.items():
        if generate_character_voice(character, data):
            success_count += 1
    
    print(f"\nGenerated {success_count}/{len(CHARACTERS)} character voices!")
    
    if success_count > 0:
        print("\nNext steps:")
        print("1. Audio files are in /audio/characters/")
        print("2. Open any character profile markdown file")
        print("3. The HTML audio players should work with these files")
        print("4. Test by opening markdown files in a browser")
        
        print("\nNote: Files are in WAV format. For better web compatibility,")
        print("you may want to convert to MP3 using online converters or ffmpeg.")

if __name__ == "__main__":
    main()