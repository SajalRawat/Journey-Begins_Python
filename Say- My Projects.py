from tkinter import *

import os

root = Tk()

root.geometry("500x500")

root.maxsize(500,500)

root.minsize(500,500)

root.title ("Say")

def tempbindevent(event):

    a= sd.get()

    g = open(( "temp.vbs"), 'w')

    g.write("Dim speaks, speech")

    g.write("\n")

    g.write("speaks =" )

    g.write('''"''')

    g.write(a)

    g.write('''"''')

    g.write("\n")

    g.write('''Set speech=CreateObject("sapi.spvoice")''')

    g.write("\n")

    g.write("speech.Speak speaks")

    g.close()

    cd = "temp.vbs"

    os.system(cd)

    os.remove(cd)

    E.delete(first=0,last=1000)

def temp():

    a= sd.get()

    g = open(( "temp.vbs"), 'w')

    g.write("Dim speaks, speech")

    g.write("\n")

    g.write("speaks =" )

    g.write('''"''')

    g.write(a)

    g.write('''"''')

    g.write("\n")

    g.write('''Set speech=CreateObject("sapi.spvoice")''')

    g.write("\n")

    g.write("speech.Speak speaks")

    g.close()

    cd = "temp.vbs"

    os.system(cd)

    os.remove(cd)

    E.delete(first=0,last=1000)

root.bind('<Return>',tempbindevent)
