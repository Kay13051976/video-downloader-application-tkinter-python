from tkinter import *
from pytube import YouTube
from moviepy.editor import *

def download():
    #fletch URL
    video_path=link.get()
    mp4=YouTube(video_path).streams.get_highest_resolution().download()
    video_clip=VideoFileClip(mp4)
    video_clip.close()


#application page
root=Tk()
root.title("Youtube Downloader")
canvas=Canvas(root,width=400,height=200)
canvas.pack()

#program name
app_title=Label(root,text="Youtube Downloader",font=('Arial',20,'bold'))
canvas.create_window(200,30,window=app_title)

#link/download button
label=Label(root,text="URL")
canvas.create_window(200,80,window=label)

link=Entry(root,width=35)
canvas.create_window(200,100,window=link)
downloadBtn=Button(text="Download",command=download)
canvas.create_window(200,150,window=downloadBtn)


root.mainloop()
