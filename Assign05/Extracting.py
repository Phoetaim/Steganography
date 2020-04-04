from PIL import Image

class Extracting:
    def __init__(self, dirty_filename, extracted_filename):
        self.extracted_filename = extracted_filename
        self.dirty_file = Image.open(dirty_filename)
        self.pixels = ()
        self.height = 0
        self.width = 0
        self.offset = 32
        self.txt_length = 0
        self.current_bit = 0
        self.extracted_data = ''
        self.pixels = []
        self.extracted_text = ''
        
    def get_image_data(self):
        self.pixels = self.dirty_file.load()
        self.width, self.height = self.dirty_file.size
    
    def extract_size(self):
        self.txt_length = self.offset*3
        for y in range (0,self.offset):
            self.extract_from_pixel(0,y)
        print(self.extracted_data)
    
        
    def extract_from_last_bit(self,pixel, plan):
        self.extracted_data += bin(pixel[plan])[-1]
        self.current_bit += 1
        
    def extract_from_pixel(self, x, y):
        pixel = list(self.pixels[x,y])
        remaining = (self.txt_length - self.current_bit) # nb of remaining changes
        nb_to_retreive = remaining if remaining < 3 else 3 # if < 3 bits remaining, the changes won't be on R,G and B
        for i in range(0,nb_to_retreive):
            self.extract_from_last_bit(pixel, i)
        
    def extract_data_from_image(self):
        for x in range (0,self.width): #each row
            for y in range (self.offset,self.height): #each column
                if (self.current_bit == self.txt_length):
                    return
                self.extract_from_pixel(x,y)
                
    def from_bin_to_int(self):
        
        while(self.extracted_data[0] == '0'):
            self.extracted_data = self.extracted_data[1:]
        self.txt_length = int(''.join([str(bit) for bit in self.extracted_data]),2)
        self.extracted_data = ''
        self.current_bit = 0              
         
    def from_bitstream_to_text(self):
        chars = []
        for i in range(len(self.extracted_data)//8):
            byte = self.extracted_data[i*8:(i+1)*8]
            dec = int(''.join([str(bit) for bit in byte]),2)
            if(dec == 4):
                break
            chars.append(chr(dec))
        self.extracted_text = ''.join(chars)
    
    def save_extracted_text(self):
        extracted = open(self.extracted_filename,"w")
        extracted.write(self.extracted_text)
        extracted.close()
        
    def extracting_process(self):
        self.get_image_data()
        self.extract_size()
        self.from_bin_to_int()
        self.extract_data_from_image()
        self.from_bitstream_to_text()
        self.save_extracted_text()
        



