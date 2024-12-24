import gcp_tts
import tortoise_tts

def main():
    # gcp_tts.tts("out/output.mp3", "Hello, World!")
    tortoise_tts.tts("Hello, World!", "out/output.mp3")

if __name__ == "__main__":
    main()

