from PIL import Image
import bitarray

class Embedding:
    def __init__(self, payload_filename, overt_filename, dirty_filename):
        payload_file = open(payload_filename, "r")
        self.payload = payload_file.read()
        payload_file.close()
        self.txt_length = 0
        self.bitstream = ''
        self.current_bit = 0
        overt_file = Image.open(overt_filename)
        overt_file.save(dirty_filename)
        overt_file.close()
        self.dirty_file = Image.open(dirty_filename)
        self.dirty_filename = dirty_filename
        self.offset = 32
        self.pixels = ()
        self.width = 0 # width of the image
        self.height = 0 # height of the image
        self.new_pixel = [0,0,0] # pixel after the changes in RGB
        
    def text_to_bitstream(self):
        pay = self.payload
        bit_array = bitarray.bitarray()
        bit_array.frombytes(pay.encode('utf-8'))
        self.bitstream = [int(i) for i in bit_array]
        self.txt_length = len(self.bitstream)
    
    def get_image_data(self):
        self.pixels = self.dirty_file.load()
        self.width, self.height = self.dirty_file.size
        
            
        
    def change_last_bit(self, currpixel, bit_to_change, plan):
        byte = currpixel[plan]
        bin_byte = bin(byte)
        self.new_pixel[plan] = int(bin_byte[:-1] + str(bit_to_change),2)
        self.current_bit += 1
            
    def change_pixel(self, x, y,data):
        self.new_pixel = list(self.pixels[x,y]) # the current pixel
        remaining = (self.txt_length - self.current_bit) # nb of remaining changes
        nb_of_change = remaining if remaining < 3 else 3 # if < 3 bits remaining, the changes won't be on R,G and B
        for i in range(0,nb_of_change):
            self.change_last_bit(self.new_pixel, data[self.current_bit], i)
        self.pixels[x,y] = tuple(self.new_pixel)
        
    def change_image (self):
        for x in range(0, self.width):
            for y in range(self.offset, self.height):
                if (self.current_bit == self.txt_length):
                    return
                self.change_pixel(x, y, self.bitstream)
    
    def hide_size(self): #Hide the size of the textfile
        binary_size = bin(self.txt_length)[2:]
        store_len = self.txt_length
        length = (self.offset*3 - len(binary_size))
        binary_size = '0'*length + binary_size
        self.txt_length = self.offset*3
        for y in range (0,self.offset):               
            self.change_pixel(0,y, binary_size)
        self.current_bit = 0
        self.txt_length = store_len
            
    def save_embedded_image(self):
        self.dirty_file.save(self.dirty_filename)
        
    def embedding_process(self):
        self.text_to_bitstream()
        self.get_image_data()
        self.hide_size()
        self.change_image()
        self.save_embedded_image()











                




