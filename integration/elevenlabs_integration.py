#!/usr/bin/env python3
"""
ElevenLabs Integration for The Weight of the Crown Campaign
Automatically generates character voices using ElevenLabs API
"""

import os
import requests
import json
from pathlib import Path
from audio_manager import AudioManager

class ElevenLabsGenerator:
    """Generate audio using ElevenLabs API"""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('ELEVENLABS_API_KEY')
        self.base_url = "https://api.elevenlabs.io/v1"
        self.headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": self.api_key
        }
        
        if not self.api_key:
            print("⚠️  Warning: No API key found. Set ELEVENLABS_API_KEY environment variable or pass api_key parameter.")
    
    def get_available_voices(self):
        """Get list of available voices from ElevenLabs"""
        try:
            response = requests.get(f"{self.base_url}/voices", headers=self.headers)
            if response.status_code == 200:
                voices = response.json()["voices"]
                return [(voice["voice_id"], voice["name"]) for voice in voices]
            else:
                print(f"Error getting voices: {response.status_code}")
                return []
        except Exception as e:
            print(f"Error connecting to ElevenLabs: {e}")
            return []
    
    def generate_speech(self, text: str, voice_id: str, output_file: str, 
                       stability: float = 0.75, similarity_boost: float = 0.75):
        """Generate speech using ElevenLabs API"""
        
        if not self.api_key:
            print("❌ No API key configured. Cannot generate audio.")
            return False
        
        url = f"{self.base_url}/text-to-speech/{voice_id}"
        
        data = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": stability,
                "similarity_boost": similarity_boost
            }
        }
        
        try:
            response = requests.post(url, json=data, headers=self.headers)
            
            if response.status_code == 200:
                # Ensure output directory exists
                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                
                # Save audio file
                with open(output_file, 'wb') as f:
                    f.write(response.content)
                
                print(f"✅ Generated: {output_file}")
                return True
            else:
                print(f"❌ Error generating audio: {response.status_code}")
                print(response.text)
                return False
                
        except Exception as e:
            print(f"❌ Error: {e}")
            return False

# Recommended voice mappings for characters
VOICE_RECOMMENDATIONS = {
    "brennis": {
        "description": "Deep, authoritative military voice",
        "text": "The law is clear. The fine is five silver. My duty is to the office, not the man.",
        "settings": {"stability": 0.8, "similarity_boost": 0.7},
        "voice_suggestions": ["Deep male", "Authoritative", "Military", "Stern"]
    },
    "elara": {
        "description": "Refined female voice with musical accent",
        "text": "True justice is achieved through order and virtue. We must be the exemplars of the law we wish to see.",
        "settings": {"stability": 0.7, "similarity_boost": 0.8},
        "voice_suggestions": ["Elegant female", "Refined", "Musical", "Noble"]
    },
    "kael": {
        "description": "Street-smart female voice, slightly raspy",
        "text": "Their laws weren't written to protect us. The only justice we get is the justice we take.",
        "settings": {"stability": 0.6, "similarity_boost": 0.7},
        "voice_suggestions": ["Young female", "Energetic", "Street-smart", "Rebellious"]
    },
    "gorok": {
        "description": "Deep rumbling voice with rural accent",
        "text": "I make no pretty speeches about justice. I take what I want from those too weak to stop me.",
        "settings": {"stability": 0.8, "similarity_boost": 0.6},
        "voice_suggestions": ["Very deep male", "Gruff", "Rural", "Threatening"]
    },
    "pellor": {
        "description": "Smooth, deceptively pleasant bureaucratic voice",
        "text": "I am merely a humble servant of the realm, Your Grace. Let me handle these tedious details.",
        "settings": {"stability": 0.75, "similarity_boost": 0.8},
        "voice_suggestions": ["Professional male", "Smooth", "Pleasant", "Bureaucratic"]
    },
    "valerius": {
        "description": "Hesitant, weak voice seeking approval",
        "text": "I never asked for this crown. Perhaps someone else would wear it better than I.",
        "settings": {"stability": 0.6, "similarity_boost": 0.7},
        "voice_suggestions": ["Nervous male", "Hesitant", "Weak", "Uncertain"]
    }
}

def setup_api_key():
    """Interactive setup for ElevenLabs API key"""
    print("🔑 ElevenLabs API Key Setup")
    print("=" * 40)
    print("1. Go to https://elevenlabs.io/")
    print("2. Sign in to your account")
    print("3. Go to Profile → API Key")
    print("4. Copy your API key")
    print()
    
    api_key = input("Enter your ElevenLabs API key: ").strip()
    
    if api_key:
        # Save to environment variable for this session
        os.environ['ELEVENLABS_API_KEY'] = api_key
        
        # Create .env file for persistence
        env_content = f"# ElevenLabs API Configuration\nELEVENLABS_API_KEY={api_key}\n"
        
        with open('.env', 'w') as f:
            f.write(env_content)
        
        print("✅ API key configured!")
        print("💾 Saved to .env file for future use")
        
        # Add .env to .gitignore if it exists
        gitignore_path = Path('.gitignore')
        if gitignore_path.exists():
            with open(gitignore_path, 'r') as f:
                content = f.read()
            if '.env' not in content:
                with open(gitignore_path, 'a') as f:
                    f.write('\n# Environment variables\n.env\n')
                print("🔒 Added .env to .gitignore for security")
        
        return api_key
    else:
        print("❌ No API key provided")
        return None

def browse_voices():
    """Interactive voice browser"""
    generator = ElevenLabsGenerator()
    
    if not generator.api_key:
        print("❌ No API key configured. Run setup_api_key() first.")
        return
    
    print("🎵 Available ElevenLabs Voices")
    print("=" * 50)
    
    voices = generator.get_available_voices()
    
    if not voices:
        print("❌ Could not retrieve voices. Check your API key and connection.")
        return
    
    for i, (voice_id, name) in enumerate(voices, 1):
        print(f"{i:2d}. {name} ({voice_id})")
    
    print("\n💡 Recommended voice types for characters:")
    for char, data in VOICE_RECOMMENDATIONS.items():
        print(f"• {char.title()}: {', '.join(data['voice_suggestions'])}")
    
    return voices

def generate_character_voices(voice_mapping: dict = None):
    """Generate all character voice samples"""
    generator = ElevenLabsGenerator()
    
    if not generator.api_key:
        print("❌ No API key configured. Run setup_api_key() first.")
        return
    
    if not voice_mapping:
        print("❌ No voice mapping provided. Use browse_voices() to see available voices.")
        return
    
    print("🎬 Generating Character Voice Samples")
    print("=" * 50)
    
    audio_manager = AudioManager()
    
    for character, voice_id in voice_mapping.items():
        if character not in VOICE_RECOMMENDATIONS:
            print(f"⚠️  Unknown character: {character}")
            continue
        
        char_data = VOICE_RECOMMENDATIONS[character]
        output_file = f"../audio/characters/{character}-sample.mp3"
        
        print(f"🎙️  Generating {character.title()}...")
        
        success = generator.generate_speech(
            text=char_data["text"],
            voice_id=voice_id,
            output_file=output_file,
            **char_data["settings"]
        )
        
        if success:
            # Update audio manager
            audio_manager.add_character_audio(
                character=character,
                audio_file=f"{character}-sample.mp3",
                quote=char_data["text"].split('.')[0] + '.',
                description=char_data["description"]
            )

def generate_scene_narrations(narrator_voice_id: str):
    """Generate scene narration audio"""
    generator = ElevenLabsGenerator()
    
    if not generator.api_key:
        print("❌ No API key configured.")
        return
    
    scenes = {
        "prologue-opening": "In the morning light of Estellon, three philosophies will collide, and the players will witness the spark that ignites a revolution.",
        "act1-riot": "As the sun sets, tensions rise. The festive mood of the morning has curdled into something darker.",
        "epilogue-council": "The factions gather in the great hall. The old regime has ended. The PCs must decide the city's future."
    }
    
    print("🎬 Generating Scene Narrations")
    print("=" * 40)
    
    for scene, text in scenes.items():
        output_file = f"audio/scenes/{scene}.mp3"
        print(f"🎙️  Generating {scene}...")
        
        generator.generate_speech(
            text=text,
            voice_id=narrator_voice_id,
            output_file=output_file,
            stability=0.8,
            similarity_boost=0.7
        )

def main():
    """Main setup workflow"""
    print("🎵 ElevenLabs Integration Setup")
    print("=" * 40)
    print()
    
    # Check if API key exists
    if not os.getenv('ELEVENLABS_API_KEY'):
        print("🔑 No API key found. Let's set one up...")
        api_key = setup_api_key()
        if not api_key:
            return
    else:
        print("✅ API key found!")
    
    print("\n📋 Next steps:")
    print("1. Run browse_voices() to see available voices")
    print("2. Create a voice mapping dict like:")
    print("   voice_map = {")
    print("       'brennis': 'voice_id_here',")
    print("       'elara': 'voice_id_here',")
    print("       # ... etc")
    print("   }")
    print("3. Run generate_character_voices(voice_map)")
    print("4. Run generate_scene_narrations(narrator_voice_id)")
    
    print("\n💡 Example workflow:")
    print("   voices = browse_voices()")
    print("   # Pick voices and create mapping")
    print("   generate_character_voices(voice_mapping)")

if __name__ == "__main__":
    main()