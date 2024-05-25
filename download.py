from tkinter import *
from tkinter import filedialog, messagebox
from pytube import YouTube
import shutil

# Fonksiyonlar

def dosya_secme():
    path = filedialog.askdirectory()
    path_label.config(text=path)


def dosya_indirme():
    get_link= link_field.get()
    user_path = path_label.cget("text")
    resolution = resolution_var.get()

    screen.title('İndiriliyor...')

    try:
        yt = YouTube(get_link)
        if resolution == 'Highest':
            mp4_video = yt.streams.get_highest_resolution().download()
        else:
            stream = yt.streams.filter(res=resolution, progressive=True).first()
            if stream is None:
                messagebox.showwarning('Resolution Error', f'{resolution} resolution is not available. Downloading highest resolution instead.')
                mp4_video = yt.streams.get_highest_resolution().download()
            else:
                mp4_video = stream.download()

        # indirme bildirimi
        shutil.move(mp4_video, user_path)
        screen.title('İndirme Tamamlandı')
    except Exception as e:
        messagebox.showerror('Error', f'An error occurred: {e}')


screen = Tk()
title = screen.title('Youtube Download')
canvas = Canvas(screen, width=800, height=400)
canvas.pack()

# logo ekleme
logo_img = PhotoImage(file='images/YT_1201.png')
iconImg = PhotoImage(file='images/Youtube.png')
screen.iconphoto(False,iconImg)

logo_img = logo_img.subsample(4,4)
canvas.create_image(400, 200, image=logo_img)
# Link Yükleme Alanı
link_frame = Frame(screen)
link_frame.pack(pady=10)

link_label = Label(link_frame, text="İndirilecek Video Link: ", font=('Times',14))
link_field = Entry(link_frame, width=50)

link_label.pack(side='left', padx=5)
link_field.pack(side='left', padx=5)

# Video yükleme yeri seçimi
path_frame = Frame(screen)
path_frame.pack(pady=10)

path_label = Label(path_frame, text="İndirme Yapılacak Yer: ",font=('Times',14))
secme_btn = Button(path_frame, text="Dosya Seç", command=dosya_secme)

path_label.pack(side='left', padx=5)
secme_btn.pack(side='left', padx=5)

# Video Kalitesi Seçimi
resolution_frame = Frame(screen)
resolution_frame.pack(pady=10)

resolution_label = Label(resolution_frame, text="Video Kalitesi: ", font=('Times',14))
resolution_var = StringVar(value='Highest')
resolutions = ['Highest', '144p', '240p', '360p', '480p', '720p', '1080p']
resolution_menu = OptionMenu(resolution_frame, resolution_var, *resolutions)

resolution_label.pack(side='left', padx=5)
resolution_menu.pack(side='left', padx=5)

# İndirme Butonları
indirme_btn = Button(screen, text="Video İndir", command=dosya_indirme)
indirme_btn.pack(pady=20)

screen.mainloop()
