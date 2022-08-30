from datetime import datetime
from time import *

bits =[]
for i in range(32):
    bits.append("\u25A0")

def add1(bit_array):
    for i in range(len(bit_array)):
        if bit_array[i] == 0:
            bit_array[i]= 1
            return bit_array
        elif bit_array[i] == 1 and bit_array[i] != len(bit_array):
            return add1(bit_array.pop(0))
            
        else:
            for i in bit_array:
                bit_array[i]=0
                return bit_array


def bitadds():
    bitadd(0)
def bitadd(index):
    if bits[index] == 0:
        bits[index] =1
        return 
    elif bits[index] == 1 and index != len(bits)-1:
        bits[index] = 0
        return bitadd(index+1)   
    else:
        for i in range(len(bits)):
            bits[i]=0
        return 

def t():
    index = 0
    while index < len(bits):  
        if bits[index] == "\u25A0":
            bits[index] ="\u25A1"
            return 
        elif bits[index] == "\u25A1" and index != len(bits)-1:
            bits[index] = "\u25A0"
            index+=1  
        else:
            for i in range(len(bits)):
                bits[i]="\u25A0"
            return 


while 1:
    print(bits[1])
    t()
    sleep(1)


