from tkinter import *
import random 

root=Tk()
root.title("Random countries and their capitals")
root.geometry("400x600")
input_country=Entry(root)
input_capitals=Entry(root)
input_country.place(relx=0.5,rely=0.2,anchor=CENTER)
input_capitals.place(relx=0.5,rely=0.3,anchor=CENTER)
label_country=Label(root)
label_capitals=Label(root)
list_country=[]
list_capitals=[]
def showList():
    country=input_country.get()
    capitals=input_capitals.get()
    list_country.append(country)
    list_capitals.append(capitals)
    label_country["text"]="country name"+str(list_country)
    label_capitals["text"]="capital name"+str(list_capitals)
    
button1=Button(root,text="list of countrys and capitals",command=showList)
button1.place(relx=0.5,rely=0.4,anchor=CENTER)

label_country.place(relx=0.5,rely=0.5,anchor=CENTER)
label_capitals.place(relx=0.5,rely=0.6,anchor=CENTER)
    
root.mainloop()