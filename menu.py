import os
import tkinter
import customtkinter
from customtkinter import *

#Framework
win = CTk(fg_color="black")
win.title("MenuUI v1.0")
win.geometry("300x600")
win.resizable(False,False)
#win.maxsize(height=1000,width=1600)
#win.minsize(height=500,width=800)

#icon and images

win.iconbitmap(r'logo.ico')

#scroll

frame = customtkinter.CTkFrame(master=win,
                               width=800,
                               height=800,
                               corner_radius=10)
                               
frame.pack(padx=20, pady=20)

#tk_textbox = tkinter.Text(frame, highlightthickness=0)
#tk_textbox.grid(row=0, column=0, sticky=NSEW)

#ctk_textbox_scrollbar = customtkinter.CTkScrollbar(frame, command=tk_textbox.yview)
#ctk_textbox_scrollbar.grid(row=0, column=1, sticky="ns")

#main

switch_var_1 = customtkinter.StringVar(value="on")
switch_var_2 = customtkinter.StringVar(value="off")

def switch_event():
    pass

switch_1 = customtkinter.CTkSwitch(master=frame, text="Godmode", command=switch_event,
                                   variable=switch_var_1, onvalue="on", offvalue="off")

switch_1.pack(padx=20,pady=10)

switch_var_3 = customtkinter.StringVar(value="on")
switch_var_4 = customtkinter.StringVar(value="off")

switch_2 = customtkinter.CTkSwitch(master=frame, text="Invisible", command=switch_event,
                                   variable=switch_var_3, onvalue="on", offvalue="off")

switch_2.pack(padx=20,pady=10)

switch_var_5 = customtkinter.StringVar(value="on")
switch_var_6 = customtkinter.StringVar(value="off")

switch_2 = customtkinter.CTkSwitch(master=frame, text="Fly", command=switch_event,
                                   variable=switch_var_5, onvalue="on", offvalue="off")

switch_2.pack(padx=20,pady=10)


#loop
win.mainloop()
