import matplotlib.pyplot as plt #import matplotlib library
from drawnow import *
import time
import matplotlib.lines as mlines
print 'setting up...'
XVals = []
YVals =[]
ZVals = []
#plt.ion() #Tell matplotlib you want interactive mode to plot live data
cnt=0

from Arduino_Monitor import SerialData as DataGen

data = DataGen()
time.sleep(3)

def makeFig(): 
                              
    plt.title('My Live Acc Sensor Data')    
    plt.grid(True) 
    plt.ylim( -40000, 40000)                              
 
    plt.ticklabel_format(useOffset=False)                          
    
    plt.plot(XVals, 'g-')
    plt.plot(YVals, 'b-')       
    plt.plot(ZVals, 'r-')
    green_line = mlines.Line2D([], [], color='green',
                          markersize=10, label='X')
    blue_line = mlines.Line2D([], [], color='blue',
                          markersize=10, label='Y')

    red_line = mlines.Line2D([], [], color='red',
                          markersize=10, label='Z')
    plt.legend(handles=[green_line, blue_line,red_line],loc=2)

Xoff = 0
Yoff = 0
Zoff = 0

def cal():
    print 'calibrating sensors...'
    global Xoff
    global Yoff
    global Zoff
    Xcal = []
    Ycal = []
    Zcal = []
    for i in range(10):
        try:
            time.sleep(.25)  
            dataArray = data.next().split('\t')
            Xcal.append(int(dataArray[0]) )
            Ycal.append(int(dataArray[1]) )          
            Zcal.append(int(dataArray[2]) ) 
        except ValueError:
            print "Value Error:" % dataArray
               
    
        
    Xoff =  sum(Xcal)/len(Xcal)
    Yoff =  sum(Ycal)/len(Ycal)          
    Zoff =  sum(Zcal)/len(Zcal)
    

cal()
while True: 
    xList = []
    yList = []
    zList = []
    
    
    try:   

        dataArray = data.next().split('\t')

        XVals.append(int(dataArray[0]) - Xoff)          
        YVals.append(int(dataArray[1]) - Yoff)
        ZVals.append(int(dataArray[2]) - Zoff)                 
        drawnow(makeFig)                   
                    
        cnt=cnt+1
        if(cnt>30):                          
            ZVals.pop(0)  
            YVals.pop(0)
            XVals.pop(0)                  
            
#        if cnt > 200:
#            data.__del__()
#            exit()
    except Exception as e:
        print e, dataArray
        
