#!/usr/bin/env python3
"""
Test ElevenLabs API key setup
"""

import os
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
        return True
    return False

def test_setup():
    """Test API key configuration"""
    print("Testing ElevenLabs API Key Setup")
    print("=" * 40)
    
    # Check if .env file exists
    env_exists = Path('.env').exists()
    print(f"1. .env file exists: {'YES' if env_exists else 'NO'}")
    
    if not env_exists:
        print("\n❌ You need to create a .env file!")
        print("Steps:")
        print("1. Create a new file called '.env' in this directory")
        print("2. Add this line: ELEVENLABS_API_KEY=your_api_key_here")
        print("3. Replace 'your_api_key_here' with your actual API key")
        return False
    
    # Load .env file
    load_env_file()
    
    # Check if API key is set
    api_key = os.getenv('ELEVENLABS_API_KEY')
    if api_key:
        # Mask the key for security
        masked_key = api_key[:10] + "..." + api_key[-4:] if len(api_key) > 14 else "***"
        print(f"2. API key loaded: {masked_key}")
        print("✅ API key is configured!")
        
        # Test connection to ElevenLabs
        try:
            import requests
            headers = {
                "Accept": "application/json",
                "xi-api-key": api_key
            }
            response = requests.get("https://api.elevenlabs.io/v1/voices", headers=headers)
            if response.status_code == 200:
                voices = response.json()["voices"]
                print(f"3. API connection: SUCCESS ({len(voices)} voices available)")
                return True
            else:
                print(f"3. API connection: FAILED (Status: {response.status_code})")
                print("   Check if your API key is correct")
                return False
        except Exception as e:
            print(f"3. API connection: ERROR ({e})")
            return False
    else:
        print("2. API key loaded: NO")
        print("❌ API key not found in .env file")
        print("Make sure your .env file contains: ELEVENLABS_API_KEY=your_actual_key")
        return False

if __name__ == "__main__":
    test_setup()