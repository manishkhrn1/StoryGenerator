from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.grid()
        self.nameVar = StringVar()
        self.gender = StringVar()

        self.createWidgets()

    def createWidgets(self):

        #create a label
        self.name_label= Label(self,text= "Your First name")
        self.name_label["bg"] = 'blue'
        self.name_label['fg']= 'white'
        self.name_label.grid(row = 0 , column=0)

        #Create an entry
        self.name_entry = Entry(self,textvariable=self.nameVar)
        self.name_entry.grid(row=0,column=1)

        #Create a button
        self.submit = Button(self)
        self.submit["text"] = 'submit'
        self.submit["command"]= self.submitName
        self.submit.grid(row=0,column=2)

        #Create a radio button
        self.male_female_choice = Radiobutton(self,text='M')
        self.male_female_choice["variable"]= self.gender
        self.male_female_choice["value"] = 'male'
        self.male_female_choice.grid(row=1,column=1)

        self.male_female_choice = Radiobutton(self,text='F')
        self.male_female_choice["variable"]= self.gender
        self.male_female_choice["value"] = 'Female'
        self.male_female_choice.grid(row=1,column=2)

        self.hi_btn = Button(self)
        self.hi_btn['text'] = "Hew \n wassup"
        self.hi_btn['command']=self.say_hi
        self.hi_btn.grid(row=2,column=2)

    def say_hi(self):

        gender=self.gender.get()
        myName = self.nameVar.get()
        self.information = messagebox.showinfo(title = "Check it" , message = "Name of the person is " + myName + "\n" + "gender : " + gender)

    def submitName(self):
        name = self.nameVar.get()
        print("The name is : " + name)


rootWindow = Tk()
rootWindow.title("GUI Application Demo")
rootWindow.geometry("300x200")  
app= Application(master = rootWindow)
app.mainloop()