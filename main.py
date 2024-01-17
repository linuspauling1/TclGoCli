import json
import tkinter as tk
from tkinter import messagebox
from gotify import send_gotify_message

def onClick():
    try:
        file = open("connection.json", "r")
        data = json.load(file)
        url = entry_url.get()
        token = entry_token.get()
        if not url:
            url = data["URL"]
        if not token:
            token = data["Token"]
        try:
            send_gotify_message(
                entry_title.get(),entry_message.get(),
                url,token)
            if entry_url.get():
               data["URL"] = entry_url.get()
            if entry_token.get():
               data["Token"] = entry_token.get()
            entry_title.delete(0, tk.END)
            entry_message.delete(0, tk.END)
            with open("connection.json", "w") as file:
                json.dump(data, file)
        except:
            messagebox.showinfo("Alert",
                                "Please, provide correct server-client protocol \
                                (i.e., http), IP address and protocol used by \
                                Gotify server for the URL section, and the correct \
                            token for the last section.")
    except FileNotFoundError:
        messagebox.showerror('File not found!', 'A new connection.json file \
                             will be created to store the default configuration.')
        data = {"URL":"http://192.168.88.2:90","Token":"AXMOOpzeOEpRMJd"}
        with open("connection.json", "w") as file:
            json.dump(data, file)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

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
