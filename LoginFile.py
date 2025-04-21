from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import pyodbc
from UserInteerfaceLayer.MainForm import MainFormClass
LoginObject = Tk()
from PIL import ImageTk, Image
from Model.UserModel import UserModelClass

LoginObject.geometry('500x500')
LoginObject.iconbitmap('Temp/image.ico')
right = int(LoginObject.winfo_screenwidth() / 2 - 500/2)
down = int(LoginObject.winfo_screenheight() / 2 - 500/2)
LoginObject.geometry('+{}+{}'.format(right,down))
LoginObject.title('Login Form')
LoginObject.resizable(0,0)
LoginObject.configure(bg='#ffffff')
canvas = Canvas(LoginObject,bg="#ffffff",height=500,width=542,bd=0,highlightthickness=0,relief="ridge")
canvas.place(x=0, y=0)
background_img = PhotoImage(file=f"Temp/Login2.png")
background = canvas.create_image(250,220,image=background_img)


def checkLogin():
    username = txtusername.get()
    password = txtpassword.get()
    params = (username,password)


    sqlcommand = 'EXEC	 [dbo].[CheckLogin] ?, ?'
    sqlserverConnectionString = 'Driver={SQL Server};Server=(local);database=pubs;Trusted_Connection=yes'
    sqlconnection = pyodbc.connect(sqlserverConnectionString)
    cursor_SQL=sqlconnection.cursor()
    cursor_SQL.execute(sqlcommand,params)
    rows = cursor_SQL.fetchall()
    if len(rows) > 0:
        LoginObject.destroy()
        # msg.showinfo('Welcome',f'Welcome {rows[0][3]}{rows[0][4]}')
        mainFormObject = MainFormClass()
        userModelObjecgt = UserModelClass(firstname=rows[0][3],lastname=rows[0][4],username=txtusername.get(),passwoord=txtpassword.get(),isadmin=rows[0][5])
        mainFormObject.MainFormLoad(usermodelObject=userModelObjecgt)

    else:
        msg.showerror('Error','Invalid Username or Password')
# lblUsername = Label(LoginObject,text= 'Username: ')
# # lblUsername.grid(row=1,column=0,padx=10,pady=10,sticky='w')
# lblUsername.place(x=100,y= 300,width=100,height=20)

txtusername = StringVar()
entUsername = ttk.Entry(LoginObject,width=40,textvariable=txtusername)
# entUsername.grid(row=1,column= 1,padx=10,pady=10,sticky='e')
entUsername.place(x=120,y= 203,width=360,height=80)

# lblPassword = Label(LoginObject,text='Password: ')
# lblPassword.grid(row=1,column=0,padx=10,pady=10,sticky='w')
#
txtpassword = StringVar()
entPassword = ttk.Entry(LoginObject,width=40,show='*',textvariable=txtpassword)
# entPassword.grid(row=1,column= 1,pady=10,padx=10,sticky='e')
entPassword.place(x=120,y= 302.5,width=360,height=80)

# btnLogin = ttk.Button(LoginObject,text='',width=15,command=checkLogin)
# btnLogin.grid(row=2,column=1,padx=10,pady=10,sticky='e')
btnLoginImage = PhotoImage(file = f"Temp/btnlogin.png")
btnLogin = Button(image=btnLoginImage,borderwidth=0,highlightthickness=0,command=checkLogin,relief="flat",bg="#ffffff")
btnLogin.place(x=30,y= 403,width=453,height=83)

LoginObject.mainloop()

