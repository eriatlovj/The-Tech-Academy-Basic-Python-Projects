from tkinter import *
from tkinter import Tk
from tkinter import filedialog
import os

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width= False, height= False)
        self.master.geometry('{}x{}'.format(400, 200))
        self.master.title('Check Files')
        self.master.config(bg='beige')

        self.varInputFile = StringVar()

        self.lblFile = Label(self.master, text='File: ', font=("Arial", 12), fg='black', bg='beige')
        self.lblFile.grid(row=0, column=0, padx=(30, 0), pady=(40, 0))

        self.txtInputTop = Entry(self.master,text = self.varInputFile, font=("Arial", 14), fg ='black', bg= 'white' )
        self.txtInputTop.grid(row =0 ,column = 1, padx =(30,0), pady=(50,0), columnspan=6 )

        self.btnCheckFiles = Button(self.master, text = "Browse Files...", width= 10, height = 2, command = self.Browse)
        self.btnCheckFiles.grid(row =2 ,column = 0, padx =(30,0), pady=(10,0), sticky= S+W)

        self.btnClose = Button(self.master, text="Cancel", width=10, height=2, command = self.close)
        self.btnClose.grid(row=2, column=6, padx=(0,0), pady=(10,0), sticky=E)

    def close(self):
        self.master.destroy()

    def Browse (self):
        dir= filedialog.askdirectory()
        self.varInputFile.set(dir)
        print(dir)

if __name__ == "__main__":
    root = Tk()
    app = ParentWindow(root)
    root.mainloop()
