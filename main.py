"""Display three-word sentences for three seconds each. Run: py main.py"""

import tkinter as tk
from itertools import cycle


# Edit this list to use your own three-word sentences.
SENTENCES = [
    "Birds can fly.",
    "The sun shines.",
    "Flowers smell sweet.",
    "We love music.",
    "Dogs are friendly.",
    "She reads books.",
]
INTERVAL_MS = 3000


def main():
    if not SENTENCES or any(len(sentence.split()) != 3 for sentence in SENTENCES):
        raise ValueError("Provide at least one sentence, with exactly three words each.")

    window = tk.Tk()
    window.title("Three-Word Sentences")
    window.geometry("900x500")
    window.configure(bg="#101827")

    sentence_label = tk.Label(
        window,
        font=("Arial", 42, "bold"),
        fg="white",
        bg="#101827",
        wraplength=850,
    )
    sentence_label.pack(expand=True, fill="both", padx=24, pady=24)
    tk.Label(
        window,
        text="A new sentence every 3 seconds  |  Esc to exit",
        font=("Arial", 12),
        fg="#b8c4d8",
        bg="#101827",
    ).pack(pady=16)

    sentences = cycle(SENTENCES)

    def show_next_sentence():
        sentence_label.config(text=next(sentences))
        window.after(INTERVAL_MS, show_next_sentence)

    window.bind("<Escape>", lambda event: window.destroy())
    show_next_sentence()
    window.mainloop()


if __name__ == "__main__":
    main()
