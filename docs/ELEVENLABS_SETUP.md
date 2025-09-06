# ElevenLabs Setup Instructions

## Step 1: Get Your API Key

1. Go to [https://elevenlabs.io/](https://elevenlabs.io/)
2. Sign in to your account
3. Click on your profile (top right)
4. Go to **"Profile"** → **"API Key"**
5. Copy your API key (it looks like: `sk_1234567890abcdef...`)

## Step 2: Create .env File

1. In your project directory `C:\Users\win11\PycharmProjects\Estellon\`
2. Create a new file called `.env` (note the dot at the beginning)
3. Add this line to the file:

```
ELEVENLABS_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with the actual API key you copied.

## Step 3: Test Your Setup

Run this command to test your API key:

```bash
python -c "import os; print('API Key found!' if os.getenv('ELEVENLABS_API_KEY') else 'No API key found')"
```

## Step 4: Browse Available Voices

Once your API key is set up, run:

```bash
python -c "from elevenlabs_integration import browse_voices; browse_voices()"
```

## What's Next?

After setting up your API key, you'll be able to:

1. ✅ Browse all available ElevenLabs voices
2. ✅ Generate character voice samples automatically  
3. ✅ Create scene narrations
4. ✅ Test audio playback in your campaign documents

## Security Note

The `.env` file contains your private API key. Never share this file or commit it to version control!