from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from BusinessLogicLayer.TitleBLL import TitleBLLClass
from Model.UserModel import UserModelClass
class TitleFormClass:
    def titleFormLoad(self,usermodelObject:UserModelClass):

        titleObject = Tk()
        titleObject.geometry('400x500')
        right = int(titleObject.winfo_screenwidth() / 2 - 400 / 2)
        down = int(titleObject.winfo_screenheight() / 2 - 500 / 2)
        titleObject.geometry('+{}+{}'.format(right, down))
        titleObject.title('Employee Form')
        titleObject.resizable(0, 0)

        def registerTitle():
            title_id = txttitle_id.get()
            title = txttitle.get()
            type = txttype.get()
            pub_id = txtpub_id.get()
            price = txtprice.get()
            advance = txtadvance.get()
            royalty = txtroyalty.get()
            ytd_sales = txtytd_sales.get()
            notes = txtnotes.get()
            pub_date = txtpub_date.get()
            titleBLLObject = TitleBLLClass()
            titleBLLObject.registerTitleBLL(title_id, title, type, pub_id, price, advance, royalty, ytd_sales, notes, pub_date)



        def BacktoMain():
            titleObject.destroy()
            from UserInteerfaceLayer.MainForm import MainFormClass
            mainObject = MainFormClass()
            mainObject.MainFormLoad(usermodelObject=usermodelObject)

        lbltitle_id = Label(titleObject, text='title_id : ')
        lbltitle_id.grid(row=0, column=0, pady=10, padx=10, sticky='w')

        txttitle_id = StringVar()
        enttitle_id = ttk.Entry(titleObject, textvariable=txttitle_id, width=40)
        enttitle_id.grid(row=0, column=1, pady=10, padx=10, sticky='w')

        lbltitle = Label(titleObject, text='title : ')
        lbltitle.grid(row=1, column=0, pady=10, padx=10, sticky='w')

        txttitle = StringVar()
        enttitle = ttk.Entry(titleObject, textvariable=txttitle, width=40)
        enttitle.grid(row=1, column=1, pady=10, padx=10, sticky='w')

        lbltype = Label(titleObject, text='type : ')
        lbltype.grid(row=2, column=0, pady=10, padx=10, sticky='w')

        txttype = StringVar()
        cmbtype = ttk.Entry(titleObject, textvariable=txttype, width=40)
        cmbtype.grid(row=2, column=1, pady=10, padx=10, sticky='w')

        lblpub_id = Label(titleObject, text='pub_id : ')
        lblpub_id.grid(row=3, column=0, pady=10, padx=10, sticky='w')

        txtpub_id = StringVar()
        entpub_id = ttk.Entry(titleObject, textvariable=txtpub_id, width=40)
        entpub_id.grid(row=3, column=1, pady=10, padx=10, sticky='w')

        lblprice = Label(titleObject, text='price : ')
        lblprice.grid(row=4, column=0, pady=10, padx=10, sticky='w')

        txtprice = StringVar()
        entprice = ttk.Entry(titleObject, textvariable=txtprice, width=40)
        entprice.grid(row=4, column=1, pady=10, padx=10, sticky='w')

        lbladvance = Label(titleObject, text='advance : ')
        lbladvance.grid(row=5, column=0, pady=10, padx=10, sticky='w')

        txtadvance = StringVar()
        entadvance = ttk.Entry(titleObject, textvariable=txtadvance, width=40)
        entadvance.grid(row=5, column=1, pady=10, padx=10, sticky='w')

        lblroyalty = Label(titleObject, text='royalty : ')
        lblroyalty.grid(row=6, column=0, pady=10, padx=10, sticky='w')

        txtroyalty = StringVar()
        entroyalty = ttk.Entry(titleObject, textvariable=txtroyalty, width=40)
        entroyalty.grid(row=6, column=1, pady=10, padx=10, sticky='w')

        lblytd_sales = Label(titleObject, text='ytd_sales : ')
        lblytd_sales.grid(row=7, column=0, pady=10, padx=10, sticky='w')

        txtytd_sales = StringVar()
        entytd_sales = ttk.Entry(titleObject, textvariable=txtytd_sales, width=40)
        entytd_sales.grid(row=7, column=1, pady=10, padx=10, sticky='w')

        lblnotes = Label(titleObject, text='notes : ')
        lblnotes.grid(row=7, column=0, pady=10, padx=10, sticky='w')

        txtnotes = StringVar()
        entnotes = ttk.Entry(titleObject, textvariable=txtnotes, width=40)
        entnotes.grid(row=7, column=1, pady=10, padx=10, sticky='w')

        lblpub_date = Label(titleObject, text='pub_date : ')
        lblpub_date.grid(row=7, column=0, pady=10, padx=10, sticky='w')

        txtpub_date = StringVar()
        entpub_date = ttk.Entry(titleObject, textvariable=txtpub_date, width=40)
        entpub_date.grid(row=7, column=1, pady=10, padx=10, sticky='w')

        btnRegisterEmployee = Button(titleObject, text='Register Title', width=15, command=registerTitle)
        btnRegisterEmployee.grid(row=8, column=1, pady=20, padx=10, sticky='w')

        btnBacktoMain = Button(titleObject, text='BacktoMain', width=15, command=BacktoMain)
        btnBacktoMain.grid(row=8, column=1, pady=20, padx=10, sticky='e')

        titleObject.mainloop()


