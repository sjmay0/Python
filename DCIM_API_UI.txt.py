from tkinter import *
from tkinter.scrolledtext import ScrolledText
import os
entwin=Tk()#creates a window object called entwin
entwin.geometry("425x490")#sets entwin size
entwin.configure(bg="deepskyblue")#sets entwin background colour

entwin.columnconfigure(1,weight=5)
entwin.columnconfigure(0,weight=2)
entwin.columnconfigure(2,weight=2)
entwin.rowconfigure(0,weight=0)
entwin.rowconfigure(1,weight=0)
entwin.rowconfigure(2,weight=8)
entwin.rowconfigure(3,weight=0)
def passdata(usrinput):
    global output
    output=usrinput
    print(output)
    entwin.destroy()

title = Label(entwin,text="Please Enter Device names you wish to see below\nNOTE: Put a comma between each device name")#creates a label called titleel with the text defined in the speach marks
title.grid(row=0,columnspan=3,sticky="NSEW", pady = 2)#positions title to the first row, second column
title.config(bg="deepskyblue",fg="white")#makes the background of the text black and the foreground (text) white

inputbox=ScrolledText(entwin,height=25, width=50)#sets the dimensions of the inputbox which is used for data entry
inputbox.grid(row=2,column=1,sticky="NSEW",pady = 2)#sets the position

entrybutton=Button(entwin, text="Commit", command=lambda: passdata(inputbox.get("1.0","end-1c"))) #creates a button called entrybutton, sets it height and width, says what text goes in it then links it to the function passdata
entrybutton.grid(row=3,column=1,sticky="NSEW", pady = 2)#positions the button.
mainloop()#loops the previous window continuously so it doesnt just run once and then close straight away.






outwin=Tk()#creates a window object called entwin
outwin.geometry("450x490")#sets entwin size
outwin.configure(bg="deepskyblue")#sets entwin background colour
title = Label(outwin,text="Requested Servers")#creates a label called titleel with the text defined in the speach marks
title.grid(row=0,columnspan=3,sticky="NSEW", pady = 2)#positions title to the first row, second column
title.config(bg="deepskyblue",fg="white")#makes the background of the text black and the foreground (text) white

outputbox=ScrolledText(outwin,height=25, width=50)
outputbox.grid(row=1,column=1,sticky="NSEW",pady = 2)

filetitle = Label(outwin,text="If you would like to save this in a file enter the name below:")#creates a label called titleel with the text defined in the speach marks
filetitle.grid(row=2,columnspan=3,sticky="NSEW", pady = 2)#positions title to the first row, second column
filetitle.config(bg="deepskyblue",fg="white")#makes the background of the text black and the foreground (text) white

filenameinput=Text(outwin,height=1, width=5)
filenameinput.grid(row=3,column=1,sticky="NSEW",pady = 2)

outwin.columnconfigure(1,weight=5)
outwin.columnconfigure(0,weight=2)
outwin.columnconfigure(2,weight=2)
outwin.rowconfigure(0,weight=0)
outwin.rowconfigure(1,weight=8)
outwin.rowconfigure(2,weight=0)
outwin.rowconfigure(3,weight=0)

#seperates out each one on , then lists them in the input box made above
output=output.split(",")
for eachoutput in output:
    outputbox.insert(END,eachoutput)
    outputbox.insert(END,"\n")

###creates a function that is passed the filename they requested
def makefile(filename):
    print(filename)
    print(outputbox.get("1.0","end-1c"))
    filename.strip()
    if filename=="":
        filename="DIVA_SERVER_NAMES.txt"
        with open(filename,"a") as filehandle:
            filehandle.write(outputbox.get("1.0","end-1c"))
    elif filename.lower()[-4:]==".txt":
        with open(filename,"a") as filehandle:
            filehandle.write(outputbox.get("1.0","end-1c"))       
    else:
        filename=filename+".txt"
        with open(filename,"a") as filehandle:
            filehandle.write(outputbox.get("1.0","end-1c"))
    outwin.destroy()

makefilebutton=Button(outwin, text="Commit", command=lambda: makefile(filenameinput.get("1.0","end-1c"))) #creates a button called entrybutton, sets it height and width, says what text goes in it then links it to the function passdata
makefilebutton.grid(row=4,column=1,sticky="NSEW", pady = 2)#positions the button.
mainloop()

