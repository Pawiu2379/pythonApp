import tkinter as tk

window = tk.Tk()
frame = tk.Frame(background='black')
frame.pack(side=tk.TOP)

w = tk.Label(frame, text='label in frame')
w.pack(pady=5,padx=5)
window.mainloop()
