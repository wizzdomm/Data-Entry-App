from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import pyodbc
from datetime import date
from datetime import datetime
from UserInteerfaceLayer.EmployeeForm import EmployeeFormClass
from UserInteerfaceLayer.AuthorForm import AuthorFormClass
from UserInteerfaceLayer.PublisherForm import PublisherFormclass
from UserInteerfaceLayer.TitleForm import TitleFormClass
from UserInteerfaceLayer.JobForm import JobFormClass
from UserInteerfaceLayer.SalesForm import SalesFormClass
from Model.UserModel import UserModelClass

class MainFormClass:

    def MainFormLoad(self,usermodelObject: UserModelClass):

        MainObject = Tk()
        MainObject.geometry('500x500')
        right = int(MainObject.winfo_screenwidth() / 2 - 500 / 2)
        down = int(MainObject.winfo_screenheight() / 2 - 500 / 2)
        MainObject.geometry('+{}+{}'.format(right, down))
        MainObject.title('Main Form')
        MainObject.resizable(0, 0)
        MainObject.iconbitmap('Temp/MainObject.ico')
        MainObject.configure(bg="#473587")

        canvas = Canvas(
            MainObject,
            bg="#473587",
            height=600,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)

        canvas.create_text(
            450, 10,
            text=date.today().strftime("%Y-%m-%d"),
            fill="#f3f5eb",
            font=("Arial Black", int(10.0), "bold"))



        def RegisterEmployee():
            MainObject.destroy()
            employeeObject = EmployeeFormClass()
            employeeObject.EmployeeFormLoad(usermodelObject=usermodelObject)
        def registerAuthor():
            MainObject.destroy()
            authorobject = AuthorFormClass()
            authorobject.AuthorFormLoad(usermodelObject=usermodelObject)

        def registerPublisher():
            MainObject.destroy()
            publisherObject = PublisherFormclass()
            publisherObject.PublisherFormLoad(usermodelObject=usermodelObject)
        def registerTitle():
            MainObject.destroy()
            titleObject = TitleFormClass()
            titleObject.titleFormLoad(usermodelObject=usermodelObject)
        def registerJob():
            MainObject.destroy()
            jobObject = JobFormClass()
            jobObject.jobFormLoad()
        def registerSales():
            MainObject.destroy()
            salesObject = SalesFormClass()
            salesObject.salesFormLoad()
        def switchUser():
            MainObject.destroy()
            from LoginFile import LoginObject
            LoginObject.LoginFormLoad()






        lblWelcome = ttk.Label(MainObject, text=f'welcome {usermodelObject.Firstname} {usermodelObject.Lastname}')
        # lblWelcome.grid(row=1, column=1, padx=10, pady=10, sticky='w')
        lblWelcome.place(x=20,y= 10)

        registerEmployeePhoto = PhotoImage(file='Temp/RegisterEmployee.png')
        btnRegister = Button(MainObject,text='Register Employee',width=120,height=120,image=registerEmployeePhoto,compound=TOP,command=RegisterEmployee)
        # btnRegister.grid(row=2,column=1,padx=10,pady=10,sticky='w')
        btnRegister.place(x=20,y=40)

        registerAuthorPhoto = PhotoImage(file='Temp/Author.png')
        btnRegisterAuthor = Button(MainObject,text='Register Author',width=120,height=120,image=registerAuthorPhoto,compound=TOP,command=registerAuthor)
        btnRegisterAuthor.place(x=160,y=40)

        registerPublisherPhoto = PhotoImage(file='Temp/Publisher.png')
        btnRegisterPublisher = Button(MainObject,text='Register Publisher',width=120,height=120,image=registerPublisherPhoto,compound=TOP,command=registerPublisher)
        btnRegisterPublisher.place(x = 300,y=40)

        registerTitlePhoto = PhotoImage(file='Temp/Title.png')
        btnRegisterTitle = Button(MainObject,text='Regisster Title',width=120,height=120,image= registerTitlePhoto,compound=TOP,command=registerTitle)
        btnRegisterTitle.place(x=20,y=190)

        registerJobPhoto = PhotoImage(file='Temp/Job.png')
        btnRegisterJob = Button(MainObject,text='Regisster Job',width=120,height=120,image= registerJobPhoto,compound=TOP,command=registerJob)
        btnRegisterJob.place(x=160,y=190)

        registerSalesPhoto = PhotoImage(file='Temp/Sales.png')
        btnRegisterJob = Button(MainObject,text='Regisster Sales',width=120,height=120,image= registerSalesPhoto,compound=TOP,command=registerSales)
        btnRegisterJob.place(x=300,y=190)

        switchUserPhoto = PhotoImage(file='Temp/switchUser.png')
        btnSwitchUser = Button(MainObject,text='Switch User',width=120,height=120,image=switchUserPhoto,compound=TOP,command=switchUser)
        btnSwitchUser.place(x=160,y=340)

        MainObject.mainloop()