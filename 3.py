# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, messagebox
import threading

def word_frequency(text):
    word_list = text.lower().split()
    word_count = {}

    for word in word_list:
        word = word.strip(".,!?\"';:()[]{}")
        if word:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count

def analyze_text():
    text = text_entry.get("1.0", "end-1c")
    frequencies = word_frequency(text)

    result_text.delete("1.0", "end")

    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    for word, frequency in sorted_frequencies:
        result_text.insert("end", f"{word}: {frequency}\n")

def run_sentiment_analysis():
    text = text_entry.get("1.0", "end-1c").strip()
    if not text:
        messagebox.showwarning("Предупреждение", "Введите текст для анализа тональности.")
        return

    sentiment_btn.config(state="disabled", text="Анализ...")
    sentiment_result_var.set("Анализирую...")

    def task():
        try:
            from transformers import pipeline
            classifier = pipeline(
                "sentiment-analysis",
                model="blanchefort/rubert-base-cased-sentiment",
                tokenizer="blanchefort/rubert-base-cased-sentiment"
            )
            # Truncate to 512 tokens max
            result = classifier(text[:512])[0]

            label_map = {
                "POSITIVE": "😊 Позитивный",
                "NEGATIVE": "😞 Негативный",
                "NEUTRAL":  "😐 Нейтральный",
            }
            label = label_map.get(result["label"], result["label"])
            score = round(result["score"] * 100, 1)
            sentiment_result_var.set(f"{label}  (уверенность: {score}%)")
        except ImportError:
            sentiment_result_var.set("Ошибка: установите transformers и torch (см. requirements.txt)")
        except Exception as e:
            sentiment_result_var.set(f"Ошибка: {e}")
        finally:
            sentiment_btn.config(state="normal", text="Определить тональность")

    threading.Thread(target=task, daemon=True).start()

def paste_text(event):
    text = root.clipboard_get()
    text_entry.insert(tk.INSERT, text)


root = tk.Tk()
root.title("Анализатор текста")
root.resizable(False, False)

# ── Ввод текста ──────────────────────────────────────────────
tk.Label(root, text="Введите текст для анализа:").pack(pady=(10, 0))
text_entry = tk.Text(root, height=10, width=60)
text_entry.pack(padx=10)
text_entry.bind("<Control-v>", paste_text)

# ── Кнопки ───────────────────────────────────────────────────
btn_frame = tk.Frame(root)
btn_frame.pack(pady=6)

tk.Button(btn_frame, text="Частота слов", command=analyze_text, width=18).pack(side="left", padx=4)

sentiment_btn = tk.Button(btn_frame, text="Определить тональность",
                          command=run_sentiment_analysis, width=22)
sentiment_btn.pack(side="left", padx=4)

# ── Тональность ──────────────────────────────────────────────
sentiment_result_var = tk.StringVar(value="—")
sentiment_frame = tk.LabelFrame(root, text="Тональность текста", padx=8, pady=4)
sentiment_frame.pack(fill="x", padx=10, pady=(0, 6))
tk.Label(sentiment_frame, textvariable=sentiment_result_var, font=("Arial", 13)).pack()

# ── Результат частотного анализа ────────────────────────────
tk.Label(root, text="Частота слов:").pack()
result_text = tk.Text(root, height=10, width=60)
result_text.pack(padx=10, pady=(0, 10))

root.mainloop()
