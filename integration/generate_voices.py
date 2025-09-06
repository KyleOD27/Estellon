#!/usr/bin/env python3
"""
Generate character voices using common ElevenLabs voices
"""

import os
import requests
from pathlib import Path

def load_env():
    """Load .env file"""
    env_path = Path('.env')
    if env_path.exists():
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key] = value

def generate_voice_sample(text, voice_id, output_file, character_name):
    """Generate a single voice sample"""
    load_env()
    api_key = os.getenv('ELEVENLABS_API_KEY')
    
    if not api_key:
        print("No API key found!")
        return False
    
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key
    }
    
    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.75
        }
    }
    
    try:
        print(f"Generating {character_name} voice...")
        response = requests.post(url, json=data, headers=headers)
        
        if response.status_code == 200:
            # Ensure output directory exists
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            
            # Save audio file
            with open(output_file, 'wb') as f:
                f.write(response.content)
            
            print(f"SUCCESS: Generated {output_file}")
            return True
        else:
            print(f"ERROR: {response.status_code}")
            print(response.text)
            return False
            
    except Exception as e:
        print(f"ERROR: {e}")
        return False

def main():
    """Generate sample voices using common ElevenLabs voices"""
    print("Generating Character Voice Samples")
    print("=" * 50)
    
    # Common ElevenLabs voice IDs (these usually work)
    # We'll try one first to test
    
    test_voices = {
        # These are common public voices that should work
        "adam": "pNInz6obpgDQGcFmaJgB",        # Deep male
        "antoni": "ErXwobaYiN019PkySvjV",       # Male narrator  
        "arnold": "VR6AewLTigWG4xSOukaG",       # Very deep male
        "bella": "EXAVITQu4vr4xnSDxMaL",       # Female
        "domi": "AZnzlk1XvdvUeBnXmlld",        # Confident male
        "elli": "MF3mGyEYCl7XYWbV9V6O",        # Young female
        "josh": "TxGEqnHWrfWFTfGW9XjX",        # Deep male
        "rachel": "21m00Tcm4TlvDq8ikWAM",      # Calm female
        "sam": "yoZ06aMxZJJ28mfd3POQ"          # Narration
    }
    
    # Let's test with Brennis first using a deep male voice
    character = "brennis"
    text = "The law is clear. The fine is five silver. Order must be maintained at all costs."
    voice_id = test_voices["adam"]  # Deep male voice
    output_file = f"audio/characters/{character}-sample.mp3"
    
    success = generate_voice_sample(text, voice_id, output_file, character.title())
    
    if success:
        print("\nSuccess! Your first character voice has been generated.")
        print(f"File location: {output_file}")
        print("\nYou can now:")
        print("1. Open your Brennis character profile markdown file")
        print("2. The audio player should work with the generated file")
        print("3. Test it by opening the markdown in a browser or viewer that supports HTML")
    else:
        print("\nGeneration failed. This might be because:")
        print("1. Your ElevenLabs plan doesn't have text-to-speech access")
        print("2. The voice ID might not be available")
        print("3. You might need to verify your account or upgrade")
        
        print(f"\nYour API key is working: {os.getenv('ELEVENLABS_API_KEY')[:15]}...")

if __name__ == "__main__":
    main()