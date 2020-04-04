from Embedding import Embedding
from Extracting import Extracting
from tkinter import filedialog
from tkinter import Button
from tkinter import Label
from tkinter import Menu
from tkinter import NORMAL
from analysis import Analysis


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
        
        # Menu
        self.menubar = Menu(self.root)

        embedding_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Embedding", menu=embedding_menu)
        embedding_menu.add_command(label="Choose text file", command=self.text_open)
        embedding_menu.add_command(label="Choose carrier file", command=self.carrier_open)
        
        extract_menu = Menu(self.menubar, tearoff=0)
        extract_menu.add_command(label="Choose dirty file", command=self.dirty_open)
        self.menubar.add_cascade(label="Extracting", menu=extract_menu)
        
        analysis_menu = Menu(self.menubar, tearoff=0)
        analysis_menu.add_command(label="PSNR", command=self.PSNR)
        analysis_menu.add_command(label="SSIM", command=self.SSIM)
        self.menubar.add_cascade(label="Analysis", menu=analysis_menu, state = "disabled")
        
        self.menubar.add_command(label="exit", command=self.quit)
        self.root.config(menu=self.menubar)
        
        # Buttons
        self.embed_button = Button(self.root, text="Embedding", command = self.embed_function, state='disabled')
        self.extract_button = Button(self.root, text="Extracting", command = self.extract_function, state='disabled')
        
        # Labels
        self.text_label= Label(self.root, text = '')
        self.carrier_label = Label(self.root, text = '')
        self.dirty_label = Label(self.root, text = '')
        self.algo_label = Label(self.root, text = 'No Algorithm done')
        self.PSNR_label = Label(self.root,text = '')
        self.SSIM_label = Label(self.root, text = '')
        
        # Placement
        self.embed_button.grid(column=1, row=0)
        self.extract_button.grid(column=1, row=2)
        self.text_label.grid(column=2, row=0)
        self.carrier_label.grid(column=2, row=1)
        self.dirty_label.grid(column=2, row=2)
        self.algo_label.grid(column=2, row=3)
        self.PSNR_label.grid(column=2, row=4)
        self.SSIM_label.grid(column=2, row=5)
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
        self.menubar.entryconfig("Analysis", state="normal")
        self.analysis = Analysis(self.carrier_file,self.dirty_file)
        
    def extract_function(self):
        extract = Extracting(self.dirty_file ,self.extracted_file)
        extract.extracting_process()
        self.algo_label['text'] = "Extracting done!"  
        
    # Analysis
    def PSNR(self):
        psnr = self.analysis.calculate_psnr()
        self.PSNR_label['text'] = "PSNR: " + str(psnr)
    
    def SSIM(self):
        ssim = self.analysis.calculate_ssim()
        self.SSIM_label['text'] = "SSIM: " + str(ssim)   
            


    
