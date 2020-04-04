from Embedding import Embedding
from Extracting import Extracting
from tkinter import filedialog
from tkinter import *


class Window:
    
    def __init__(self,root):
        
        self.check = 1
        self.carrier_file = ''
        self.text_file = ''
        self.dirty_file = ''
        self.extracted_file = "extracted_file.txt"
        
        self.root = root
        self.root.title("LSB Algorithm")
        self.root.geometry('600x300')
        menubar = Menu(self.root)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Choose text file", command=self.text_open)
        filemenu.add_command(label="Choose carrier file", command=self.carrier_open)
        menubar.add_cascade(label="Embedding", menu=filemenu)
        
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Choose dirty file", command=self.dirty_open)
        menubar.add_cascade(label="Extracting", menu=editmenu)
        
        menubar.add_command(label="exit", command=self.quit)
        self.root.config(menu=menubar)
        
        self.embed_button = Button(self.root, text="Embedding", command = self.embed_function, state='disabled')
        self.extract_button = Button(self.root, text="Extracting", command = self.extract_function, state='disabled')
        self.text_label= Label(self.root, text = '')
        self.carrier_label = Label(self.root, text = '')
        self.dirty_label = Label(self.root, text = '')
        self.algo_label = Label(self.root, text = 'No Algorithm done')
        
        self.embed_button.grid(column=1, row=0)
        self.extract_button.grid(column=1, row=2)
        self.text_label.grid(column=2, row=0)
        self.carrier_label.grid(column=2, row=1)
        self.dirty_label.grid(column=2, row=2)
        self.algo_label.grid(column=2, row=10)
    # Open files
    def carrier_open(self):
        self.carrier_file =  filedialog.askopenfilename(initialdir = "./",title = "Select carrier file",filetypes = [("bmp files","*.bmp")])
        if (len(self.text_file) > 0):
            self.embed_button.config(state=NORMAL)
        self.carrier_label['text'] = self.carrier_file  
        
            
    def text_open(self):
        self.text_file =  filedialog.askopenfilename(initialdir = "./",title = "Select text file",filetypes = [("text files","*.txt")])
        if (len(self.carrier_file) > 0):
            self.embed_button.config(state=NORMAL)
        self.text_label['text'] = self.text_file  
        
       
    def dirty_open(self):
        self.dirty_file =  filedialog.askopenfilename(initialdir = "./",title = "Select dirty file",filetypes = [("bmp files","*.bmp")])
        if (len(self.dirty_file) > 0):
            self.extract_button.config(state=NORMAL)
        self.dirty_label['text'] = self.dirty_file  
        
    # Exit
    def quit(self):
        self.check = 0
        self.root.quit
        
    # Stego functions
    def embed_function(self):
        self.dirty_file = "LSBFile.bmp"
        embed = Embedding(self.text_file, self.carrier_file, self.dirty_file)
        embed.embedding_process()
        self.extract_button.config(state=NORMAL)
        self.algo_label['text'] = "Embedding done!"
        self.dirty_label['text'] = self.dirty_file
    def extract_function(self):
        extract = Extracting(self.dirty_file ,self.extracted_file)
        extract.extracting_process()
        self.algo_label['text'] = "Extracting done!"  
           
            


    
