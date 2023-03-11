from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.grid()
        self.celsuis= StringVar()
        self.farheneit = StringVar()

        self.createWidgets()

    def createWidgets(self):
        self.labelName =Label(self,text="Enter the temparature in celsius :")
        self.labelName.grid(row=0,column=0)

        self.entryName = Entry(self,textvariable=self.celsuis)
        self.entryName.grid(row=0,column=1)

        self.submit= Button(self)
        self.submit['text'] = 'convert'
        self.submit['command'] = self.convertTemp
        self.submit.grid(row=0,column=2)

        self.labelName2 =Label(self,text="The temparature in Farheneit :")
        self.labelName2.grid(row=1,column=0)

        self.entryName2 = Entry(self,text=self.farheneit.get())
        #self.entryName2["text"] = self.farheneit.get()
        self.entryName2.grid(row=1,column=1)


    def convertTemp(self):
        convert = (9/5) * int(self.celsuis.get()) + 32
        self.farheneit= convert
        return convert



rootWindow = Tk()
rootWindow.title("GUI Application Demo")
rootWindow.geometry("300x300")  
app= Application(master = rootWindow)
app.mainloop()