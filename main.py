from tkinter import *
import io
import random
import string

YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
PINK = "#FCC8D1"
DARK_PINK="#D14D72"




window = Tk()
window.title("Pasword Menager")
window.geometry("500x500")
window.config(pady=20,padx=20)
window.config(bg=YELLOW)

canvas = Canvas()
lock_img = PhotoImage(file="lock.PNG")
lock_img = lock_img.subsample(5, 5)
canvas.create_image(150,70,image=lock_img)
canvas.grid(row=0, column=2)
canvas.config(bg=YELLOW,highlightthickness=0)
def clear():
    entry_website.delete(0,END)
    entry_username.delete(0,END)
    entry_password.delete(0,END)
def Add():
    global website
    global username
    global password
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()
    if website == "" or username == "" or password == "":
        label_error=Label(window,text="Please fill all the fields")
        label_error.grid(row=6,column=2)
        label_error.config(bg=YELLOW,font=("Courier",15,"bold"))

    else:
        with io.open("Paswords.txt", mode="a", encoding="utf-8") as file:
            file.write( website+" | "+username+" | "+password +"\n")
        label_error = Label(window, text="Success, Password added successfully")
        label_error.grid(row=6, column=2)
        label_error.config(bg=YELLOW, font=("Courier", 15, "bold"))
        clear()



def generate():
    global spinbox
    num = int(spinbox.get())
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=num))
    entry_password.delete(0,END)
    entry_password.insert(0,password)




logo = Label(window,text="Pasword")
logo.grid(row=0,column=1)
logo.config(bg=YELLOW,font=("Courier",20,"bold"))

label_website = Label(window,text="Website")
label_website.grid(row=1,column=1)
label_website.config(bg=YELLOW,font=("Courier",15,"bold"))

entry_website = Entry(window,width=30)
entry_website.focus()
entry_website.grid(row=1,column=2)
entry_website.config(bg=PINK,font=("Courier",15,"bold"),bd=2,highlightbackground=DARK_PINK)



label_username = Label(window,text="Email/Username")
label_username.grid(row=2,column=1)
label_username.config(bg=YELLOW,font=("Courier",15,"bold"),pady=10)

entry_username = Entry(window,width=30)
entry_username.grid(row=2,column=2)
entry_username.config(bg=PINK,font=("Courier",15,"bold"),bd=2,highlightbackground=DARK_PINK)

label_password = Label(window,text="Password")
label_password.grid(row=3,column=1)
label_password.config(bg=YELLOW,font=("Courier",15,"bold"))

entry_password = Entry(window,width=30)
entry_password.grid(row=3,column=2)
entry_password.config(bg=PINK,font=("Courier",15,"bold"),highlightbackground=DARK_PINK)


button_generate = Button(window,text="Generate ",command=generate,bg=YELLOW, bd=0, highlightthickness=0, width=7,
                      height=2,highlightcolor=PINK)
button_generate.grid(row=4,column=2,sticky="w")
button_generate.config(bg=PINK,font=("Courier",15,"bold"))

spinbox = Spinbox(from_=8, to=16, width=5)
spinbox.grid(row=4,column=2,sticky="s")


button_add = Button(window,text="Add",bg=YELLOW,bd=0, highlightthickness=0, width=30,height=1,command=Add)
button_add.grid(row=5,column=2)
button_add.config(font=("Courier",15,"bold"),highlightthickness=0)






















window.mainloop()