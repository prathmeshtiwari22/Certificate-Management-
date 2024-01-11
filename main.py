from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
def login():
    if usernameEntry.get()=='' or PasswordEntry.get()=='':
        messagebox.showerror("Error",'Fields cannot be Empty')
    elif usernameEntry.get()=='Paras' and PasswordEntry.get()=='2044':
        messagebox.showinfo('Success','Welcome')
        import scratch_1

    else:
        messagebox.showerror("Error","Entry Correct Details")






root=Tk()
root.geometry("1280x700+0+0")
root.resizable(False,False)
backgroundimage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(root,image=backgroundimage)
bgLabel.place(x=0,y=0)


loginFrame=Frame(root)
loginFrame.place(x=400,y=150)

logoImage=PhotoImage(file='logo.png')
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)

usernameImage=PhotoImage(file="user.png")
usernameLabel=Label(loginFrame,image= usernameImage,text='Username',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)


usernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='black')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

PasswordImage=PhotoImage(file="password.png")
PasswordLabel=Label(loginFrame,image= PasswordImage,text='Password',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
PasswordLabel.grid(row=2,column=0,pady=10,padx=20)


PasswordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='black')
PasswordEntry.grid(row=2,column=1,pady=10,padx=20)


loginButton=Button(loginFrame,text='Login',font=('times new roman',14,'bold'),width=15
                   ,fg='white',bg='cornflowerblue',activebackground='cornflowerblue',
                   activeforeground='white',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)


root.mainloop()

