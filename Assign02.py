
filename = "text.txt"
FileINPUT = open(filename, "r")
FileOUTPUT = open("binary_text.txt", "w")

data = FileINPUT.read()
bin = bin(int.from_bytes(data.encode(), 'big'))[2:]

FileOUTPUT.write(bin)

FileINPUT.close()
FileOUTPUT.close()
