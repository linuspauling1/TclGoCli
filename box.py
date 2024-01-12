import tkinter as tk
from gotify import send_gotify_message

def onClick():
    send_gotify_message(entry_title.get(),entry_message.get())
    entry_title.delete(0, tk.END)
    entry_message.delete(0, tk.END)

root = tk.Tk()

frames = []
for i in range(5):
    frame = tk.Frame(
                master=root,
                relief=tk.RAISED,
                borderwidth=1
            )
    frame.grid(row=i,padx=5, pady=5)
    frames.append(frame)
[frame_label_title,frame_entry_title,frame_label_message,frame_entry_message,frame_button] = frames
frame_label_title.config(relief=tk.FLAT)
frame_label_message.config(relief=tk.FLAT)
frame_entry_title.config(relief=tk.SUNKEN)
frame_entry_message.config(relief=tk.SUNKEN)

button = tk.Button(master=frame_button,text="Send",width=10,command=onClick,
                   font=("Times New Roman", 16, "bold"))
label_title = tk.Label(master=frame_label_title,text="Title:",
                       font=("Times New Roman", 14))
label_message = tk.Label(master=frame_label_message,text="Message:",
                         font=("Times New Roman", 14))
entry_title = tk.Entry(master=frame_entry_title,
                       font=("Times New Roman", 14))
entry_message = tk.Entry(master=frame_entry_message,
                         font=("Times New Roman", 14))

label_title.pack()
entry_title.pack()
label_message.pack()
entry_message.pack()
button.pack()

root.mainloop()
