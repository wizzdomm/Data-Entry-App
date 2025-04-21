from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import pyodbc

class SalesFormClass:
    def salesFormLoad(self):
        salesObject = Tk()
        salesObject.geometry('400x500')
        right = int(salesObject.winfo_screenwidth() / 2 - 400 / 2)
        down = int(salesObject.winfo_screenheight() / 2 - 500 / 2)
        salesObject.geometry('+{}+{}'.format(right, down))
        salesObject.title('Employee Form')
        salesObject.resizable(0, 0)

        def registerSales():
            pass
        def BacktoMain():
            salesObject.destroy()
            from UserInteerfaceLayer.MainForm import MainFormClass
            mainObject = MainFormClass()
            mainObject.MainFormLoad('Yashar','Ghaffari')

        lblstor_id = Label(salesObject, text='stor_id : ')
        lblstor_id.grid(row=0, column=0, pady=10, padx=10, sticky='w')

        txtstor_id = StringVar()
        entstor_id = ttk.Entry(salesObject, textvariable=txtstor_id, width=40)
        entstor_id.grid(row=0, column=1, pady=10, padx=10, sticky='w')

        lblord_num = Label(salesObject, text='ord_num : ')
        lblord_num.grid(row=1, column=0, pady=10, padx=10, sticky='w')

        txtord_num = StringVar()
        entord_num = ttk.Entry(salesObject, textvariable=txtord_num, width=40)
        entord_num.grid(row=1, column=1, pady=10, padx=10, sticky='w')

        lblord_date = Label(salesObject, text='ord_date : ')
        lblord_date.grid(row=2, column=0, pady=10, padx=10, sticky='w')

        txtord_date = StringVar()
        cmbord_date = ttk.Entry(salesObject, textvariable=txtord_date, width=40)
        cmbord_date.grid(row=2, column=1, pady=10, padx=10, sticky='w')

        lblqty = Label(salesObject, text='qty : ')
        lblqty.grid(row=3, column=0, pady=10, padx=10, sticky='w')

        txtqty = StringVar()
        entqty = ttk.Entry(salesObject, textvariable=txtqty, width=40)
        entqty.grid(row=3, column=1, pady=10, padx=10, sticky='w')

        lblpayterms = Label(salesObject, text='payterms : ')
        lblpayterms.grid(row=4, column=0, pady=10, padx=10, sticky='w')

        txtpayterms = StringVar()
        entpayterms = ttk.Entry(salesObject, textvariable=txtpayterms, width=40)
        entpayterms.grid(row=4, column=1, pady=10, padx=10, sticky='w')

        lbltitle_id = Label(salesObject, text='title_id : ')
        lbltitle_id.grid(row=5, column=0, pady=10, padx=10, sticky='w')

        txttitle_id = StringVar()
        enttitle_id = ttk.Entry(salesObject, textvariable=txttitle_id, width=40)
        enttitle_id.grid(row=5, column=1, pady=10, padx=10, sticky='w')

        btnRegisterJob = Button(salesObject, text='Register Sale', width=15, command=registerSales)
        btnRegisterJob.grid(row=6, column=1, pady=20, padx=10, sticky='w')

        btnBacktoMain = Button(salesObject, text='BacktoMain', width=15, command=BacktoMain)
        btnBacktoMain.grid(row=6, column=1, pady=20, padx=10, sticky='e')



        salesObject.mainloop()
