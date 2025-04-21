from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import pyodbc
from BusinessLogicLayer.PublisherBLL import PublisherBLLClass
from Model.UserModel import UserModelClass
class PublisherFormclass:
    def PublisherFormLoad(self,usermodelObject:UserModelClass):
        PublisherObject = Tk()
        PublisherObject.geometry('400x500')
        right = int(PublisherObject.winfo_screenwidth() / 2 - 400 / 2)
        down = int(PublisherObject.winfo_screenheight() / 2 - 500 / 2)
        PublisherObject.geometry('+{}+{}'.format(right, down))
        PublisherObject.title('Employee Form')
        PublisherObject.resizable(0, 0)

        def registerPublisher():
            pub_id = txtpub_id.get()
            pub_name = txtpub_name.get()
            city = txtcity.get()
            state = txtstate.get()
            country = txtcountry.get()
            publisherBLLObject = PublisherBLLClass()
            publisherBLLObject.registerPublisher(pub_id,pub_name,city,state,country)

        def BacktoMain():
            PublisherObject.destroy()
            from UserInteerfaceLayer.MainForm import MainFormClass
            mainObject = MainFormClass()
            mainObject.MainFormLoad(usermodelObject=usermodelObject)

        lblpub_id = Label(PublisherObject, text='pub_id : ')
        lblpub_id.grid(row=0, column=0, pady=10, padx=10, sticky='w')

        txtpub_id = StringVar()
        entpub_id = ttk.Entry(PublisherObject, textvariable=txtpub_id, width=40)
        entpub_id.grid(row=0, column=1, pady=10, padx=10, sticky='w')

        lblpub_name = Label(PublisherObject, text='pub_name : ')
        lblpub_name.grid(row=1, column=0, pady=10, padx=10, sticky='w')

        txtpub_name = StringVar()
        entpub_name = ttk.Entry(PublisherObject, textvariable=txtpub_name, width=40)
        entpub_name.grid(row=1, column=1, pady=10, padx=10, sticky='w')

        lblcity = Label(PublisherObject, text='city : ')
        lblcity.grid(row=2, column=0, pady=10, padx=10, sticky='w')

        txtcity = StringVar()
        cmbcity = ttk.Entry(PublisherObject, textvariable=txtcity, width=40)
        cmbcity.grid(row=2, column=1, pady=10, padx=10, sticky='w')

        lblstate = Label(PublisherObject, text='state : ')
        lblstate.grid(row=3, column=0, pady=10, padx=10, sticky='w')

        txtstate = StringVar()
        entstate = ttk.Entry(PublisherObject, textvariable=txtstate, width=40)
        entstate.grid(row=3, column=1, pady=10, padx=10, sticky='w')

        lblcountry = Label(PublisherObject, text='country : ')
        lblcountry.grid(row=4, column=0, pady=10, padx=10, sticky='w')

        txtcountry = StringVar()
        entcountry = ttk.Entry(PublisherObject, textvariable=txtcountry, width=40)
        entcountry.grid(row=4, column=1, pady=10, padx=10, sticky='w')

        btnRegisterPublisher = Button(PublisherObject, text='Register Publisher', width=15, command=registerPublisher)
        btnRegisterPublisher.grid(row=5, column=1, pady=20, padx=10, sticky='w')

        btnBacktoMain = Button(PublisherObject, text='BacktoMain', width=15, command=BacktoMain)
        btnBacktoMain.grid(row=5, column=1, pady=20, padx=10, sticky='e')


        PublisherObject.mainloop()
