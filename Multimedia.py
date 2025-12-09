from tkinter import *
import webbrowser

root = Tk()
root.title("Mohamed Hamdy")
root.geometry("290x350")


def Googal():
    webbrowser.open(r"http://www.google.com")
    
def YouTube():
    webbrowser.open(r"https://www.youtube.com/")

def Facebook():
    webbrowser.open(r"https://www.facebook.com/?locale=ar_AR")

def instagram():
    webbrowser.open(r"https://www.instagram.com/")


# This is Buttons for open Googal
my_button1 = Button(
    root,
    text="Googal",
    command=Googal,
    width=10,
    height=2,
    bg="white",
    fg="black",
    font=50,
)
# This is Buttons for open YouTube
my_button2 = Button(
    root,
    text="YouTube",
    command=YouTube,
    width=10,
    height=2,
    bg="white",
    fg="red",
    font=50,
)
# This is Buttons for open Facebook
my_button3 = Button(
    root,
    text="Facebook",
    command=Facebook,
    width=10,
    height=2,
    bg="white",
    fg="blue",
    font=50,
)
# This is Buttons for open instagram
my_button4 = Button(
    root,
    text="instagram",
    command=instagram,
    width=10,
    height=2,
    bg="white",
    fg="orange",
    font=50,
)

my_button1.grid(column=1, row=1)
my_button2.grid(column=1, row=2)
my_button3.grid(column=2, row=1)
my_button4.grid(column=2, row=2)
root.mainloop()