import socket
from  threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

IP_ADDRESS = '127.0.0.1'
PORT = 5500
BUFFER_SIZE = 8050
SERVER = None

def musicWindow():
    window=Tk()
    window.title('Music Window')
    window.geometry("300x300")
    window.configure(bg='LightSkyBlue')

    selectLabel = Label(window, text = "Select song", bg = 'LightSkyBlue', font = ("Calibri", 8))
    selectLabel.place(x= 2, y=1)

    listbox = Listbox(window, height=10, width=39, activestyle='dotbox', bg="LightSkyBlue", font = ('Calibri',10))
    listbox.place(x=10, y=17)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight=1, relx = 1)
    scrollbar1.config(command=listbox.yview)

    playButton = Button(window, text="Play", width = 10, bd=1, bg="SkyBlue", font=("Calibri", 10))
    playButton.place(x=30, y=200)

    stop = Button(window, text="Stop", width = 10, bd=1, bg="SkyBlue", font=("Calibri", 10))
    stop.place(x=200, y=200)
    
    upload = Button(window, text="Upload", width = 10, bd=1, bg="SkyBlue", font=("Calibri", 10))
    upload.place(x=30, y=250)
    
    download = Button(window, text="Download", width = 10, bd=1, bg="SkyBlue", font=("Calibri", 10))
    download.place(x=200, y=250)

    info_label = Label(window, text="", fg="blue", font=("Calibri",8))
    info_label.place(x=4, y=200)

    window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
   
    musicWindow()

setup()