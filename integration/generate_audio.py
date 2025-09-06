#!/usr/bin/env python3
"""
Audio Generation Helper for The Weight of the Crown Campaign
Helps generate AI voice overs using various text-to-speech services
"""

import os
import json
from pathlib import Path
from audio_manager import AudioManager

# Sample text content for each character
CHARACTER_QUOTES = {
    "brennis": {
        "quote": "The law is clear. The fine is five silver.",
        "extended": "My duty is to the office, not the man. The law is the foundation. Without it, we are all savages. Order must be maintained at all costs.",
        "voice_notes": "Deep, authoritative, military bearing. Never emotional, always certain."
    },
    "elara": {
        "quote": "True justice is achieved through order and virtue.",
        "extended": "We must be the exemplars of the law we wish to see. The system can and must be redeemed from within.",
        "voice_notes": "Refined, musical accent with orc undertones. Measured and precise speech."
    },
    "kael": {
        "quote": "Their laws weren't written to protect us; they were written to protect them.",
        "extended": "The only justice we get is the justice we take. The system must be shattered, not reformed.",
        "voice_notes": "Quick, sharp, street-smart with slight rasp. Laced with cynicism and wit."
    },
    "gorok": {
        "quote": "I make no pretty speeches about justice. I take what I want from those too weak to stop me.",
        "extended": "Strength is the only true law. Those too weak to defend what they have don't deserve to keep it.",
        "voice_notes": "Rumbling voice with hill country accent. Speaks rarely, never wastes words."
    },
    "pellor": {
        "quote": "I am merely a humble servant of the realm, Your Grace. Let me handle these... tedious details.",
        "extended": "True power belongs to those intelligent enough to seize it from those too weak to wield it properly.",
        "voice_notes": "Smooth, bureaucratic, deceptively pleasant. Measured and reasonable tones."
    },
    "valerius": {
        "quote": "I never asked for this crown... Perhaps someone else would wear it better.",
        "extended": "Leadership is a burden I was never meant to bear. Others are better suited to make the hard choices.",
        "voice_notes": "Hesitant, weak, constantly seeking approval. Even commands sound like suggestions."
    }
}

SCENE_NARRATIONS = {
    "prologue-opening": {
        "text": """In the morning light of Estellon, three philosophies will collide, and the players will witness the spark that ignites a revolution. 
        
        The morning of the Sunstone Festival dawns bright and clear over Estellon. The central market is a bustling cacophony of merchants hawking wares, citizens shopping, and the city guard watching it all. The air smells of spices, sweat, and the promise of celebration.""",
        "voice_notes": "Dramatic narrator voice, building tension and atmosphere."
    },
    "act1-riot": {
        "text": """As the sun sets, a town crier moves through the districts: 'Hear ye! By order of the Duke's chamberlain, the unsanctioned Sunstone Festival is prohibited! All gatherings will be dispersed! Public disturbances will be dealt with severely!' 
        
        You see squads of the city watch, led by the grim Captain Brennis, already moving into position. The festive mood of the morning has curdled into tension.""",
        "voice_notes": "Start with town crier voice, then shift to dramatic narrator for tension."
    },
    "epilogue-council": {
        "text": """The factions gather in the great hall of the palace, along with key citizens, nobles, and guild leaders. The external threats are defeated. The old regime has ended. 
        
        The PCs are given seats of honor as the ultimate arbiters. The council must decide on justice for the former ruler, and more importantly, the future form of government that will guide Estellon into a new age.""",
        "voice_notes": "Solemn, ceremonial tone. This is the moment of final decision."
    }
}

def generate_script_files():
    """Generate script files for AI voice generation"""
    
    # Create scripts directory
    scripts_dir = Path("audio/scripts")
    scripts_dir.mkdir(exist_ok=True)
    
    # Generate character scripts
    for char, data in CHARACTER_QUOTES.items():
        script_content = f"""# {char.title()} Voice Script

## Character Voice Notes
{data['voice_notes']}

## Short Quote (for quick sample)
{data['quote']}

## Extended Quote (for longer sample)
{data['extended']}

---

## Suggested AI Voice Generation Settings:

### For ElevenLabs:
- Voice: [Choose appropriate voice]
- Stability: 0.7-0.8 (for consistency)
- Clarity: 0.8-0.9
- Style Exaggeration: 0.3-0.5

### For Other TTS Services:
- Tone: {data['voice_notes'].split('.')[0]}
- Speed: Normal to Slow
- Pitch: Adjust based on character age and authority

## Sample Prompts for Character Context:
"Generate this dialogue as {char.title()}, a {get_character_description(char)} in a fantasy setting."
"""
        
        script_file = scripts_dir / f"{char}_script.md"
        with open(script_file, 'w', encoding='utf-8') as f:
            f.write(script_content)
    
    # Generate scene scripts
    for scene, data in SCENE_NARRATIONS.items():
        script_content = f"""# {scene.replace('-', ' ').title()} Narration Script

## Voice Notes
{data['voice_notes']}

## Full Text
{data['text']}

---

## Suggested AI Voice Generation Settings:

### For Narration:
- Voice: Professional narrator voice
- Stability: 0.8-0.9 (for smooth narration)
- Clarity: 0.9
- Style Exaggeration: 0.4-0.6
- Pace: Slightly slower for dramatic effect

## Context Prompt:
"Narrate this text as a dungeon master describing a scene in a fantasy tabletop RPG campaign."
"""
        
        script_file = scripts_dir / f"{scene}_script.md"
        with open(script_file, 'w', encoding='utf-8') as f:
            f.write(script_content)
    
    print(f"Generated {len(CHARACTER_QUOTES) + len(SCENE_NARRATIONS)} script files in {scripts_dir}")

def get_character_description(char):
    """Get brief character description for AI prompting"""
    descriptions = {
        "brennis": "stern military captain and law enforcer",
        "elara": "noble orc paladin seeking justice through reform",
        "kael": "street-smart revolutionary fighting corrupt authority",
        "gorok": "barbarian warlord who values only strength",
        "pellor": "manipulative court official hiding his true nature",
        "valerius": "weak and indecisive ruler overwhelmed by responsibility"
    }
    return descriptions.get(char, "fantasy character")

def create_audio_generation_guide():
    """Create a comprehensive guide for generating audio"""
    
    guide_content = """# Audio Generation Guide for The Weight of the Crown

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
"""
    
    with open("AUDIO_GENERATION_GUIDE.md", 'w', encoding='utf-8') as f:
        f.write(guide_content)
    
    print("Created AUDIO_GENERATION_GUIDE.md")

if __name__ == "__main__":
    print("Setting up audio generation system...")
    
    # Generate script files for each character and scene
    generate_script_files()
    
    # Create comprehensive guide
    create_audio_generation_guide()
    
    print("\n✅ Audio generation system ready!")
    print("\nNext steps:")
    print("1. Check /audio/scripts/ for voice generation scripts")
    print("2. Read AUDIO_GENERATION_GUIDE.md for detailed instructions")
    print("3. Choose your preferred AI voice service")
    print("4. Generate audio files and place them in /audio/ subdirectories")
    print("5. Audio players are already embedded in your markdown files!")