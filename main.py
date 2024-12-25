import gcp_tts
import tortoise_tts
import xtts_v2


def main():
    # gcp_tts.tts("out/output.mp3", "Hello, World!")
    # tortoise_tts.tts("Hello, World!", "out/output.mp3")
    xtts_v2.tts(
        """
                I'm a little teapot, short and stout, here is my handle, here is my spout.
                When I get all steamed up, hear me shout, just tip me over and pour me out.
                """,
        "out/output.mp3",
    )


if __name__ == "__main__":
    main()
