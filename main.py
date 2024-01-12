import tkinter as tk
from tkinter import messagebox
from gotify import send_gotify_message

def onClick():
    try:
        send_gotify_message(
            entry_title.get(),entry_message.get(),
            entry_url.get(),entry_token.get())
        entry_title.delete(0, tk.END)
        entry_message.delete(0, tk.END)
    except:
        messagebox.showinfo("Alert",
                            "Please, provide correct server-client protocol \
                            (i.e., http), IP address and protocol used by \
                            Gotify server for the URL section, and the correct \
                        token for the last section.")

root = tk.Tk()

frames = []
for i in range(9):
    frame = tk.Frame(
                master=root,
                borderwidth=1
            )
    frame.grid(row=i,padx=5, pady=5)
    frames.append(frame)
[frame_label_title,frame_entry_title,frame_label_message,frame_entry_message,
 frame_label_url,frame_entry_url,frame_label_token,frame_entry_token,
 frame_button] = frames
frame_entry_title.config(relief=tk.SUNKEN)
frame_entry_message.config(relief=tk.SUNKEN)
frame_entry_url.config(relief=tk.SUNKEN)
frame_entry_token.config(relief=tk.SUNKEN)
frame_button.config(relief=tk.RAISED)

button = tk.Button(master=frame_button,text="Send",width=10,command=onClick,
                   font=("Times New Roman", 16, "bold"))
label_title = tk.Label(master=frame_label_title,text="Title:",
                       font=("Times New Roman", 14))
label_message = tk.Label(master=frame_label_message,text="Message:",
                         font=("Times New Roman", 14))
label_url = tk.Label(master=frame_label_url,text="Server URL:",
                       font=("Times New Roman", 14))
label_token = tk.Label(master=frame_label_token,text="Token:",
                         font=("Times New Roman", 14))
entry_title = tk.Entry(master=frame_entry_title,
                       font=("Times New Roman", 14))
entry_message = tk.Entry(master=frame_entry_message,
                         font=("Times New Roman", 14))
entry_url = tk.Entry(master=frame_entry_url,
                       font=("Times New Roman", 14))
entry_token = tk.Entry(master=frame_entry_token,
                         font=("Times New Roman", 14))

label_title.pack()
entry_title.pack()
label_message.pack()
entry_message.pack()
label_url.pack()
entry_url.pack()
label_token.pack()
entry_token.pack()
button.pack()

root.mainloop()
