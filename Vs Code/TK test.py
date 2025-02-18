import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("800x600+50+50")
root.configure(bg="black")

def update_text(label, texts, index):
    if index < len(texts):
        label.config(text=texts[index])
        root.after(1000, update_text, label, texts, index + 1)
        print(index)
    else:
        label.config(text="Finished processing")

def caculate():
    for ele in root.winfo_children():
        ele.destroy()
    
    txt = ["analyzing data", "performing quality checks", "formatting inputs"]
    spacer = tk.Label(root, bg="black")
    spacer.grid(row=1, column=1, padx=10)
    
    la1 = tk.Label(root, bg="black", fg="white", text="beginning calculations")
    la1.grid(row=3, column=3)
    
    # Start updating the text after a delay
    root.after(1000, update_text, la1, txt, 0)

spacer = tk.Label(root, bg="black")
spacer.grid(row=1, column=1, padx=10)

la1 = tk.Label(root, bg="black", fg="white", text="Think of a number between 1 - 10")
la1.grid(row=2, column=2, padx=10)

la2 = tk.Entry(root, bg="black", fg="white")
la2.grid(row=3, column=2, padx=10)

la3 = tk.Button(root, bg="black", fg="white", text="Submit", command=caculate)
la3.grid(row=4, column=2, padx=10)

root.mainloop()