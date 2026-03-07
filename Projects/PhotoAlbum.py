import tkinter as tk
import time 
from PIL import Image ,ImageTk

#  Main 
root=tk.Tk()
root.title("PhotoAlbum")
root.geometry("500x500")
# list of image path 
imagePath=[
    r"C:\Users\Acer\OneDrive\Pictures\Pictures\PHOTOS\20220324_171057.jpg",
    r"C:\Users\Acer\OneDrive\Pictures\Pictures\PHOTOS\20220419_195036.jpg",
    r"C:\Users\Acer\OneDrive\Pictures\Pictures\PHOTOS\20220927_180313.jpg"
]
image=[]
imageSize=(700,700)
for path in imagePath:
    img=Image.open(path)
    img=img.resize(imageSize)
    image.append(img)
# creating  tkinter compatible image using PIL image
finalImage=[]
for i in image:
    photo=ImageTk.PhotoImage(i)
    finalImage.append(photo)

# label widget 
imageLabel=tk.Label(root)
imageLabel.pack(pady=30)

# Slideshow function
def startSlideshow():
    for i in finalImage:
        imageLabel.config(image=i)
        imageLabel.image=i
        root.update()
        time.sleep(3)

# button
def stopSlideshow():
    global running
    running = False

startBtn = tk.Button(root, text="Start", command=startSlideshow)
startBtn.pack(pady=10)

stopBtn = tk.Button(root, text="Stop", command=stopSlideshow)
stopBtn.pack(pady=10)
root.mainloop() #to keep the window open 


 

