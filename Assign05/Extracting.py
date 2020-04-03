from PIL import Image

class Extracting:
    def __init__(self, dirty_filename, extracted_filename):
        self.extracted_filename = extracted_filename
        self.dirty_file = Image.open(dirty_filename)
        self.pixels = ()
        self.height = 0
        self.width = 0
        self.extracted_data = ''
        self.pixels = []
        self.extracted_text = ''
        
    def get_image_data(self):
        self.pixels = self.dirty_file.load()
        self.width, self.height = self.dirty_file.size
    
    def extract_from_pixel(self,pixel):
        self.extracted_data += bin(pixel[0])[-1]
        self.extracted_data += bin(pixel[1])[-1]
        self.extracted_data += bin(pixel[2])[-1]
        
    def extract_from_image(self):
        for x in range (0,self.width): #each row
            for y in range (0,self.height): #each column
                pixel = list(self.pixels[x,y])
                self.extract_from_pixel(pixel)
                
        
    def from_bitstream_to_text(self):
        chars = []
        for i in range(len(self.extracted_data)//8):
            byte = self.extracted_data[i*8:(i+1)*8]
            dec = int(''.join([str(bit) for bit in byte]),2)
            if(dec == 4):
                break
            chars.append(chr(dec))
            print(dec)
        self.extracted_text = ''.join(chars)
    
    def save_extracted_text(self):
        extracted = open(self.extracted_filename,"w")
        extracted.write(self.extracted_text)
        extracted.close()
        
    def extracting_process(self):
        self.get_image_data()
        self.extract_from_image()
        self.from_bitstream_to_text()
        self.save_extracted_text()
        



