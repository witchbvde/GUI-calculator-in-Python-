import tkinter as tk

def on_button_click(event):
    current_text = entry.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font=("Helvetica", 20), bd=5, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, expand=True)

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

for i in range(4):
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)
    for j in range(4):
        button_text = buttons[i * 4 + j]
        button = tk.Button(frame, text=button_text, font=("Helvetica", 20), bd=3,
                           relief=tk.FLAT, bg="black", fg="white")
        button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        button.bind("<Button-1>", on_button_click)

root.mainloop()
