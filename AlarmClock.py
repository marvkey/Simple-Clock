import core
import time 
from plyer import notification

from datetime import datetime,date
import threading

allAlarm=[]
class AlarmClock:
    monday:bool =False
    tuesday:bool =False
    wednesday:bool =False
    thursday:bool =False
    friday:bool =False
    saturday:bool =False
    sunday:bool =False

    enabled:bool = True

    hourBox = core.Button(40,20,100,50,f"{0}")
    minuteBox = core.Button(120,20,100,50,f"{0}")
    secondBox = core.Button(200,20,100,50,f"{0}")

    SetTime = core.Button(40,120,100,50,f"Set")
    hourTime:int=0
    minuteTime:int=0
    secondTime:int=0
    def __init__(self):
        allAlarm.append(self)

    def onUpdate(self):
        e = datetime.datetime.now()
        if self.enabled==False:
            return 
        if datetime.today().weekday()==0 and self.monday==True:
            if e.hour==self.hourTime and e.minute==self.minuteTime and e.second==self.secondTime:
                threading.Thread(target=self.StartTime).start()
        
        if datetime.today().weekday()==1 and self.tuesday==True:
            if e.hour==self.hourTime and e.minute==self.minuteTime and e.second==self.secondTime:
                threading.Thread(target=self.StartTime).start()
        
        if datetime.today().weekday()==2 and self.wednesday==True:
            if e.hour==self.hourTime and e.minute==self.minuteTime and e.second==self.secondTime:
                threading.Thread(target=self.StartTime).start()
        
        if datetime.today().weekday()==3 and self.thursday==True:
            if e.hour==self.hourTime and e.minute==self.minuteTime and e.second==self.secondTime:
                threading.Thread(target=self.StartTime).start()

        if datetime.today().weekday()==4 and self.friday==True:
            if e.hour==self.hourTime and e.minute==self.minuteTime and e.second==self.secondTime:
                threading.Thread(target=self.StartTime).start()

        if datetime.today().weekday()==5 and self.saturday==True:
            if e.hour==self.hourTime and e.minute==self.minuteTime and e.second==self.secondTime:
                threading.Thread(target=self.StartTime).start()


        if datetime.today().weekday()==6 and self.sunday==True:
            if e.hour==self.hourTime and e.minute==self.minuteTime and e.second==self.secondTime:
                threading.Thread(target=self.StartTime).start()
    
    def StartAlarm(self):
        notification.notify(title = 'Clock app',message = 'Timer is complete',app_icon = None,timeout = 10)




