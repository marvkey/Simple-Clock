import core
import time

from plyer import notification
import threading



class Timer:
    hourBox = core.Button(40,20,100,50,f"{0}")
    minuteBox = core.Button(120,20,100,50,f"{0}")
    secondBox = core.Button(200,20,100,50,f"{0}")

    
    changeHour = core.Button(40,-10,20,20)
    changeminute = core.Button(120,-10,20,20)
    changesecond = core.Button(200,-10,20,20)

    SetTime = core.Button(40,120,100,50,f"Set")
    hourTime:int=0
    minuteTime:int=0
    secondTime:int=0
    millisecondTime=0
    timeset =False
    def onupdate(self):
        if self.changeHour.IsPressed():
            if self.hourBox.text == str(60):
                self.hourBox.text="0"
            else:
                text = int(self.hourBox.text)
                text=text+1
                self.hourBox.text=str(text)
        
        if self.changeminute.IsPressed():
            if self.minuteBox.text == str(60):
                self.minuteBox.text="0"
            else:
                text = int(self.minuteBox.text)
                text=text+1
                self.minuteBox.text=str(text)

        if self.changesecond.IsPressed():
            if self.secondBox.text == str(60):
                self.secondBox.text="0"
            else:
                text = int(self.secondBox.text)
                text=text+1
                self.secondBox.text=str(text)
        if self.SetTime.IsPressed() and self.timeset==False:
            self.timeset=True
            text =self.hourBox.text
            self.hourTime=int(text)
            text = self.minuteBox.text
            self.minuteTime =int(text)
            #text2 = self.secondBox.text
            #self.secondTime =int(text2)
            self.secondTime=int(self.secondBox.text)
            threading.Thread(target=self.StartTime).start()

        
    
    def StartTime(self):
        while self.timeset==True:
            time.sleep(1)
            self.secondTime-=1
            if(self.secondTime<=0):
                if self.minuteTime>=1:
                    self.minuteTime-=1
                if self.secondTime==0 and self.minuteTime==0 and self.hourTime==0:
                    notification.notify(
                    title = 'Clock app',
                    message = 'Timer is complete',
                    app_icon = None,
                    timeout = 10,
                    )
                    self.timeset=False
                else:
                    self.secondTime=60

            if self.minuteTime==0 :
                if self.hourTime>=1:
                    self.hourTime-=1
                    self.minuteTime=60
            self.hourBox.text=str(self.hourTime)
            self.minuteBox.text =str(self.minuteTime)
            self.secondBox.text = str(self.secondTime)

       




