from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import pyodbc
from BusinessLogicLayer.AuthorBLL import AuthorBLLClass
from Model.UserModel import UserModelClass
class AuthorFormClass:
    def AuthorFormLoad(self,usermodelObject:UserModelClass):
        AuthorObject = Tk()
        AuthorObject.geometry('400x500')
        right = int(AuthorObject.winfo_screenwidth() / 2 - 400 / 2)
        down = int(AuthorObject.winfo_screenheight() / 2 - 500 / 2)
        AuthorObject.geometry('+{}+{}'.format(right, down))
        AuthorObject.title('Employee Form')
        AuthorObject.resizable(0, 0)

        def resetForm():
            for widget in AuthorObject.winfo_children():
                if type(widget) == ttk.Entry or type(widget) == ttk.Combobox:
                    widget.delete(0,END)

        def registerAuthor():

            au_id = txtau_id.get()
            lastname = txtau_lname.get()
            firstname = txtau_fname.get()
            phone = txtphone.get()
            address = txtaddress.get()
            city = txtcity.get()
            state = txtState.get()
            zip = txtzip.get()
            contract = txtcontract.get()
            AuthorBLLObject = AuthorBLLClass()
            AuthorBLLObject.registerAuthorBLL(au_id, lastname, firstname, phone, address, city, state, zip, contract)
            resetForm()
        def BacktoMain():
            AuthorObject.destroy()
            from UserInteerfaceLayer.MainForm import MainFormClass
            mainObject = MainFormClass()
            mainObject.MainFormLoad(usermodelObject=usermodelObject)
        lblau_id = Label(AuthorObject, text='au_id : ')
        lblau_id.grid(row=0, column=0, pady=10, padx=10, sticky='w')

        txtau_id = StringVar()
        entau_id = ttk.Entry(AuthorObject, textvariable=txtau_id, width=40)
        entau_id.grid(row=0, column=1, pady=10, padx=10, sticky='w')

        lblau_lname = Label(AuthorObject, text='Lastname : ')
        lblau_lname.grid(row=1, column=0, pady=10, padx=10, sticky='w')

        txtau_lname = StringVar()
        entau_lname = ttk.Entry(AuthorObject, textvariable=txtau_lname, width=40)
        entau_lname.grid(row=1, column=1, pady=10, padx=10, sticky='w')

        lblau_fname = Label(AuthorObject, text='Firstname : ')
        lblau_fname.grid(row=2, column=0, pady=10, padx=10, sticky='w')

        txtau_fname = StringVar()
        cmbau_fname = ttk.Entry(AuthorObject, textvariable=txtau_fname, width=40)
        cmbau_fname.grid(row=2, column=1, pady=10, padx=10, sticky='w')

        lblphone = Label(AuthorObject, text='phone : ')
        lblphone.grid(row=3, column=0, pady=10, padx=10, sticky='w')

        txtphone = StringVar()
        entphone = ttk.Entry(AuthorObject, textvariable=txtphone, width=40)
        entphone.grid(row=3, column=1, pady=10, padx=10, sticky='w')

        lbladdress = Label(AuthorObject, text='address : ')
        lbladdress.grid(row=4, column=0, pady=10, padx=10, sticky='w')

        txtaddress = StringVar()
        entaddress = ttk.Entry(AuthorObject, textvariable=txtaddress, width=40)
        entaddress.grid(row=4, column=1, pady=10, padx=10, sticky='w')

        lblcity = Label(AuthorObject, text='city : ')
        lblcity.grid(row=5, column=0, pady=10, padx=10, sticky='w')

        txtcity = StringVar()
        entcity = ttk.Entry(AuthorObject, textvariable=txtcity, width=40)
        entcity.grid(row=5, column=1, pady=10, padx=10, sticky='w')

        lblzip = Label(AuthorObject, text='zip : ')
        lblzip.grid(row=6, column=0, pady=10, padx=10, sticky='w')

        txtzip = StringVar()
        entzip = ttk.Entry(AuthorObject, textvariable=txtzip, width=40)
        entzip.grid(row=6, column=1, pady=10, padx=10, sticky='w')

        lblcontract = Label(AuthorObject, text='contract : ')
        lblcontract.grid(row=7, column=0, pady=10, padx=10, sticky='w')

        txtcontract = StringVar()
        entcontract = ttk.Entry(AuthorObject, textvariable=txtcontract, width=40)
        entcontract.grid(row=7, column=1, pady=10, padx=10, sticky='w')

        lblState = Label(AuthorObject, text='State : ')
        lblState.grid(row=8, column=0, pady=10, padx=10, sticky='w')

        txtState = StringVar()
        entState = ttk.Entry(AuthorObject, textvariable=txtState, width=40)
        entState.grid(row=8, column=1, pady=10, padx=10, sticky='w')

        btnRegisterAuthor = Button(AuthorObject, text='Register Author', width=15, command=registerAuthor)
        btnRegisterAuthor.grid(row=9, column=1, pady=20, padx=10, sticky='w')

        btnBacktoMain = Button(AuthorObject, text='BacktoMain', width=15, command=BacktoMain)
        btnBacktoMain.grid(row=9, column=1, pady=20, padx=10, sticky='e')

        AuthorObject.mainloop()