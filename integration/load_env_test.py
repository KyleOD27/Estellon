#!/usr/bin/env python3
"""
Test loading .env file properly
"""

import os
from pathlib import Path

# Load .env file manually
def load_env():
    env_path = Path('.env')
    if env_path.exists():
        print(f"Found .env file at: {env_path.absolute()}")
        with open(env_path, 'r') as f:
            content = f.read()
            print("File contents:")
            for i, line in enumerate(content.split('\n'), 1):
                if line.strip():
                    print(f"  {i}: {line}")
            
        # Load environment variables
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key] = value
                    print(f"Loaded: {key}=***{value[-4:] if len(value) > 4 else '***'}")
    else:
        print(f"No .env file found at: {env_path.absolute()}")
        return False
    
    return True

if __name__ == "__main__":
    print("Testing .env file loading...")
    print("=" * 40)
    
    # Check current directory
    print(f"Current directory: {Path.cwd()}")
    
    # Load .env
    if load_env():
        # Test if API key is available
        api_key = os.getenv('ELEVENLABS_API_KEY')
        if api_key:
            print(f"\nSUCCESS: API key loaded!")
            print(f"Key starts with: {api_key[:10]}...")
        else:
            print(f"\nFAILED: API key not found in environment")
    else:
        print("\nFAILED: Could not load .env file")