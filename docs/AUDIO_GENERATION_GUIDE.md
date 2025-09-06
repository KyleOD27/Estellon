# Audio Generation Guide for The Weight of the Crown

## Overview
This guide helps you generate AI voice overs for the campaign using various text-to-speech services.

## Recommended AI Voice Services

### 1. ElevenLabs (Recommended)
- **Best for:** Character voices, high quality
- **Pricing:** Subscription-based
- **Features:** Voice cloning, emotion control, multiple voices

### 2. Murf
- **Best for:** Narrator voices, professional sound
- **Pricing:** Subscription-based  
- **Features:** Multiple accents, business-focused

### 3. Azure Cognitive Services Speech
- **Best for:** Python integration, cost-effective
- **Pricing:** Pay-per-use
- **Features:** SSML support, custom voices

### 4. Free Alternatives
- **Windows:** Built-in Speech Platform
- **Python:** pyttsx3 library
- **Online:** Natural Reader, TTSMaker

## Character Voice Mapping

| Character | Voice Type | Key Traits | AI Voice Suggestions |
|-----------|------------|------------|---------------------|
| Brennis | Deep Male | Authoritative, military | Choose stern, older male voice |
| Elara | Female | Refined, musical accent | Elegant female with slight accent |
| Kael | Young Female | Street-smart, raspy | Energetic, slightly rough female |
| Gorok | Deep Male | Rumbling, rural accent | Very deep, gruff male voice |
| Pellor | Male | Smooth, bureaucratic | Pleasant, professional male |
| Valerius | Male | Hesitant, weak | Nervous, uncertain male voice |

## Generation Workflow

1. **Choose your TTS service**
2. **Use the script files in `/audio/scripts/`**
3. **Apply character voice settings**
4. **Generate audio files**
5. **Save to appropriate `/audio/` subdirectory**
6. **Test in markdown files**

## File Naming Convention
- Character samples: `{character}-sample.mp3`
- Scene narration: `{scene}-{description}.mp3`
- Multiple takes: `{name}-v{number}.mp3`

## Integration Steps
1. Generate audio file
2. Place in correct `/audio/` subdirectory
3. Audio players are already embedded in markdown files
4. Test playback in your markdown viewer

## Python Integration (Advanced)

```python
from audio_manager import AudioManager

# Initialize audio manager
manager = AudioManager()

# Add new audio file
manager.add_character_audio(
    character="brennis",
    audio_file="brennis-sample-v2.mp3", 
    quote="New quote here",
    description="Updated voice"
)

# Generate HTML for embedding
html = manager.generate_character_audio_section("brennis")
print(html)
```

## Tips for Better Results

1. **Voice Consistency:** Use the same AI voice/settings for each character
2. **Context Prompts:** Include character background in AI prompts
3. **Multiple Takes:** Generate several versions, keep the best
4. **Post-Processing:** Consider light audio editing for consistency
5. **File Formats:** Use MP3 for compatibility, OGG as fallback

## Troubleshooting

**Audio not playing?**
- Check file paths in HTML
- Ensure files exist in `/audio/` directories
- Try different browsers

**Poor voice quality?**
- Adjust TTS service settings
- Try different AI voices
- Consider professional voice acting for key characters

**Python script errors?**
- Check file paths are correct
- Ensure audio directories exist
- Verify audio_manager.py is working
