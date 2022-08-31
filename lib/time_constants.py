from datetime import datetime

#Progress Bar Length
PLEN = 250
BACKGROUND ='#3299a8'

#microsecond constants
MICROSECONDS = 1000000.0
MICROMINUTES = MICROSECONDS * 60
MICROHOURS = MICROMINUTES * 60
MICRODAY  = MICROHOURS * 24 
#Month calculated in function 

now = datetime.now()
TODAY = now.day
if((now.year % 400 == 0) or  
     (now.year % 100 != 0) and  
     (now.year % 4 == 0)):   
     LEAPYEAR = 1
else:
    LEAPYEAR =0 
MICROYEAR = MICRODAY * (365+LEAPYEAR)

def month_days(d,year):
    match d:
        case 1:
            return 31
        case 2:
            #check for leap year
            if (year %400 or (year%100!=0 and year%4==0)):
                return 29
            return 28
        case 3:
            return 31
        case 4:
            return 30
        case 5:
            return 31
        case 6:
            return 30
        case 7:
            return 31
        case 8:
            return 31
        case 9:
            return 30
        case 10:
            return 31
        case 11:
            return 30
        case 12:
            return 31
    