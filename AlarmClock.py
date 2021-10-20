import core
import time 
from plyer import notification

from datetime import datetime,date
import threading

allAlarm=[]
class AlarmClock:
    monday:bool =False
    tuesday:bool =False
    wednesday:bool =True
    thursday:bool =False
    friday:bool =False
    saturday:bool =False
    sunday:bool =False

    enabled:bool = True

    hourBox = core.Button(40,20,100,50,f"{11}")
    minuteBox = core.Button(120,20,100,50,f"{26}")
    secondBox = core.Button(200,20,100,50,f"{0}")

    changeHour = core.Button(40,-10,20,20)
    changeminute = core.Button(120,-10,20,20)
    changesecond = core.Button(200,-10,20,20)


    AddAlarm = core.Button(40,120,100,50,f"Add")
    hourTime:int=11
    minuteTime:int=26
    secondTime:int=40
    

    def onupdate(self):  
        e = datetime.now()
        if self.changeHour.IsPressed():
            if self.hourBox.text == str(24):
                self.hourBox.text="0"
            else:
                text = int(self.hourBox.text)
                text=text+1
                self.hourBox.text=str(text)
        
        if self.changeminute.IsPressed():
            if self.minuteBox.text == str(59):
                self.minuteBox.text="0"
            else:
                text = int(self.minuteBox.text)
                text=text+1
                self.minuteBox.text=str(text)

        if self.changesecond.IsPressed():
            if self.secondBox.text == str(59):
                self.secondBox.text="0"
            else:
                text = int(self.secondBox.text)
                text=text+1
                self.secondBox.text=str(text)
        
        if self.AddAlarm.IsPressed():
            allAlarm.append(self)
            print("Added alarm")
    
    def CheckAlarm(self):
        e = datetime.now()
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
        notification.notify(
        title = 'Clock app',
        message = 'Timer is complete',
        app_icon = None,
        timeout = 10,
        )




