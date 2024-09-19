from tkinter import *                                  # * : untuk mengaktifkan seluruh perintah dalam tkinter
from tkinter import filedialog                       # filedialog = membantu untuk membuka folder tujuan kita
from PIL import Image, ImageTk              # untuk menambahkan gambar di tkinter (PIL = Python Imaging Library)  
from pygame import mixer                           # Mixer = untuk memutar lagu, menghentikan lagu      
import os                                                   # OS(Operating System) = digunakan ketika akan bekerja dengan file
 
mixer.init()                                                  # Untuk mempersiapkan modul mixer sebelum digunakan 

# Lembar Tkinter
main = Tk()                                                 # Untuk memunculkan layar tkinter
main.geometry('407x450')                            # Mengatur ukuran layar tkinter (lebar x tinggi)
main.title("Sepotipai Premium")                      # Memberi judul lembar tkinter

# Background Tkinter
image = Image.open("Sepotipai cover.png")            # File gambar harus dlm format png
resize_image = image.resize((403,600))               # Mengubah ukuran gambar (lebar x tinggi)
img = ImageTk.PhotoImage(resize_image)
Label(main, image = img).place(x = 0, y=0)

# Layar Musik
music_frame = Frame(main, bd = 2, relief = 'ridge')                       # bd = border
music_frame.place(x = 110, y = 180, width = 270, height = 165)

# Untuk Scroll ke bawah
scroll = Scrollbar(music_frame)
play_list = Listbox(music_frame, width = 50, yscrollcommand = scroll.set, bg = 'black', fg = 'white')
scroll.config(command = play_list.yview)
scroll.pack(side = RIGHT, fill = Y)
play_list.pack(side = LEFT)

def open_folder():                                           # Fungsi untuk membuka folder
    path = filedialog.askdirectory()                    # untuk memilih folder tujuan yang kita inginkan
    if (path):
        os.chdir(path)                                        # chdir(change directory) = mengubah alamat tujuan
        songs = os.listdir(path)                           # listdir = untuk memperoleh list dari semua file pada alamat tujuan                            
        for song in songs:
            if song.endswith(".mp3") :                   # Kalo format lagu berakhiran "mp3' = otomatis terinsert
                play_list.insert(END, song)              # Lagu baru yang ditambahkan selalu dimunculkan di akhir 
                
def play_song() :
    mixer.music.load(play_list.get(ACTIVE))          
    mixer.music.play()
    
def set_volume(vol):                                 
    mixer.music.set_volume(int(vol)/100)
    
# Tombol Tkinter
Button(main, text = 'PLAY', width = 9, command = play_song, bg = 'black', fg = 'white').place(x = 30, y = 180)
Button(main, text = 'STOP', width = 9, command = mixer.music.stop, bg = 'black', fg = 'white').place(x = 30, y = 215)
Button(main, text = 'PAUSE', width = 9, command = mixer.music.pause, bg = 'black', fg = 'white').place(x = 30, y = 250)
Button(main, text = 'UNPAUSE', width = 9, command = mixer.music.unpause, bg = 'black', fg = 'white').place(x = 30, y = 285)
Button(main, text = 'OPEN', width = 9, command = open_folder, bg = 'black', fg = 'white').place(x = 30, y = 320)

# Mengatur Volume Suara
volume = Scale(main, from_ = 0, to = 100, length = 270, orient = HORIZONTAL, command = set_volume, bg = 'black', fg = 'white')
volume.set(50)
volume.place(x = 110, y = 355)
    
main.mainloop() 
