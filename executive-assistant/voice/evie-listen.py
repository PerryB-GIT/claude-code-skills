#!/usr/bin/env python3
"""
Evie Voice Listener - Speech-to-Text
Captures audio from microphone and transcribes using Whisper

Usage:
    python evie-listen.py                    # Listen once, return text
    python evie-listen.py --continuous       # Keep listening until "goodbye Evie"
    python evie-listen.py --wake-word        # Wait for "Hey Evie" to activate
    python evie-listen.py --timeout 10       # Listen for 10 seconds max
"""

import subprocess
import sys
import argparse
import os

# Install dependencies if needed
def ensure_deps():
    deps = [
        ("speech_recognition", "SpeechRecognition"),
        ("pyaudio", "pyaudio"),
        ("whisper", "openai-whisper"),
    ]
    for module, package in deps:
        try:
            __import__(module)
        except ImportError:
            print(f"Installing {package}...")
            subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)

ensure_deps()

import speech_recognition as sr
import whisper
import tempfile
import warnings

# Suppress whisper FP16 warning on CPU
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU")

# Global whisper model (loaded once)
_whisper_model = None

def get_whisper_model(model_size="base"):
    """Load whisper model (cached)."""
    global _whisper_model
    if _whisper_model is None:
        print(f"[Evie] Loading speech recognition model ({model_size})...")
        _whisper_model = whisper.load_model(model_size)
        print("[Evie] Ready to listen.")
    return _whisper_model

def list_microphones():
    """List available microphones."""
    print("\nAvailable Microphones:")
    print("-" * 40)
    for i, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"  [{i}] {name}")
    print()

def listen_once(timeout=5, phrase_limit=None, mic_index=None, use_whisper=True):
    """
    Listen for a single utterance and return transcribed text.

    Args:
        timeout: Max seconds to wait for speech to start
        phrase_limit: Max seconds of speech to capture
        mic_index: Specific microphone index (None = default)
        use_whisper: Use Whisper (True) or Google Speech API (False)

    Returns:
        Transcribed text or None if failed
    """
    recognizer = sr.Recognizer()

    # Adjust for ambient noise
    mic_kwargs = {"device_index": mic_index} if mic_index is not None else {}

    try:
        with sr.Microphone(**mic_kwargs) as source:
            print("[Evie] Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            print("[Evie] Listening... (speak now)")
            audio = recognizer.listen(
                source,
                timeout=timeout,
                phrase_time_limit=phrase_limit
            )
            print("[Evie] Processing...")

            if use_whisper:
                # Use Whisper for transcription
                model = get_whisper_model()

                # Save audio to temp file
                with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
                    f.write(audio.get_wav_data())
                    temp_path = f.name

                try:
                    result = model.transcribe(temp_path, fp16=False)
                    text = result["text"].strip()
                finally:
                    os.unlink(temp_path)
            else:
                # Use Google Speech Recognition (requires internet)
                text = recognizer.recognize_google(audio)

            return text

    except sr.WaitTimeoutError:
        print("[Evie] No speech detected.")
        return None
    except sr.UnknownValueError:
        print("[Evie] Couldn't understand that.")
        return None
    except sr.RequestError as e:
        print(f"[Evie] Speech service error: {e}")
        return None
    except Exception as e:
        print(f"[Evie] Error: {e}")
        return None

def listen_continuous(wake_word=None, exit_phrase="goodbye evie", mic_index=None):
    """
    Continuously listen and yield transcriptions.

    Args:
        wake_word: If set, only process after hearing this phrase
        exit_phrase: Stop listening when this is heard
        mic_index: Specific microphone index

    Yields:
        Transcribed text for each utterance
    """
    print(f"[Evie] Continuous listening mode.")
    if wake_word:
        print(f"[Evie] Say '{wake_word}' to activate.")
    print(f"[Evie] Say '{exit_phrase}' to stop.\n")

    waiting_for_wake = wake_word is not None

    while True:
        if waiting_for_wake:
            print("[Evie] Waiting for wake word...")

        text = listen_once(timeout=None, phrase_limit=15, mic_index=mic_index)

        if text is None:
            continue

        text_lower = text.lower().strip()

        # Check for exit
        if exit_phrase in text_lower:
            print("[Evie] Goodbye, love. Chat soon.")
            break

        # Check for wake word
        if waiting_for_wake:
            if wake_word.lower() in text_lower:
                print("[Evie] Yes, love? I'm listening...")
                waiting_for_wake = False
                # Remove wake word from text
                text = text_lower.replace(wake_word.lower(), "").strip()
                if text:
                    yield text
            continue

        # Normal mode - yield the text
        if text:
            print(f"[You said] {text}")
            yield text

        # Reset wake word requirement after each command
        if wake_word:
            waiting_for_wake = True

def main():
    parser = argparse.ArgumentParser(description="Evie Voice Listener")
    parser.add_argument("--continuous", "-c", action="store_true",
                       help="Continuous listening mode")
    parser.add_argument("--wake-word", "-w", default=None,
                       help="Wake word to activate (e.g., 'hey evie')")
    parser.add_argument("--timeout", "-t", type=int, default=5,
                       help="Seconds to wait for speech (default: 5)")
    parser.add_argument("--phrase-limit", "-p", type=int, default=None,
                       help="Max seconds of speech to capture")
    parser.add_argument("--mic", "-m", type=int, default=None,
                       help="Microphone index (use --list-mics to see options)")
    parser.add_argument("--list-mics", action="store_true",
                       help="List available microphones")
    parser.add_argument("--google", action="store_true",
                       help="Use Google Speech API instead of Whisper")

    args = parser.parse_args()

    if args.list_mics:
        list_microphones()
        return

    use_whisper = not args.google

    if args.continuous:
        for text in listen_continuous(
            wake_word=args.wake_word,
            mic_index=args.mic
        ):
            # In standalone mode, just print
            # When imported, the caller handles the text
            pass
    else:
        text = listen_once(
            timeout=args.timeout,
            phrase_limit=args.phrase_limit,
            mic_index=args.mic,
            use_whisper=use_whisper
        )
        if text:
            print(f"\n[Transcription] {text}")
            return text
        return None

if __name__ == "__main__":
    main()
