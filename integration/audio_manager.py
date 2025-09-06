#!/usr/bin/env python3
"""
Audio Manager for The Weight of the Crown Campaign
Manages audio file integration with markdown documentation
"""

import os
import json
from pathlib import Path
from typing import Dict, List, Optional

class AudioManager:
    """Manages audio files and their integration into campaign documents"""
    
    def __init__(self, project_root: str = ".."):
        self.project_root = Path(project_root)
        self.audio_dir = self.project_root / "audio"
        self.config_file = self.audio_dir / "audio_config.json"
        self.audio_manifest = self._load_manifest()
    
    def _load_manifest(self) -> Dict:
        """Load or create audio manifest"""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return {
            "characters": {},
            "scenes": {},
            "narration": {},
            "epilogue_variants": {}
        }
    
    def save_manifest(self):
        """Save audio manifest to config file"""
        os.makedirs(self.audio_dir, exist_ok=True)
        with open(self.config_file, 'w') as f:
            json.dump(self.audio_manifest, f, indent=2)
    
    def add_character_audio(self, character: str, audio_file: str, 
                           quote: str, description: str = ""):
        """Add character voice sample"""
        self.audio_manifest["characters"][character] = {
            "file": audio_file,
            "quote": quote,
            "description": description,
            "relative_path": f"audio/characters/{audio_file}"
        }
        self.save_manifest()
    
    def add_scene_audio(self, scene: str, audio_file: str, 
                       description: str, location: str):
        """Add scene audio"""
        self.audio_manifest["scenes"][scene] = {
            "file": audio_file,
            "description": description,
            "location": location,
            "relative_path": f"audio/scenes/{audio_file}"
        }
        self.save_manifest()
    
    def add_narration_audio(self, narration_id: str, audio_file: str, 
                           description: str, content: str):
        """Add narration audio"""
        self.audio_manifest["narration"][narration_id] = {
            "file": audio_file,
            "description": description,
            "content": content,
            "relative_path": f"audio/narration/{audio_file}"
        }
        self.save_manifest()
    
    def generate_audio_player_html(self, audio_path: str, 
                                 description: str = "") -> str:
        """Generate HTML audio player code"""
        return f'''
<div class="audio-player">
    <p><strong>🎵 {description}</strong></p>
    <audio controls style="width: 100%;">
        <source src="{audio_path}" type="audio/mpeg">
        <source src="{audio_path.replace('.mp3', '.ogg')}" type="audio/ogg">
        Your browser does not support the audio element.
        <a href="{audio_path}">Download audio file</a>
    </audio>
</div>
'''
    
    def generate_character_audio_section(self, character: str) -> str:
        """Generate character audio section for profiles"""
        if character.lower() not in self.audio_manifest["characters"]:
            return ""
        
        char_data = self.audio_manifest["characters"][character.lower()]
        return f'''
## Character Voice Sample

{self.generate_audio_player_html(char_data["relative_path"], f"{character}'s Voice")}

> *"{char_data["quote"]}"*

{char_data.get("description", "")}
'''
    
    def generate_scene_audio_section(self, scene: str) -> str:
        """Generate scene audio section"""
        if scene not in self.audio_manifest["scenes"]:
            return ""
        
        scene_data = self.audio_manifest["scenes"][scene]
        return f'''
## Scene Audio

{self.generate_audio_player_html(scene_data["relative_path"], scene_data["description"])}
'''
    
    def get_character_audio_list(self) -> List[str]:
        """Get list of characters with audio"""
        return list(self.audio_manifest["characters"].keys())
    
    def get_scene_audio_list(self) -> List[str]:
        """Get list of scenes with audio"""
        return list(self.audio_manifest["scenes"].keys())
    
    def create_audio_placeholder_files(self):
        """Create placeholder audio files for testing"""
        # Create empty placeholder files
        placeholders = [
            "audio/characters/brennis-sample.mp3",
            "audio/characters/elara-sample.mp3", 
            "audio/characters/kael-sample.mp3",
            "audio/characters/gorok-sample.mp3",
            "audio/characters/pellor-sample.mp3",
            "audio/characters/valerius-sample.mp3"
        ]
        
        for placeholder in placeholders:
            file_path = self.project_root / placeholder
            os.makedirs(file_path.parent, exist_ok=True)
            if not file_path.exists():
                # Create empty file
                file_path.touch()
                print(f"Created placeholder: {placeholder}")

def initialize_campaign_audio():
    """Initialize audio system with campaign characters and scenes"""
    manager = AudioManager()
    
    # Add character voice samples
    characters = [
        ("brennis", "brennis-sample.mp3", "The law is clear. The fine is five silver.", "Deep, authoritative military voice"),
        ("elara", "elara-sample.mp3", "True justice is achieved through order and virtue.", "Refined voice with musical accent"),
        ("kael", "kael-sample.mp3", "Their laws weren't written to protect us.", "Quick, street-smart, slightly raspy"),
        ("gorok", "gorok-sample.mp3", "I make no pretty speeches about justice.", "Rumbling voice with hill country accent"),
        ("pellor", "pellor-sample.mp3", "I am merely a humble servant of the realm.", "Smooth, deceptively pleasant bureaucratic voice"),
        ("valerius", "valerius-sample.mp3", "I never asked for this crown...", "Hesitant, weak voice seeking approval")
    ]
    
    for char, file, quote, desc in characters:
        manager.add_character_audio(char, file, quote, desc)
    
    # Add scene audio
    scenes = [
        ("prologue-opening", "Prologue Opening Narration", "story/prologue.md"),
        ("act1-riot", "Festival Riot Scene", "story/act i/act-i.md"),
        ("epilogue-council", "Council Chamber Scene", "story/epilogue.md")
    ]
    
    for scene, file, desc, location in scenes:
        manager.add_scene_audio(scene, file, desc, location)
    
    # Create placeholder files for testing
    manager.create_audio_placeholder_files()
    
    return manager

if __name__ == "__main__":
    # Initialize the audio system
    manager = initialize_campaign_audio()
    print("Audio system initialized!")
    print(f"Characters with audio: {manager.get_character_audio_list()}")
    print(f"Scenes with audio: {manager.get_scene_audio_list()}")
    
    # Example: Generate HTML for Brennis
    print("\nExample character audio HTML:")
    print(manager.generate_character_audio_section("brennis"))