from tkinter import Tk,Button ,Label,Listbox,Scale,StringVar
from tkinter .filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
import os

root=Tk()
root.title("My Music player")

listofsongs=[]
realname =[]
var=stringvar()
index=0
choice=1
def previous():
    global index
    if(index==0):
        index=len(realnames)-1
    else:
        index=index-1
    pygame.mixer.music.load(listofsong[index])
    pygame.mexer.music.play()
    var.set(realnames[index])
def play():
    global choice
    if(choice==0):
        pygame.mixer.music.unpause()
        choice=1
    else:
        pygame.mixer.music.pause()
        choice=0
def nextsong():
    global index
    if(index==Len(realname)-1):
        index=0
    else:
        index=index+1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    var.set(realnames[index])
def selectsongs():
    directory=Askdirectory()
    os.chdir(directory)
    for files in os.listdir(directore):
        if(files.endswitch(".mp3")):
            realpath=os.path.realpath(files)
            audio=ID3(realpath)
            realname.append(audio["TIT2"].text[0])
            listofsongs.append(files)
    pygame.mixer.init()
    pygame.mixer.music.load(listofsong[1])
    pygame.mixer.music.play()
    pygame.mixer.set_volume(0.5)
    var.set(realname[0])
selectsongs()
songname=Label(root,textvariable=var,font=('impact',25))
slist=Listbox(root,font=('imapct',15))
for i in realnames:
        slip.insert('end',i)
PrevButton=Button(root,text="prev",font=('imapct',15),width=20,height=2,command=previous)
PlayButton=Button(root,text="prev",font=('imapct',15),width=20,height=2,command=play)
NextButton=Button(root,text="prev",font=('imapct',15),width=20,height=2,command=nextsong)
songName.grid(row,column=1,columnspan=4)
slist.grid(row=1,column=0)
prevButton.grid(row=1,column=1)
playButton.grid(row=1,column=2)
nextButton.grid(row=1,column=3)

root.mainloop()





                  
        
