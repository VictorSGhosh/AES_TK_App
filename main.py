import os
import sys
from functools import partial
from tkinter import ttk

from aes import AES
from tkinter import *
from tkinter.filedialog import askopenfilename, askopenfile

if __name__ == '__main__':
    key = "DSA_CS512_Project"
    inp_text = "My name is Victor and I am a student at Rutgers University, New Brunswick."
    file_path = ""

    def reseeet():
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def submit():
        global inp
        global inp_text
        global key
        global keyinp
        global app
        inp_text = inp.get()
        key = keyinp.get()
        app.destroy()

    def efileinp():
        global inp
        global inp_text
        global key
        global keyinp
        global file_path
        global app
        inp_text = ""
        app.withdraw()
        file_path = askopenfilename(title="Select file", filetypes=(("Text files", ".txt"),))
        filetxt = open(file_path, 'r')
        aa=filetxt.readlines()
        for a in aa:
            inp_text += a
        key = keyinp.get()
        app.destroy()

    def dfileinp():
        global inp
        global inp_text
        global key
        global keyinp
        global file_path
        global app
        inp_text = ""
        app.withdraw()
        file_path = askopenfilename(title="Select file", filetypes=(("Text files", ".txt"),),initialdir=os.getcwd())
        filetxt = open(file_path, 'rb')
        aa = filetxt.readlines()
        for a in aa:
            inp_text += a.decode("utf-8")
        key = keyinp.get()
        app.destroy()

    def encrypt():
        global app
        global keyinp
        global inp
        global frame2
        global frame1
        frame1.destroy()
        frame2.destroy()
        frame3.destroy()
        frame = Frame(app)
        app.geometry("700x150")
        inp = Entry(app)
        keyinp = Entry(app)
        app.title('encrypt')
        text_label = ttk.Label(text="Text")
        text_label.pack(fill='x', expand=True)
        inp.insert(0, "My name is Victor and I am a student at Rutgers University, New Brunswick.")
        inp.pack(fill='x', expand=True)
        inp.focus_set()
        key_label = ttk.Label(text="Key")
        key_label.pack(fill='x', expand=True)
        keyinp.insert(0, "DSA_CS512_Project")
        keyinp.pack(fill='x', expand=True)

        Button(app, text='Submit', command=submit).pack(side='bottom')
        Button(app, text='Input File', command=efileinp).pack(side='bottom')
        app.mainloop()
        aes = AES()
        cipher = aes.encrypt(inp_text, key)
        exiter = Tk()
        exiter.title("Encrypted Text")
        text_label = ttk.Label(text=cipher)
        text_label.pack(fill='x', expand=True)
        Button(exiter, text="End", command=reseeet).pack(side="bottom")
        exiter.mainloop()

        print(cipher)

    def decrypt():
        global app
        global keyinp
        global inp
        global frame2
        global frame1
        frame1.destroy()
        frame2.destroy()
        frame3.destroy()
        app.geometry("700x150")
        inp = Entry(app)
        keyinp = Entry(app)
        app.title('decrypt')
        text_label = ttk.Label(text="Text")
        text_label.pack(fill='x', expand=True)
        inp.insert(0, "My name is Victor and I am a student at Rutgers University, New Brunswick.")
        inp.pack(fill='x', expand=True)
        inp.focus_set()
        key_label = ttk.Label(text="Key")
        key_label.pack(fill='x', expand=True)
        keyinp.insert(0, "DSA_CS512_Project")
        keyinp.pack(fill='x', expand=True)

        Button(app, text='Submit', command=submit).pack(side='bottom')
        Button(app, text='Input File', command=dfileinp).pack(side='bottom')
        app.mainloop()
        aes = AES()
        out_text = aes.decrypt(inp_text, key)
        exiter=Tk()
        exiter.title("Decrypted Text")
        text_label = ttk.Label(text=out_text)
        text_label.pack(fill='x', expand=True)
        Button(exiter, text="End", command=reseeet).pack(side="bottom")
        exiter.mainloop()



    app = Tk()
    inp = Entry(app)
    keyinp = Entry(app)
    app.title("AES")
    app.geometry("800x600")
    bg = PhotoImage(file="857px-The.Matrix.glmatrix.2.png")
    background_label = ttk.Label(app, image=bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    frame1 = LabelFrame(app, borderwidth=0, highlightthickness=0)
    frame1.grid(row=5, column=5,padx=(200, 10),pady=(100, 10))
    Button(frame1, text="Encrypt",command=encrypt).pack()
    frame2 = LabelFrame(app,borderwidth=0, highlightthickness=0)
    frame2.grid(row=5, column=6,padx=(200, 10),pady=(100, 10))
    Button(frame2, text="Decrypt", command=decrypt).pack()
    frame3 = LabelFrame(app,borderwidth=0, highlightthickness=0)
    frame3.grid(row=6,column=5,columnspan=2,padx=(200, 10),pady=(100, 10))
    Button(frame3,text="Exit",command=exit).pack()

    app.mainloop()



    print(inp_text)




