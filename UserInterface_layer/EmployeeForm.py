from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import pyodbc
from tkcalendar import DateEntry
from BusinessLogicLayer.EmployeeBLL import EmployeeBLLClass
from Model.UserModel import UserModelClass
from BusinessLogicLayer.MinitBLL import MinitBLLClass


class EmployeeFormClass:
    def EmployeeFormLoad(self,usermodelObject:UserModelClass):
        EmployeeObject = Tk()
        EmployeeObject.geometry('400x500')
        right = int(EmployeeObject.winfo_screenwidth() / 2 - 400 / 2)
        down = int(EmployeeObject.winfo_screenheight() / 2 - 500 / 2)
        EmployeeObject.geometry('+{}+{}'.format(right, down))
        EmployeeObject.title('Employee Form')
        EmployeeObject.resizable(0, 0)

        def resetForm():
            for widget in EmployeeObject.winfo_children():
                if type(widget) == ttk.Entry or type(widget) == ttk.Combobox:
                    widget.delete(0,END)


        def registerEmployee():
            emp_id = txtemp_id.get()
            firstname = txtFirstname.get()
            minit = txtminit.get()
            lastname = txtlname.get()
            jobid = txtjob_id.get()
            joblvl = txtjob_lvl.get()
            pubid = txtpub_id.get()
            hiredate = txthire_date.get()
            employeeBLLObject = EmployeeBLLClass()
            employeeBLLObject.registerEmployeeBLL(emp_id, firstname, minit, lastname, jobid, joblvl, pubid, hiredate)
            resetForm()



        def BacktoMain():
            EmployeeObject.destroy()
            from UserInteerfaceLayer.MainForm import MainFormClass
            mainObject = MainFormClass()
            mainObject.MainFormLoad(usermodelObject=usermodelObject)


        def checkjoblvl(*args):

            # if len(txtjob_lvl.get()) > 5:
            #     txtjob_lvl.set(txtjob_lvl.get()[: len(txtjob_lvl.get()) - 1])
            if not txtjob_lvl.get().isnumeric():
                txtjob_lvl.set(txtjob_lvl.get()[: len(txtjob_lvl.get()) - 1])
        def checkempid(*args):
            if len(txtemp_id.get()) > 9:
                txtemp_id.set(txtemp_id.get()[: len(txtemp_id.get()) - 1])
        def checkminit(*args):
            for char in txtminit.get():
                txtminit.set(txtminit.get().upper())
            if len(txtminit.get()) > 1:
                txtminit.set(txtminit.get()[: len(txtminit.get()) - 1])
            if txtminit.get().isnumeric():
                txtminit.set(txtminit.get()[: len(txtminit.get()) - 1])
        def checkfname(*args):
            for char in txtFirstname.get():
                if txtFirstname.get().isnumeric():
                    txtFirstname.set(txtFirstname.get()[: len(txtFirstname.get()) - 1])

        lblemp_id = Label(EmployeeObject, text='emp_id : ')
        lblemp_id.grid(row=0, column=0, pady=10, padx=10, sticky='w')

        txtemp_id = StringVar()
        txtemp_id.trace('w',checkempid)
        entemp_id = ttk.Entry(EmployeeObject, textvariable=txtemp_id, width=40)
        entemp_id.grid(row=0, column=1, pady=10, padx=10, sticky='w')

        lblFirstname = Label(EmployeeObject,text='fname : ')
        lblFirstname.grid(row=1,column=0,pady=10,padx=10,sticky='w')

        txtFirstname = StringVar()
        txtFirstname.trace('w',checkfname)
        entFirstname = ttk.Entry(EmployeeObject,textvariable=txtFirstname,width=40)
        entFirstname.grid(row=1,column=1,pady=10,padx=10,sticky='w')

        lblminit = Label(EmployeeObject, text='minit : ')
        lblminit.grid(row=2, column=0, pady=10, padx=10, sticky='w')

        txtminit = StringVar()
        txtminit.trace('w',checkminit)
        minitBLLObject = MinitBLLClass()
        values = []
        for i in minitBLLObject.getallMinnitList():
            values.append(i.Minit)
        cmbMinit = ttk.Combobox(EmployeeObject,values=values,textvariable=txtminit, width=37)
        cmbMinit.grid(row=2, column=1, pady=10, padx=10, sticky='w')

        lbllname = Label(EmployeeObject, text='lname : ')
        lbllname.grid(row=3, column=0, pady=10, padx=10, sticky='w')

        txtlname = StringVar()
        entlname = ttk.Entry(EmployeeObject, textvariable=txtlname, width=40)
        entlname.grid(row=3, column=1, pady=10, padx=10, sticky='w')

        lbljob_id = Label(EmployeeObject, text='job_id : ')
        lbljob_id.grid(row=4, column=0, pady=10, padx=10, sticky='w')

        txtjob_id = StringVar()
        entjob_id = ttk.Entry(EmployeeObject, textvariable=txtjob_id, width=40)
        entjob_id.grid(row=4, column=1, pady=10, padx=10, sticky='w')

        lbljob_lvl = Label(EmployeeObject, text='job_lvl : ')
        lbljob_lvl.grid(row=5, column=0, pady=10, padx=10, sticky='w')

        txtjob_lvl = StringVar()
        txtjob_lvl.trace('w',checkjoblvl)
        entjob_lvl = ttk.Entry(EmployeeObject, textvariable=txtjob_lvl, width=40)
        entjob_lvl.grid(row=5, column=1, pady=10, padx=10, sticky='w')

        lblpub_id = Label(EmployeeObject, text='pub_id : ')
        lblpub_id.grid(row=6, column=0, pady=10, padx=10, sticky='w')

        txtpub_id = StringVar()
        entpub_id = ttk.Entry(EmployeeObject, textvariable=txtpub_id, width=40)
        entpub_id.grid(row=6, column=1, pady=10, padx=10, sticky='w')

        lblhire_date = Label(EmployeeObject, text='hire_date : ')
        lblhire_date.grid(row=7, column=0, pady=10, padx=10, sticky='w')

        txthire_date = StringVar()
        enthire_date = DateEntry(EmployeeObject, textvariable=txthire_date, width=36)
        enthire_date.grid(row=7, column=1, pady=10, padx=10, sticky='w')

        btnRegisterEmployee = Button(EmployeeObject,text = 'Register Employee',width=15,command=registerEmployee)
        btnRegisterEmployee.grid(row=8, column=1 , pady=20, padx=10, sticky='e')

        btnBacktoMain = Button(EmployeeObject, text='BacktoMain', width=15, command=BacktoMain)
        btnBacktoMain.grid(row=8, column=1, pady=20, padx=10, sticky='w')


        EmployeeObject.mainloop()