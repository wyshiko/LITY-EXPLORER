from PIL import Image, ImageTk 
import  tkinter as tk 
root = tk.Tk() 

image = Image.open("IMG_7428.jpeg") 
photo = ImageTk.PhotoImage(image) 
 
canvas = tk.Canvas(root, width = image.size[0], height = image.size[1]) 
canvas.create_image(0,0, anchor = tk.NW, image=photo)
canvas.pack() 
root.mainloop()