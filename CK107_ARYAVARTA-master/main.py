from tkinter import *
import captureData
import dataTraing
import identifyPerson
import tkinter.messagebox as tmsg
from tkinter import simpledialog


def alert():
    value = tmsg.askquestion("Alert", "Do You want to add new person")
    if value == 'yes':
        userName = simpledialog.askstring("user name", "Enter Your Name")
        print(userName)
        captureData.dataCollect(userName)


root = Tk()
root.title("Dynamic Human Recognition")
root.geometry("1080x640")
root.minsize(1080, 640)
root.maxsize(1080, 640)

f1 = Frame(root, bg="grey", borderwidth=1, relief=SUNKEN)
f1.pack(fill=BOTH)

l1 = Label(f1, text="Person Identification", font="Helvetica 18 bold", fg="white", bg="grey")
l1.pack(side=TOP, ipadx=30)

f2 = Frame(root, bg="grey", borderwidth=1, relief=GROOVE)
f2.pack(side=RIGHT, fill="y", ipadx=50)

register = Button(f2, text="Register", font="Helvetica 15 bold", width=10, border=10, command=alert)
register.pack(pady=50)

train = Button(f2, text="Train", font="Helvetica 15 bold", width=10, border=10, command=dataTraing.dataTrain)
train.pack(pady=50)

detect = Button(f2, text="Identify", font="Helvetica 15 bold", width=10, border=10,
                command=identifyPerson.identification)
detect.pack(pady=50)

C = Canvas(root, bg="blue", width=830)

C.pack(side=LEFT, fill=BOTH)

# f3 = Frame(root, bg="grey", borderwidth=1, relief=GROOVE)
# f3.pack(side=LEFT, fill='y')
# l3 = Label(f3, text="hello", font="Helvetica 50 bold", fg="white", bg="grey", width=10, height=10)
# l3.grid(row=1, column=0,)
# l3.pack()

root.mainloop()
