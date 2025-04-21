from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import pyodbc

class JobFormClass:
    def jobFormLoad(self):
        jobObject = Tk()
        jobObject.geometry('400x500')
        right = int(jobObject.winfo_screenwidth() / 2 - 400 / 2)
        down = int(jobObject.winfo_screenheight() / 2 - 500 / 2)
        jobObject.geometry('+{}+{}'.format(right, down))
        jobObject.title('Employee Form')
        jobObject.resizable(0, 0)

        def registerJob():
            pass
        def BacktoMain():
            jobObject.destroy()
            from UserInteerfaceLayer.MainForm import MainFormClass
            mainObject = MainFormClass()
            mainObject.MainFormLoad('Yashar','Ghaffari')

        lbljob_id = Label(jobObject, text='title_id : ')
        lbljob_id.grid(row=0, column=0, pady=10, padx=10, sticky='w')

        txtjob_id = StringVar()
        entjob_id = ttk.Entry(jobObject, textvariable=txtjob_id, width=40)
        entjob_id.grid(row=0, column=1, pady=10, padx=10, sticky='w')

        lbljob_desc = Label(jobObject, text='job_desc : ')
        lbljob_desc.grid(row=1, column=0, pady=10, padx=10, sticky='w')

        txtjob_desc = StringVar()
        entjob_desc = ttk.Entry(jobObject, textvariable=txtjob_desc, width=40)
        entjob_desc.grid(row=1, column=1, pady=10, padx=10, sticky='w')

        lblminLvl = Label(jobObject, text='minLvl : ')
        lblminLvl.grid(row=2, column=0, pady=10, padx=10, sticky='w')

        txtminLvl = StringVar()
        cmbminLvl = ttk.Entry(jobObject, textvariable=txtminLvl, width=40)
        cmbminLvl.grid(row=2, column=1, pady=10, padx=10, sticky='w')

        lblmaxLvl = Label(jobObject, text='maxLvl : ')
        lblmaxLvl.grid(row=3, column=0, pady=10, padx=10, sticky='w')

        txtmaxLvl = StringVar()
        entmaxLvl = ttk.Entry(jobObject, textvariable=txtmaxLvl, width=40)
        entmaxLvl.grid(row=3, column=1, pady=10, padx=10, sticky='w')

        btnRegisterJob = Button(jobObject, text='Register Job', width=15, command=registerJob)
        btnRegisterJob.grid(row=4, column=1, pady=20, padx=10, sticky='w')

        btnBacktoMain = Button(jobObject, text='BacktoMain', width=15, command=BacktoMain)
        btnBacktoMain.grid(row=4, column=1, pady=20, padx=10, sticky='e')

        jobObject.mainloop()