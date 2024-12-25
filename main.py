import gcp_tts
import tortoise_tts
import xtts_v2

def main():
    # gcp_tts.tts("out/output.mp3", "Hello, World!")
    # tortoise_tts.tts("Hello, World!", "out/output.mp3")
    xtts_v2.tts("Hello, World!", "out/output.mp3")

if __name__ == "__main__":
    main()

