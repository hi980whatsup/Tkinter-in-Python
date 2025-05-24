from tkinter import *

window = Tk()

window.title("Sample window")
window.geometry("400x200")


greeting = Label(text="How are you", fg='dark red', bg='light blue')
button =  Button (text="Click me ", bg='pink', fg='black')
entry =  Entry (fg="Green", bg="orange", width=60)
greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()

label = Label(master=frame, text='Sample Frame')
label.pack()

textbox = Text(fg="blue", bg='white')
textbox.pack()

window.mainloop()