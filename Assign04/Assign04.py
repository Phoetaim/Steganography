import struct
image = 'ballons_rgb.bmp'

def getBMPHeaderInfo (image):
    image = open(image, 'rb')
    imageType = image.read(2).decode()

    if (imageType == "BM"):
       print("The file is a BMP image")
    else: 
        print("The file is NOT a BMP image, please change your file!")

    imageSize = struct.unpack('I', image.read(4))
    struct.unpack('Q', image.read(8)) #Offset for unpacking
    imageHeaderSize = struct.unpack_from('i', image.read(4))
    imageHeaderSize = int(''.join(map(str, imageHeaderSize)))
    if (imageHeaderSize == 124):
        print("the header is BITMAPV5HEADER, the correct version")
    else:
        print('%s' % imageHeaderSize)
        print("please use a bitmap image with a correct header version!")
        exit
    print('Image size: %s' % imageSize)
    width = struct.unpack('I', image.read(4))
    height = struct.unpack('I', image.read(4))
    print("Image width: %s" % width)
    print("Image height: %s" % height)
    image.close()

def createBMPImage(image):
    I = open(image, 'rb')
    imageData = I.read()
    I.close()
    
    newImage = open('newBMP.bmp', 'wb')
    newImage.write(imageData)
    newImage.close()
    print("New image created")
    
getBMPHeaderInfo(image)
createBMPImage(image)
