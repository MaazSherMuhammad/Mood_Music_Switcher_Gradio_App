# app.py

import gradio as gr
from mood_logic import detect_mood, suggest_song

def mood_suggester(user_input):
    mood = detect_mood(user_input)
    if mood:
        song, link, message = suggest_song(mood)
        return f"🎶 **Suggested Song:** [{song}]({link})\n\n💬 **Message:** {message}"
    else:
        return "😕 Sorry, I couldn't detect your mood. Try using words like *happy*, *sad*, *relaxed*, *stressed*, or *excited*."

iface = gr.Interface(
    fn=mood_suggester,
    inputs=gr.Textbox(lines=2, placeholder="Type how you're feeling..."),
    outputs="markdown",
    title="Mood Music Suggester 🎧",
    description="Describe your mood, and get a matching song with a motivational message!"
)

if __name__ == "__main__":
  iface.launch(share=True)

