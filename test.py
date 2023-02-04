import tkinter
from tkinter import *
from tkinter import messagebox
import new


def Auto_renew():
    if USERNAME.get() == '' or PASSWORD.get() == '':
        messagebox.showerror(
            "Required Fields", "Please include all fields")
        return
    username = USERNAME.get()
    password = PASSWORD.get()
    url = "http://117.239.204.229:8380/opac/myaccount/myAccount.html"

    new.startbot(username, password, url)


def Reset():
    USERNAME.set('')
    PASSWORD.set('')


app = Tk()

# Username
USERNAME = StringVar()
userlabel = Label(app, text='Username: ', font=('bold', 14))
userlabel.grid(row=0, column=0, sticky=W, padx=(220, 0), pady=(150, 0))
userentry = Entry(app, textvariable=USERNAME)
userentry.grid(row=0, column=1, pady=(150, 0))

# Password
PASSWORD = StringVar()
passlabel = Label(app, text='Password: ', font=('bold', 14))
passlabel.grid(row=1, column=0, sticky=W, padx=(220, 0))
passentry = Entry(app, textvariable=PASSWORD,show='*')
passentry.grid(row=1, column=1)

# Autorenew Button
autorenew = Button(app, text='Auto Renew', width=12, command=Auto_renew)
autorenew.grid(row=2, column=0, pady=20, padx=(200, 0))

reset_button = Button(app, text='Reset', width=12, command=Reset)
reset_button.grid(row=2, column=1, pady=20)

app.title('AutoRenew')
app.geometry('700x350')

app.mainloop()
