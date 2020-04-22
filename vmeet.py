from tkinter import *
from bin import client

def cleanup(*frames):
    for frame in frames:
        for w in frame.winfo_children():
            w.destroy()

def meeting_view(root,display,reply,*args,**kwargs):
    root.title("VMEET")
    root.minsize(960,640)
    root.maxsize(960,640)
    cleanup(display,reply)

    display["height"] = 600
    display["width"] = 960
    display["bg"] = "#224"

    reply["height"] = 40
    reply["width"] = 960
    reply["bg"] = "#222"

def connect_meeting(meeting_number,meeting_pin):
    # validation 
    if len(meeting_number)!= 12 or len(meeting_pin)!= 6: print("not valid")
    else:
        pass

def login_view(root,display,reply,*args,**kwargs):
    root.title("login")
    root.minsize(960,640)
    root.maxsize(960,640)
    cleanup(display,reply)

    display["height"] = 640
    display["width"] = 960
    display["bg"] = "#224"

    print("login")

    meeting_number_label = Label(display,text="Meeting No.:",font=("Arial",12,"bold"),bg="#224",fg="#fff")
    meeting_number = Entry(display,font=("Arial",12,"bold"))
    meeting_number_label.pack(side=TOP,pady=(150,2),padx=425)
    meeting_number.pack(side=TOP,ipady=7,ipadx=7,pady=(0,10),padx=350)
    meeting_pin_label = Label(display,text="PIN:",font=("Arial",12,"bold"),bg="#224",fg="#fff")
    meeting_pin = Entry(display,font=("Arial",12,"bold"))
    meeting_pin_label.pack(side=TOP,pady=(20,2),padx=420)
    meeting_pin.pack(side=TOP,ipady=7,ipadx=7,pady=(0,10),padx=300)
    connectbutton = Button(display,text="Connect",font=("Arial",12,"bold"),width=20,height=2,bg="#0af",bd=0,fg="#fff",command= lambda: connect_meeting(meeting_number.get(),meeting_pin.get()))
    connectbutton.pack(side=TOP,pady=(60,200),padx=350)
root = Tk()

header = Frame(root)
header.pack(side=TOP)

footer = Frame(root)
footer.pack(side=TOP)

login_view(root,header,footer)

root.mainloop()