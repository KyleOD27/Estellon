#!/usr/bin/env python3
"""
Update all HTML audio players to use WAV files
"""

import os
from pathlib import Path

def update_audio_players():
    """Update all character profiles to use WAV files"""
    
    character_files = [
        "characters/brennis-profile.md",
        "characters/elara-profile.md", 
        "characters/kael-profile.md",
        "characters/gorok-profile.md",
        "characters/pellor-profile.md",
        "characters/valerius-profile.md"
    ]
    
    updates_made = 0
    
    for file_path in character_files:
        if Path(file_path).exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract character name from file path
            char_name = Path(file_path).stem.split('-')[0]
            
            # Update the audio source to WAV
            old_mp3_line = f'        <source src="../audio/characters/{char_name}-sample.mp3" type="audio/mpeg">'
            new_wav_line = f'        <source src="../audio/characters/{char_name}-sample.wav" type="audio/wav">'
            
            if old_mp3_line in content:
                content = content.replace(old_mp3_line, new_wav_line)
                
                # Also update the download link
                old_download = f'        <a href="../audio/characters/{char_name}-sample.mp3">Download audio file</a>'
                new_download = f'        <a href="../audio/characters/{char_name}-sample.wav">Download audio file</a>'
                
                if old_download in content:
                    content = content.replace(old_download, new_download)
                
                # Write back
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"Updated {file_path}")
                updates_made += 1
            else:
                print(f"No MP3 reference found in {file_path}")
    
    print(f"\nUpdated {updates_made} character profiles to use WAV files!")
    
def test_audio_files():
    """Test that all audio files exist"""
    print("\nChecking audio files...")
    
    characters = ["brennis", "elara", "kael", "gorok", "pellor", "valerius"]
    
    for char in characters:
        wav_path = Path(f"audio/characters/{char}-sample.wav")
        if wav_path.exists():
            size = wav_path.stat().st_size
            print(f"  {char.title()}: {size} bytes - OK")
        else:
            print(f"  {char.title()}: MISSING")

def create_test_html():
    """Create a test HTML file to check audio players"""
    html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Audio Test - The Weight of the Crown</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .character { margin-bottom: 30px; padding: 20px; border: 1px solid #ccc; }
        .audio-player { margin: 10px 0; }
        audio { width: 100%; }
    </style>
</head>
<body>
    <h1>Character Voice Test</h1>
    
    <div class="character">
        <h2>Brennis - Captain of the Guard</h2>
        <div class="audio-player">
            <p><strong>🎵 Brennis's Voice</strong></p>
            <audio controls style="width: 100%;">
                <source src="audio/characters/brennis-sample.wav" type="audio/wav">
                Your browser does not support the audio element.
            </audio>
        </div>
        <p><em>"The law is clear. The fine is five silver."</em></p>
    </div>
    
    <div class="character">
        <h2>Elara - The Reformer</h2>
        <div class="audio-player">
            <p><strong>🎵 Elara's Voice</strong></p>
            <audio controls style="width: 100%;">
                <source src="audio/characters/elara-sample.wav" type="audio/wav">
                Your browser does not support the audio element.
            </audio>
        </div>
        <p><em>"True justice is achieved through order and virtue."</em></p>
    </div>
    
    <div class="character">
        <h2>Kael - The Revolutionary</h2>
        <div class="audio-player">
            <p><strong>🎵 Kael's Voice</strong></p>
            <audio controls style="width: 100%;">
                <source src="audio/characters/kael-sample.wav" type="audio/wav">
                Your browser does not support the audio element.
            </audio>
        </div>
        <p><em>"Their laws weren't written to protect us."</em></p>
    </div>
    
    <div class="character">
        <h2>Gorok - The Barbarian King</h2>
        <div class="audio-player">
            <p><strong>🎵 Gorok's Voice</strong></p>
            <audio controls style="width: 100%;">
                <source src="audio/characters/gorok-sample.wav" type="audio/wav">
                Your browser does not support the audio element.
            </audio>
        </div>
        <p><em>"I make no pretty speeches about justice."</em></p>
    </div>
    
    <div class="character">
        <h2>Pellor - The Chamberlain</h2>
        <div class="audio-player">
            <p><strong>🎵 Pellor's Voice</strong></p>
            <audio controls style="width: 100%;">
                <source src="audio/characters/pellor-sample.wav" type="audio/wav">
                Your browser does not support the audio element.
            </audio>
        </div>
        <p><em>"I am merely a humble servant of the realm, Your Grace."</em></p>
    </div>
    
    <div class="character">
        <h2>Valerius - The Weak Duke</h2>
        <div class="audio-player">
            <p><strong>🎵 Valerius's Voice</strong></p>
            <audio controls style="width: 100%;">
                <source src="audio/characters/valerius-sample.wav" type="audio/wav">
                Your browser does not support the audio element.
            </audio>
        </div>
        <p><em>"I never asked for this crown."</em></p>
    </div>
    
    <hr>
    <p><strong>Instructions:</strong></p>
    <ul>
        <li>Click the play button on each audio player to test the voices</li>
        <li>If audio doesn't play, check that the WAV files exist in audio/characters/</li>
        <li>Try opening this file in different browsers (Chrome, Firefox, Edge)</li>
    </ul>
    
</body>
</html>"""
    
    with open("AUDIO_TEST.html", 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("Created AUDIO_TEST.html - open this in your browser to test all voices!")

if __name__ == "__main__":
    print("Updating Audio Players for WAV Files")
    print("=" * 50)
    
    update_audio_players()
    test_audio_files() 
    create_test_html()
    
    print("\nAll done! Your audio system is ready:")
    print("1. All character profiles now use WAV audio files")
    print("2. Open AUDIO_TEST.html in your browser to test all voices")
    print("3. Open any character profile markdown to see embedded audio")
    print("4. Audio files are in /audio/characters/")