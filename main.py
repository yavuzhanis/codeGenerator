# öncelikle qrcode pillow versiyonunu indirdik => Görüntü için
# ? import the modules
import qrcode
import PIL
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# TODO DEFİNE FUNCTIONS


def createQR(*args):
    data = text_entry.get()
    if data:
        img = qrcode.make(data)
        resized_img = img.resize((280, 250))
        tkimage = ImageTk.PhotoImage(resized_img)
        qr_canvas.delete('all')
        qr_canvas.create_image(0, 0, anchor=tk.NW, image=tkimage)
        qr_canvas.image = tkimage
    else:
        messagebox.showwarning('Başarısız','Qr Code Yüklenmedi')

def saveQR(*args):
    data = text_entry.get()
    if data:
        img = qrcode.make(data)
        resized_img = img.resize((280, 250))
        path = filedialog.asksaveasfilename(defaultextension='.png')
        if path:
            resized_img.save(path)
            messagebox.showinfo('Başarılı','Qr Code Yüklendi')
        else:
            messagebox.showwarning('Başarısız','Qr Code Yüklenmedi')


#! GUI code
root = tk.Tk()

root.title('Qr Code Generator')
root.geometry('600x800')  # 450 width, 550 height
root.config(bg='green')  # ? Arka Plan Rengi
  # Yneiden boyutlandırma

frame1 = tk.Frame(root, bd=2, relief=tk.RAISED)
frame1.place(x=10, y=0, width=500, height=400)

frame2 = tk.Frame(root, bd=2, relief=tk.SUNKEN)
frame2.place(x=10, y=260, width=400, height=100)

image = Image.open('barkod.png')
# Resmi ekrana sığacak boyuta ölçekleyin
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
image = image.resize((width, height), Image.ANTIALIAS)
cover_img = ImageTk.PhotoImage(image)

qr_canvas = tk.Canvas(frame1)
qr_canvas.create_image(0, 0, anchor = tk.NW, image = cover_img)
qr_canvas.image = cover_img
qr_canvas.bind('<Double-1>', saveQR)
qr_canvas.pack(fill=tk.BOTH)

text_entry = ttk.Entry(frame2 , width=26, font=('Sitka Small', 12), justify=tk.CENTER)
text_entry.bind('<Return>', createQR)
text_entry.place(x=100, y=15)

btn_1 = ttk.Button(frame2, text='Create', width=10 , command=createQR)
btn_1.place(x=35, y=50)


btn_2 = ttk.Button(frame2, text='Save', width=10, command=saveQR)
btn_2.place(x=135, y=50)

btn_3 = ttk.Button(frame2, text="Exit", width=10 , command=root.quit)
btn_3.place(x=235, y=50)


root.mainloop()
