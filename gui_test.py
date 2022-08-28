 
from time import sleep
from tkinter import *
from datetime import datetime
from tkinter.ttk import Progressbar, Style
from threading import Thread

MICROSECONDS = 1000000.0
MICROMINUTES = MICROSECONDS * 60.0
MICROHOURS = MICROMINUTES * 60.0
MICRODAY  = MICROHOURS * 12.0




def Seconds():
    row = 0
    now = datetime.now()
    s_micro = now.second * MICROSECONDS + now.microsecond
    m_micro = now.minute * MICROMINUTES + s_micro
    h_micro = now.minute * MICROMINUTES + m_micro
    row = 0
    
    t_percent =   (m_micro /MICROHOURS) * 100
    print( '%f' %( now.hour +m_micro/MICROHOURS%1))
    print((m_micro/MICROHOURS) * 100)

while 1:
    
    Seconds()