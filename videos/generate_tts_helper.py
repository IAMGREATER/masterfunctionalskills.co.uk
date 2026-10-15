import subprocess
import time
import os

def generate_voiceover(text, output_path, voice="en-GB-RyanNeural"):
    # If already generated and valid, skip
    if os.path.exists(output_path) and os.path.getsize(output_path) > 1000:
        print(f"Already exists: {output_path}")
        return True
        
    for attempt in range(3):
        try:
            print(f"Calling edge-tts (attempt {attempt+1}) for {os.path.basename(output_path)}...")
            cmd = [
                "uvx", "edge-tts",
                "--voice", voice,
                "--rate=-3%",
                "--text", text,
                "--write-media", output_path
            ]
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            if res.returncode == 0 and os.path.exists(output_path) and os.path.getsize(output_path) > 1000:
                print(f"Successfully generated: {output_path}")
                time.sleep(1.5)
                return True
            else:
                print(f"Warning: returncode {res.returncode}, stderr: {res.stderr[:200]}")
        except Exception as e:
            print(f"Error on attempt {attempt+1}: {e}")
        time.sleep(2.0)
        
    # Fallback to gTTS
    print(f"Falling back to gTTS for {output_path}...")
    try:
        cmd_gtts = [
            "uvx", "--from", "gTTS", "gtts-cli",
            "--lang", "en",
            "--tld", "co.uk",
            "-o", output_path,
            text
        ]
        subprocess.run(cmd_gtts, check=True, timeout=30)
        print(f"gTTS fallback succeeded: {output_path}")
        return True
    except Exception as e:
        print(f"Failed gTTS fallback: {e}")
        return False

if __name__ == "__main__":
    t = "This is a test of the resilient voiceover generator."
    generate_voiceover(t, "/home/subi/Projects/masterfunctionalskills.co.uk/videos/test_helper.mp3")
