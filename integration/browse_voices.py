#!/usr/bin/env python3
"""
Browse ElevenLabs voices (Windows-compatible)
"""

import os
import requests
from pathlib import Path

def load_env_file():
    """Load .env file manually"""
    env_path = Path('.env')
    if env_path.exists():
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key] = value

def browse_voices():
    """Browse available ElevenLabs voices"""
    load_env_file()
    api_key = os.getenv('ELEVENLABS_API_KEY')
    
    if not api_key:
        print("No API key found!")
        return
    
    print("Available ElevenLabs Voices")
    print("=" * 50)
    
    try:
        headers = {
            "Accept": "application/json",
            "xi-api-key": api_key
        }
        response = requests.get("https://api.elevenlabs.io/v1/voices", headers=headers)
        
        if response.status_code == 200:
            voices = response.json()["voices"]
            
            for i, voice in enumerate(voices, 1):
                name = voice["name"]
                voice_id = voice["voice_id"]
                category = voice.get("category", "Unknown")
                
                print(f"{i:2d}. {name:<20} ({category})")
                print(f"    ID: {voice_id}")
                print()
            
            print(f"Total voices available: {len(voices)}")
            print("\nRecommended character mappings:")
            print("-" * 40)
            print("Brennis (Deep Military):    Look for deep, authoritative male voices")
            print("Elara (Refined Female):     Look for elegant, noble female voices") 
            print("Kael (Street Smart):        Look for young, energetic female voices")
            print("Gorok (Barbarian):          Look for very deep, gruff male voices")
            print("Pellor (Bureaucrat):        Look for smooth, professional male voices")
            print("Valerius (Weak Ruler):      Look for hesitant, nervous male voices")
            
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    browse_voices()