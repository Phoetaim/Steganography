# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 11:07:28 2020

@author: clems
"""
import bitarray
import base64

message = 'YourVerySecretText'

#Converts the message into an array of bits
ba = bitarray.bitarray()
ba.frombytes(message.encode('utf-8'))
extracted = [int(i) for i in ba]
print(extracted)
chars = []
for i in range(len(extracted)//8):
    byte = extracted[i*8:(i+1)*8]
    dec = int(''.join([str(bit) for bit in byte]),2)
    chars.append(chr(dec))
    if (dec == 26):
        break
data = ''.join(chars)

print(data)