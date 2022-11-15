from PyPDF2 import PdfWriter, PdfReader,PdfMerger
from tkinter import *

#Have problem with some pdf

def Pagine_da_salvare():
    print(entrybox.get(),entrybox2.get(),entrybox3.get())
    StartPath = entrybox.get()
    EndPath = entrybox4.get()

    pages_to_keep = []  # page numbering starts from 0
    startpage= int(entrybox2.get())-1
    endpage = int(entrybox3.get())
    for i in range(startpage,endpage):
        pages_to_keep.append(i)
    infile = PdfReader(StartPath, 'rb')
    output = PdfWriter()
    try:
        for i in pages_to_keep:
            p = infile.pages[i]
            output.add_page(p)
    except:
        pass
    with open(EndPath, 'wb') as f:
        output.write(f)
    pass

def Unisci():
    def Unire():
        primo= firstpathentry.get()
        secondo= secondpathentry.get()
        infile1=PdfReader(primo,'rb')
        infile2=PdfReader(secondo,'rb')
        merger=PdfMerger()

        merger.append(infile1)
        merger.append(infile2)
        with open(primo, 'wb') as f:
            merger.write(f)
        pass

    root2=Tk()

    firstpathlabel = Label(root2, text="Primo file")
    firstpathlabel.grid(row=0, column=0)
    secondpathlabel = Label(root2, text="Secondo file")
    secondpathlabel.grid(row=1, column=0)
    firstpathentry = Entry(root2)
    firstpathentry.grid(row=0,column=1)
    secondpathentry = Entry(root2)
    secondpathentry.grid(row=1, column=1)
    procede = Button(root2,text='Procedi',command=Unire)
    procede.grid(row=2,column=1)

    root2.mainloop()
    pass

root = Tk()

root.geometry("900x700")

Elimapagine = Frame(root)
menubar= Menu(Elimapagine)
menubar.add_command(label='PDF Join',command=Unisci)


labelentrybox= Label(Elimapagine,text='Inserisci file')
labelentrybox.grid(column=0,row=0)
entrybox= Entry(Elimapagine)
entrybox.grid(column=1,row=0,columnspan=2)
labelentrybox2= Label(Elimapagine,text="Pagina iniziale")
labelentrybox2.grid(column=0,row=1)
entrybox2= Entry(Elimapagine)
entrybox2.grid(column=1,row=1)
labelentrybox3= Label(Elimapagine,text="Pagina Finale")
labelentrybox3.grid(column=0,row=2)
entrybox3= Entry(Elimapagine)
entrybox3.grid(column=1,row=2)
labelentrybox4= Label(Elimapagine,text="Dove Salvare")
labelentrybox4.grid(column=0,row=3)
entrybox4= Entry(Elimapagine)
entrybox4.grid(column=1,row=3)
button1 = Button(Elimapagine,text='Esegui',command=Pagine_da_salvare)
button1.grid(column=1,row=4)
Elimapagine.pack()


root.config(menu=menubar)
root.mainloop()

