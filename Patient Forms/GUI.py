import tkinter
from tkinter import *
class GUI:
    def __init__(self, model):
        self.model = model
        self.window = tkinter.Tk()
        self.window.geometry(f"{1000}x{100}")
        self.topFrame = Frame(self.window)
        self.successFrame = Frame(self.window)
        self.topFrame.pack()
        self.addField()
        self.window.title("Health Records Generator")
        self.makeGraphButton()
        self.bottomFrame = Frame(self.window)
        self.bottomFrame.pack()
        self.response = None
        self.window.mainloop()


    def addField(self):
        self.label = Label(self.topFrame, text="Please Enter Patient Id")
        self.label.pack(side=LEFT)
        self.idEntry = Entry(self.topFrame, width=50)
        self.idEntry.pack(side=LEFT)
        self.idButton = Button(self.topFrame, text="Generate Patient Record", command=self.makeDocument)
        self.idButton.pack(side=RIGHT)

    def makeGraphButton(self):
        self.GraphFrame = Frame(self.window)
        self.GraphFrame.pack()
        self.test = Button(self.GraphFrame, text="All Patients Graph", command=self.plotGraph)
        self.test.pack(side=BOTTOM)

    def plotGraph(self):
        self.model.getAgeToObservation()

    def makeDocument(self):
        self.clearBottomFrame()
        try:
            self.model.makeDocument(self.idEntry.get())
        except ValueError:
            return
        except PermissionError:
            self.errorResponse("File Already in use")
            return
        except Exception as e:
            self.errorResponse(e)
            return
        self.successResponse()

    def errorResponse(self, e):
        self.response = Label(self.bottomFrame, text=str(e))
        self.response.pack(side=BOTTOM)

    def successResponse(self):
        self.response = Label(self.bottomFrame, text="File Generated!")
        self.response.pack(side=BOTTOM)
    def clearBottomFrame(self):
        if self.response is not None:
            self.response.destroy()


