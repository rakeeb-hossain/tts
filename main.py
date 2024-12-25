import gcp_tts
import tortoise_tts
import xtts_v2

kyon_text = """
I bet everyone thought she was kidding.
But it wasn’t a joke.
And it wasn’t anything to laugh about.
Haruhi is always dead serious.
And that’s how we first met.
Looking back, I wanna believe that it was just a coincidence.
"""

haruhi_text = """
Y'know that appliance store that sponsored our movie? 
Well I just got the owner to give us a heater for free!
He called us up and said he's got an extra one he's trying to get rid of.
"""

def main():
    # gcp_tts.tts("out/output.mp3", "Hello, World!")
    # tortoise_tts.tts("Hello, World!", "out/output.mp3")
    xtts_v2.tts(kyon_text, "out/kyon.mp3")

if __name__ == "__main__":
    main()

