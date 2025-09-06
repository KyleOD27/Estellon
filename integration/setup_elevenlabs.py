#!/usr/bin/env python3
"""
Simple ElevenLabs API key setup (Windows-compatible)
"""

import os
from pathlib import Path

def setup_api_key():
    """Interactive setup for ElevenLabs API key"""
    print("ElevenLabs API Key Setup")
    print("=" * 40)
    print("1. Go to https://elevenlabs.io/")
    print("2. Sign in to your account") 
    print("3. Go to Profile > API Key")
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
        
        print("API key configured!")
        print("Saved to .env file for future use")
        
        # Add .env to .gitignore if it exists
        gitignore_path = Path('.gitignore')
        if gitignore_path.exists():
            with open(gitignore_path, 'r') as f:
                content = f.read()
            if '.env' not in content:
                with open(gitignore_path, 'a') as f:
                    f.write('\n# Environment variables\n.env\n')
                print("Added .env to .gitignore for security")
        
        return api_key
    else:
        print("No API key provided")
        return None

if __name__ == "__main__":
    setup_api_key()