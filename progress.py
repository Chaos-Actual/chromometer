from tkinter import *
from datetime import datetime
from tkinter.ttk import Progressbar, Style
from threading import Thread
from time import sleep
import time
from lib.time_constants import *
from lib.sun_moon import get_sun_moon

#Progress Bar Length
PLEN = 250
BACKGROUND ='#3299a8'

bits =[]
for i in range(32):
    bits.append("\u25A1")
            
app = Tk()
app_style = Style()
app_style.theme_use('alt')
app_style.configure("mine.Horizontal.TProgressbar", troughcolor =BACKGROUND, 
                        background='lightblue', thickness=5)
app.config(background='#3299a8')
app.title('Progress Bar')
app.geometry("1000x500")
canvas = Canvas(app)

def  Create_time_labels():
    row =10
    labels = [
    Label(app,text="Second",background=BACKGROUND, anchor='e', width=6,justify='right'),
    Label(app,text="Minute",background=BACKGROUND, anchor='e', width=6,justify='right'),
    Label(app,text="Hour",background=BACKGROUND, anchor='e',width=6,justify='right'),
    Label(app,text="Day",background=BACKGROUND, anchor='e',width=6,justify='right'),
    Label(app,text="Month",background=BACKGROUND, anchor='e', width=6,justify='right'),
    Label(app,text="Year",background=BACKGROUND, anchor='e', width=6,justify='right')
    ]
    for i in range(6):
        labels[i].grid(row=i+1,column=0)
    return labels
    
def Create_time_count_labels():
    column= 1
    labels =[]
    for i in range(6):
        labels.append(Label(app,text=i,background=BACKGROUND,relief='ridge',anchor='w', width=13,justify='right'))
        labels[i].grid(row=i+1,column=column)       
    return labels

def Create_progress_bars():
    column= 2
    pbars =[]
    for i in range(6):
        pbars.append(Progressbar(app, orient=HORIZONTAL,
                style="mine.Horizontal.TProgressbar",
                length=PLEN, mode="determinate"))
        pbars[i].grid(row=i+1,column=column)       
    return pbars

def Create_percent_labels():
    column= 3
    labels =[]
    for i in range(6):
        labels.append(Label(app,text=i,background=BACKGROUND))
        labels[i].grid(row=i+1,column=column)       
    return labels 

def  Create_sun_moon_labels():
    row = 10
    labels = [
    Label(app,text="Dawn",background=BACKGROUND, anchor='e', width=10,justify='right'),
    Label(app,text="Sunrise",background=BACKGROUND, anchor='e', width=10,justify='right'),
    Label(app,text="Sunset",background=BACKGROUND, anchor='e',width=10,justify='right'),
    Label(app,text="Dusk",background=BACKGROUND, anchor='e',width=10,justify='right'),
    Label(app,text="Moon Phase",background=BACKGROUND, anchor='e', width=10,justify='right')
    ]
    for i in range(len(labels)):
        labels[i].grid(row= row+i,column=0)
    return labels

def Create_sun_moon_times_label():
    row = 10
    labels = [
    ]
    for i in range(5):
        labels.append(Label(app,background=BACKGROUND, anchor='w', width=30,justify='right'))

    for i in range(len(labels)):
        labels[i].grid(row= row+i,column=1,columnspan=2)
    return labels

def update_time():
# Seconds:
    row = 0
    now = datetime.now()
    s_micro = now.second * MICROSECONDS + now.microsecond
    m_micro = now.minute * MICROMINUTES + s_micro
    h_micro = now.hour * MICROHOURS + m_micro
    d_micro = (now.day -1) * MICRODAY + h_micro
    
    t_percent =   (now.microsecond /MICROSECONDS) 
    label_time_count[row].config(text='%10.8f' %( now.second +t_percent))
    t_percent *= 100
    pbars[row]['value'] = t_percent
    label_percents[row].config(text="{:.0f}%".format(t_percent))
    
# Minutes:
    row +=1
    t_percent =   (s_micro/MICROMINUTES) 
    label_time_count[row].config(text='{:10.8f}'.format( now.minute +t_percent))
    t_percent *=100
    pbars[row]['value'] = t_percent
    label_percents[row].config(text="{:.0f}%".format(t_percent))
    
# Hours:
    row +=1
    t_percent =   (m_micro /MICROHOURS) 
    label_time_count[row].config(text='%10.8f' %( now.hour +t_percent))
    t_percent *=100
    pbars[row]['value'] = t_percent
    label_percents[row].config(text="{:.0f}%".format(t_percent))
    
# Days:
    row +=1
    t_percent =   (h_micro /MICRODAY) 
    label_time_count[row].config(text='%10.8f' %( now.day + t_percent))
    t_percent *=100
    pbars[row]['value'] = t_percent  
    label_percents[row].config(text="{:.0f}%".format(t_percent))

# months:
    row +=1
    days_in_month = month_days(now.month,now.year)
    mircomonth = MICRODAY  * days_in_month
    t_percent =   (d_micro /mircomonth) 
    label_time_count[row].config(text='%10.8f' %( now.month+t_percent),justify=RIGHT)
    t_percent *= 100
    pbars[row]['value'] = t_percent 
    label_percents[row].config(text="{:.0f}%".format(t_percent))

#Years:
    row+=1
    y_micro = MICRODAY * (now.timetuple().tm_yday -1) + h_micro
    t_percent =   (y_micro /MICROYEAR) 
    label_time_count[row].config(text='%12.8f' %( now.year+t_percent))
    t_percent *= 100
    pbars[row]['value'] = t_percent
    label_percents[row].config(text="{:.0f}%".format(t_percent))
    
    canvas.after(10,update_time)

 #updates bits and unix time  
def bitadd():
    label_bit_add.config(text=bits)
    index = 0
    while index < len(bits):  
        if bits[index] == "\u25A1":
            bits[index] ="\u25A0"
            break 
        elif bits[index] == "\u25A0" and index != len(bits)-1:
            bits[index] = "\u25A1"
            index+=1  
        else:
            for i in range(len(bits)):
                bits[i]="\u25A1"
            break
    unixtime = int(time.time())
    label_unix_time.config(text='Unix:' + str(unixtime))
    canvas.after(1000,bitadd)

#updates sunrise, sunset, 
def update_sun():
    now = datetime.now()
    print("here")
    sm = get_sun_moon()
    if sm["moon"] ==0:
        moon = 'New moon' 
    elif sm['moon'] <  7:
        moon = 'Waxing Crescent'
    elif sm['moon'] == 7:
        moon = 'First Quarter'
    elif sm['moon'] < 14:
        moon = 'Waxing Gibbous'    
    elif sm['moon'] == 14:
        moon = 'Full'
    elif sm['moon'] < 21:
        moon = 'Waning Gibbous'
    elif sm['moon'] == 21:
        moon = 'Last Quarter'
    elif sm['moon'] < 28:
        moon = 'Waning Crescent'

    label_sun_times[0].config(text=sm["dawn"].strftime('%H:%M:%S'))
    label_sun_times[1].config(text=sm["sunrise"].strftime('%H:%M:%S'))
    label_sun_times[2].config(text=sm["sunset"].strftime('%H:%M:%S'))
    label_sun_times[3].config(text=sm["dusk"].strftime('%H:%M:%S'))
    label_sun_times[4].config(text=moon)


label_bit_add = Label(app,background=BACKGROUND)
label_bit_add.grid(row=8,columnspan=4)
label_unix_time = Label(app, text='Unix:',background=BACKGROUND)
label_unix_time.grid(row=9,columnspan=4)

label_first_column = Create_time_labels()
label_time_count = Create_time_count_labels()
pbars = Create_progress_bars()
label_percents = Create_percent_labels()
label_sun = Create_sun_moon_labels()
label_sun_times = Create_sun_moon_times_label()
time_display = Label(app, text = 'TIME',background=BACKGROUND)
time_display.config(text=now)
time_display.grid(row=0,columnspan=4)

a = Thread(target=bitadd)
a.start()

b = Thread(target=update_time)
b.start()
b = Thread(target=update_sun)
b.start()


#app.overrideredirect(True)
app.mainloop()


