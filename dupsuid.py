# you will need tkinter, pyodbc, and base64 if you dont have them already.

from tkinter import *
import pyodbc
import base64, sys

image_string = <insertBase64texthere>

# main window with all needed functions in the class
class Main:

    def __init__(self, master):

# general window configs
        self.master = master
        master.title('DUPSUID Fixer')
        master.geometry('300x250')
        master.configure(bg='gray16')

# custom logo as a label
        self.image = PhotoImage(data=image_string)
        self.label_logo = Label(master)
        self.label_logo.config(image=self.image)
        self.label_logo.pack()

# labels, entry, and button that will display on launch
        self.label_accession = Label(master, text='Accession # : ', bg='gray16', fg='alice blue')
        self.label_accession.pack()

        self.entry_accession = Entry(master, bg='gray32', bd=.5, fg='alice blue')
        self.entry_accession.pack()

        self.button_fixit = Button(master, text='Fix It!', bg='gray20', fg='alice blue', command=self.fixit)
        self.button_fixit.pack()
        
# this label launches after fixit is run
        self.label_success = Label(master, text='Exception now in status UNK', bg='gray16', fg='alice blue')
        self.label_fail = Label(master, text='Failed!!!', bg='gray16', fg='alice blue')


# this function handles the DB update and DB query to confirm the status change
    def fixit(self):
        cnxn = pyodbc.connect("Driver={SQL Server};"
                              "Server=<ip>;"
                              "Database=<db name>;"
                              "uid=<>; pwd=<>")
        cursor = cnxn.cursor()
        cursor.execute(
            'UPDATE [StentorClinical].[dbo].[SwAcquisitionException] SET exceptionTypeCd = ? WHERE accessionNumber = ? AND exceptionTypeCd = ?'
            , 'UNK', str(self.entry_accession.get()), 'DUPSUID')
        cnxn.commit()
        cnxn.close()

        cnxn = pyodbc.connect("Driver={SQL Server};"
                              "Server=<ip>;"
                              "Database=<db name>;"
                              "uid=<>; pwd=<>")
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

# runs the scene/window
root=Tk()
main_scene = Main(root)
root.mainloop()
