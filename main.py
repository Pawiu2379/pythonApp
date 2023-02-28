import tkinter as tk

window = tk.Tk()

for x in range(3):
    for y in range(3):
        label = tk.Label(window,text=f"Row {x}\n Column {y}",relief=tk.SOLID,borderwidth=1)
        label.grid(row=x,column=y)


label = tk.Label(window,text="this is a span ",relief=tk.RAISED,borderwidth=1)
label.grid(row=3,column=8,columnspan=3)
window.mainloop()
