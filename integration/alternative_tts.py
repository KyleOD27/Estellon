#!/usr/bin/env python3
"""
Alternative text-to-speech options for character voices
"""

import os
import subprocess
from pathlib import Path

def windows_tts_test():
    """Test Windows built-in text-to-speech"""
    print("Testing Windows Text-to-Speech")
    print("=" * 40)
    
    try:
        import pyttsx3
        
        # Initialize the engine
        engine = pyttsx3.init()
        
        # Get available voices
        voices = engine.getProperty('voices')
        print(f"Available voices: {len(voices)}")
        
        for i, voice in enumerate(voices[:5]):  # Show first 5
            print(f"{i+1}. {voice.name}")
        
        # Test generation
        text = "The law is clear. The fine is five silver."
        output_file = "../audio/characters/brennis-sample-windows.wav"
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Generate audio
        engine.save_to_file(text, output_file)
        engine.runAndWait()
        
        if Path(output_file).exists():
            print(f"SUCCESS: Generated {output_file}")
            return True
        else:
            print("FAILED: Audio file not created")
            return False
            
    except ImportError:
        print("pyttsx3 not installed. Installing...")
        try:
            subprocess.check_call(['pip', 'install', 'pyttsx3'])
            print("Installed pyttsx3. Please run this script again.")
            return False
        except:
            print("Could not install pyttsx3")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def create_manual_guide():
    """Create guide for manual audio generation"""
    guide = """
# Alternative Audio Generation Methods

Since ElevenLabs requires a paid plan, here are alternative approaches:

## Option 1: Windows Built-in TTS
- Install: `pip install pyttsx3`
- Run: `python alternative_tts.py`
- Pros: Free, works offline
- Cons: Limited voice quality

## Option 2: Online TTS Services (Free)
1. **NaturalReader** (https://www.naturalreaders.com/)
   - Upload your character scripts
   - Download as MP3
   - Good voice quality

2. **TTSMaker** (https://ttsmaker.com/)
   - Free online TTS
   - Multiple voices
   - Download as MP3

3. **Google Cloud TTS** (Free tier: 4M characters/month)
   - High quality voices
   - Requires Google account
   - API integration possible

## Option 3: Record Your Own Voices
- Use Audacity (free audio editor)
- Record each character line
- Save as MP3 in the /audio/ directories
- Most authentic but time-consuming

## Option 4: Use AI Voice Generators (Free trials)
- **Murf.ai** - Free trial available
- **Speechify** - Limited free usage
- **Azure Cognitive Services** - Free tier available

## Character Audio Scripts Already Created
Your scripts are ready in `/audio/scripts/` - just copy the text and paste into any TTS service!

## File Naming Convention
Save generated files as:
- brennis-sample.mp3
- elara-sample.mp3  
- kael-sample.mp3
- gorok-sample.mp3
- pellor-sample.mp3
- valerius-sample.mp3

Place in `/audio/characters/` directory - the HTML players are already set up!
"""
    
    with open("ALTERNATIVE_TTS_GUIDE.md", 'w') as f:
        f.write(guide)
    
    print("Created ALTERNATIVE_TTS_GUIDE.md with all options!")

def main():
    print("ElevenLabs Alternative TTS Options")
    print("=" * 50)
    print()
    
    # Try Windows TTS first
    success = windows_tts_test()
    
    if not success:
        print("\nWindows TTS didn't work. Creating manual guide...")
        
    # Always create the guide
    create_manual_guide()
    
    print("\nRECOMMENDATION:")
    print("1. Try the free online services in ALTERNATIVE_TTS_GUIDE.md")
    print("2. Use the scripts in /audio/scripts/ for each character")  
    print("3. Save the generated MP3s to /audio/characters/")
    print("4. Your HTML audio players are already embedded and ready!")

if __name__ == "__main__":
    main()