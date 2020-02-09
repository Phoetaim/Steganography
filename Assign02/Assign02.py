
filename = "Assign02/Declaration_of_Independance.txt"
FileINPUT = open(filename, "r")
FileOUTPUT = open("Assign02/binary_text_python.txt", "w")

data = FileINPUT.read()
bin = bin(int.from_bytes(data.encode(), 'big'))[2:]

FileOUTPUT.write(bin)

FileINPUT.close()
FileOUTPUT.close()
