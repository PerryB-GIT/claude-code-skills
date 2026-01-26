#!/usr/bin/env python3
"""
Evie Voice Generator - Edge TTS (Free, no API key needed)
Same Microsoft neural voices as Azure, completely free

Usage:
    python evie-speak-edge.py "Hello, love."
    python evie-speak-edge.py --play "Your meeting is in 15 minutes."
    python evie-speak-edge.py --save greeting.mp3 "Good morning, darling."
"""

import subprocess
import sys
import asyncio
import argparse
from pathlib import Path
import tempfile

# Install edge-tts if needed
try:
    import edge_tts
except ImportError:
    print("Installing edge-tts...")
    subprocess.run([sys.executable, "-m", "pip", "install", "edge-tts"], check=True)
    import edge_tts

# Evie's voice - British English, warm female
EVIE_VOICE = "en-GB-SoniaNeural"  # Warm, professional British female
BACKUP_VOICE = "en-GB-LibbyNeural"  # Friendly, conversational British female

# Voice styling - natural British cadence, no unnatural pauses
VOICE_CONFIG = {
    "default": {"rate": "+8%", "pitch": "-2Hz"},
    "greeting": {"rate": "+5%", "pitch": "+0Hz"},
    "alert": {"rate": "+15%", "pitch": "+5Hz"},
    "encouragement": {"rate": "+3%", "pitch": "-3Hz"},
    "urgent": {"rate": "+20%", "pitch": "+8Hz"},
}

async def generate_speech(text: str, output_file: str, style: str = "default"):
    """Generate speech with Evie's voice."""
    config = VOICE_CONFIG.get(style, VOICE_CONFIG["default"])

    communicate = edge_tts.Communicate(
        text,
        EVIE_VOICE,
        rate=config["rate"],
        pitch=config["pitch"]
    )

    await communicate.save(output_file)
    return output_file

def play_audio(file_path: str):
    """Play audio file using system default player."""
    import platform

    system = platform.system()
    if system == "Windows":
        # Use Windows Media Player or default
        subprocess.run(["powershell", "-c", f"(New-Object Media.SoundPlayer '{file_path}').PlaySync()"], check=True)
    elif system == "Darwin":  # macOS
        subprocess.run(["afplay", file_path], check=True)
    else:  # Linux
        subprocess.run(["aplay", file_path], check=True)

def speak(text: str, style: str = "default", output_file: str = None, play: bool = True):
    """Speak text with Evie's voice."""

    # Determine output file
    if output_file:
        out_path = output_file
        should_cleanup = False
    else:
        # Use temp file
        temp = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
        out_path = temp.name
        temp.close()
        should_cleanup = play  # Only cleanup if we're playing

    print(f"[Evie speaking...]")

    # Generate audio
    asyncio.run(generate_speech(text, out_path, style))

    if output_file:
        print(f"[OK] Saved to: {output_file}")

    if play:
        # Convert to wav for Windows playback
        wav_path = out_path.replace(".mp3", ".wav")
        try:
            # Try ffmpeg first
            result = subprocess.run(
                ["ffmpeg", "-y", "-i", out_path, "-ar", "22050", wav_path],
                capture_output=True
            )
            if result.returncode == 0:
                play_audio(wav_path)
                Path(wav_path).unlink(missing_ok=True)
            else:
                # Fallback: use PowerShell with Windows Media Player
                subprocess.run([
                    "powershell", "-c",
                    f"Add-Type -AssemblyName presentationCore; $player = New-Object System.Windows.Media.MediaPlayer; $player.Open('{out_path}'); Start-Sleep -Milliseconds 500; $player.Play(); while($player.Position -lt $player.NaturalDuration.TimeSpan) {{ Start-Sleep -Milliseconds 100 }}; $player.Close()"
                ], check=True)
        except FileNotFoundError:
            # No ffmpeg, try direct
            print("(Install ffmpeg for better audio playback)")
            subprocess.run([
                "powershell", "-c",
                f"Add-Type -AssemblyName presentationCore; $player = New-Object System.Windows.Media.MediaPlayer; $player.Open('{out_path}'); Start-Sleep -Milliseconds 500; $player.Play(); while($player.Position -lt $player.NaturalDuration.TimeSpan) {{ Start-Sleep -Milliseconds 100 }}; $player.Close()"
            ], check=True)

    if should_cleanup:
        Path(out_path).unlink(missing_ok=True)

    print("[OK] Done")

def main():
    parser = argparse.ArgumentParser(description="Evie Voice (Edge TTS - Free)")
    parser.add_argument("text", nargs="?", help="Text for Evie to speak")
    parser.add_argument("--style", "-s", default="default",
                       choices=["default", "greeting", "alert", "encouragement", "urgent"],
                       help="Speaking style")
    parser.add_argument("--save", "-o", help="Save to MP3 file")
    parser.add_argument("--play", "-p", action="store_true", default=True,
                       help="Play audio (default: True)")
    parser.add_argument("--no-play", action="store_true", help="Don't play, just save")
    parser.add_argument("--list-voices", action="store_true", help="List available British voices")

    args = parser.parse_args()

    if args.list_voices:
        print("\nAvailable British Female Voices:")
        print("-" * 40)
        voices = [
            ("en-GB-SoniaNeural", "Warm, professional (Evie's voice)"),
            ("en-GB-LibbyNeural", "Friendly, conversational"),
            ("en-GB-MaisieNeural", "Young, energetic"),
        ]
        for voice, desc in voices:
            print(f"  {voice}: {desc}")
        return

    if not args.text:
        text = "Good morning, love. I'm Evie, your executive assistant. I'll be keeping you organised, on track, and well looked after. Shall we get started?"
    else:
        text = args.text

    play = not args.no_play
    speak(text, args.style, args.save, play)

if __name__ == "__main__":
    main()
