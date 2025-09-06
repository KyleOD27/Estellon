
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
