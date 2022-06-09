from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.video.io.VideoFileClip import VideoFileClip
from pytube import YouTube
import shutil

# Fonksiyonlar 

def dosya_secme():
    path = filedialog.askdirectory()
    path_label.config(text=path)


def dosya_indirme():
    get_link= link_field.get()
    user_path = path_label.cget("text")

    screen.title('İndiriliyor...')

    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    # indirme bildirimi
    shutil.move(mp4_video,user_path)

    screen.title('İndirme Tamamlandı')




screen = Tk()
title = screen.title('Youtube Download')
canvas= Canvas(screen, width=800, height=700)
canvas.pack()

# logo ekleme
logo_img = PhotoImage(file='YT_1201.png')
iconImg = PhotoImage(file='Youtube.png')
screen.iconphoto(False,iconImg)
# Ölçeklendirme
logo_img = logo_img.subsample(4,4)
canvas.create_image(400,150, image=logo_img)

# Link Yükleme Alanı
link_field = Entry(screen, width=50)
link_label = Label(screen, text="İndirilecek Video Link: ", font=('Times',14))

# Video yükleme yeri seçimi
path_label = Label(screen, text="İndirme Yapılacak Yer: ",font=('Times',14))
secme_btn = Button(screen, text="Dosya Seç", command=dosya_secme)

# Video Yükleme Alanının Ekrana İşlenmesi
canvas.create_window(300,350, window=path_label)
canvas.create_window(425,400, window=secme_btn)

# link Alanının Ekrana İşlenmesi
canvas.create_window(300,300, window=link_label)
canvas.create_window(400,300, window=link_field)

# İndirme Butonları
indirme_btn = Button(screen, text="Video İndir", command=dosya_indirme)

# Canvas Ekleme
canvas.create_window(525,400, window=indirme_btn)

screen.mainloop()