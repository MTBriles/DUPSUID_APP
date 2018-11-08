# app screen

from tkinter import *
import pyodbc
import base64, sys
# from myimages import image_string

# data = open(sys.argv[0], 'rb').read()

image_string = b'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'


class Main:

    def __init__(self, master):


        self.master = master
        master.title('DUPSUID Fixer')
        master.geometry('300x250')
        master.configure(bg='gray16')


        # self.logo = PhotoImage(file='CPPACSlogo.gif')
        self.image = PhotoImage(data=image_string)
        self.label_logo = Label(master)
        self.label_logo.config(image=self.image)
        self.label_logo.pack()


        self.label_accession = Label(master, text='Accession # : ', bg='gray16', fg='alice blue')
        self.label_accession.pack()

        self.entry_accession = Entry(master, bg='gray32', bd=.5, fg='alice blue')
        self.entry_accession.pack()

        self.button_fixit = Button(master, text='Fix It!', bg='gray20', fg='alice blue', command=self.fixit)
        self.button_fixit.pack()

        self.label_success = Label(master, text='Exception now in status UNK', bg='gray16', fg='alice blue')
        self.label_fail = Label(master, text='Failed!!!', bg='gray16', fg='alice blue')



    def fixit(self):
        cnxn = pyodbc.connect("Driver={SQL Server};"
                              "Server=10.232.233.17;"
                              "Database=StentorClinical;"
                              "uid=sa; pwd=st3nt0r")
        cursor = cnxn.cursor()
        cursor.execute(
            'UPDATE [StentorClinical].[dbo].[SwAcquisitionException] SET exceptionTypeCd = ? WHERE accessionNumber = ? AND exceptionTypeCd = ?'
            , 'UNK', str(self.entry_accession.get()), 'DUPSUID')
        cnxn.commit()
        cnxn.close()

        cnxn = pyodbc.connect("Driver={SQL Server};"
                              "Server=10.232.233.17;"
                              "Database=StentorClinical;"
                              "uid=sa; pwd=st3nt0r")
        cursor = cnxn.cursor()
        cursor.execute('SELECT exceptionTypeCd, accessionNumber FROM [StentorClinical].[dbo].[SwAcquisitionException]with(nolock) WHERE accessionNumber = ?'
          , str(self.entry_accession.get()))
        self.rows = cursor.fetchall()
        for self.row in self.rows:
            print(self.row)


        if self.row[0] == 'UNK':
            self.label_success.pack()
        elif self.row[0] != 'UNK':
           self.label_fail.pack()

        cnxn.close()


root=Tk()
main_scene = Main(root)
root.mainloop()
