import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip
import os
import subprocess

def convert_to_mp3():
    video_file = filedialog.askopenfilename(filetypes=[("MP4 Files", "*.mp4")])
    
    if video_file:
        audio_file = os.path.splitext(video_file)[0] + ".mp3"
        
        try:
            clip = VideoFileClip(video_file)
            clip.audio.write_audiofile(audio_file)
            label_status.config(text="Conversion successful !")
            convert_to_mp3()
        except Exception as e:
            label_status.config(text=f"Error : {e}")
    else:
        label_status.config(text="No file selected.")

fenetre = tk.Tk()
fenetre.title("MP4 to MP3 converter")

label_instruction = tk.Label(fenetre, text="Select a MP4 file to convert to MP3")
label_instruction.pack(pady=10)

btn_convertir = tk.Button(fenetre, text="Select and convert", command=convert_to_mp3)
btn_convertir.pack(pady=10)

label_status = tk.Label(fenetre, text="")
label_status.pack(pady=10)

fenetre.mainloop()