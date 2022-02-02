from msilib.schema import File
from tkinter import *
from io import open
from tkinter import filedialog as Filedialog
root = Tk()
root.title("Blog de notas")
root.geometry("900x700")
menubar = Menu()
root.config(menu=menubar)
archivemenu = Menu(menubar,tearoff=0)
text = Text(root,font="Consolas",width=900,height=700)
def saved():
    text2 = Tk()
    text2.title("Archivo")
    text2.geometry("300x100")
    Label(text2,text="Escriba el nombre del archivo").pack()
    entry = Entry(text2,font="Consolas")
    def create_txt():
        entryr = str(entry.get())
        file = open(f"{entryr}.txt","w")
        textr = str(text.get(1.0,"end"))
        file.write(textr)
        file.close()
    def create_py():
        entryr = str(entry.get())
        file = open(f"{entryr}.py","w")
        textr = str(text.get(1.0,"end"))
        file.write(textr)
        file.close()
    entry.pack()
    Button(text2,text="Guardar en texto",command=create_txt).pack()
    Button(text2,text="Guardar en python",command=create_py).pack()
    text2.mainloop()
archive = None
def load():
    global archive
    archive = Filedialog.askopenfilename(initialdir="C:/",filetypes=(("Archivos de texto","*.txt"),("Archivos de python","*.py"),),title="Archivo")
    file = open(archive,"r")
    text_usert = file.readlines()
    root.title(f"{archive} Blog de notas")
    text.insert('end',"".join(text_usert))
def actual_overwrite():
    textr = text.get(1.0,"end")
    file = open(archive,"w")
    file.write(textr)
    file.close()
def select_overwrite():
    archive2 = Filedialog.askopenfilenames(filetypes=(("Archivos de texto","*.txt"),("Archivos de python","*.py"),),title="Archivo")
    textr = text.get(1.0,"end")
    file = open("".join(archive2),"w")
    file.write(textr)
    file.close()
archivemenu.add_command(label="Guardar",command=saved)
archivemenu.add_command(label="Cargar",command=load)
archivemenu.add_command(label="Sobrescribir Archivo Actual",command=actual_overwrite)
archivemenu.add_command(label="Sobrescribir Un Archivo Selecionado",command=select_overwrite)
menubar.add_cascade(label="Archivo",menu=archivemenu)
text.place(y=0,x=0)
root.mainloop()