# -*- coding: utf-8 -*-
import tkinter as tk

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

def paste_text(event):
    text = root.clipboard_get()
    text_entry.insert(tk.INSERT, text)


root = tk.Tk()
root.title("Анализатор частоты слов")


text_entry_label = tk.Label(root, text="Введите текст для анализа:")
text_entry_label.pack()

text_entry = tk.Text(root, height=10, width=50)
text_entry.pack()

analyze_button = tk.Button(root, text="Анализировать", command=analyze_text)
analyze_button.pack()

result_text_label = tk.Label(root, text="Результат анализа:")
result_text_label.pack()

result_text = tk.Text(root, height=10, width=50)
result_text.pack()


text_entry.bind("<Control-v>", paste_text)


root.mainloop()
