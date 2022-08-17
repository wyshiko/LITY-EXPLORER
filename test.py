from tkinter import *
from unittest import result
import tkinter as tk 
from PIL import Image, ImageTk 

id = "admin"
mdp = "admin"

def show_frame(frame):
    frame.tkraise()
root = tk.Tk()
root.configure(background='black')
root.geometry("975x540")
root.title("Login")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame_logger = tk.Frame(root)
frame_1 = tk.Frame(root)

for frame in (frame_logger, frame_1):
    frame.grid(row=0,column=0,sticky='nsew')


# logger code    ################################    

Label(frame_logger, text = 'LOGIN', 
      font =('Verdana', 15)).pack(side = TOP, pady = 10)


entry_id = Entry(frame_logger, width=50)
entry_id.pack()

entry_mdp = Entry(frame_logger, show="*", width=50)
entry_mdp.pack()


def logger():
    error = 0
    enter_id = entry_id.get()
    enter_mdp = entry_mdp.get()

    if enter_id!=id or enter_mdp != mdp :
        error = 1
        print("Votre identifiant ou votre mot de passe est incorrect")
        result = "Votre identifiant ou votre mot de passe est incorrect"
        myLabel = Label(frame_logger, text=result).pack()
        
    elif error == 0 :
        print("Welcome " + str(id) +".")
        show_frame(frame_1)
        
Button(frame_logger, text="Loggin", command=logger).pack()

# Frame 1 code    ################################
Label(frame_1, text = 'WELCOME ' + str(id), 
      font =('Verdana', 15)).pack(side = TOP, pady = 10)
# button
frame_1_btn = tk.Button(frame_1, text='Enter', command=lambda:show_frame(frame_logger))
frame_1_btn.pack()

show_frame(frame_logger)

root.mainloop()