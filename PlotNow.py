

import matplotlib.pyplot as plt #import matplotlib library
import matplotlib.figure as fig
import time
import matplotlib.lines as mlines
print 'setting up...'
XVals = []
YVals =[]
ZVals = []
#plt.ion() #Tell matplotlib you want interactive mode to plot live data
cnt=0
Clist = []
from Arduino_Serial_Input import SerialData as DataGen

data = DataGen()
time.sleep(2)



def makeFig(): 

        #plt.clf()
#        plt.title('Live Sensor Data')    
#        plt.grid(True) 
        plt.ylim( -40000, 40000)  
        
                           
        plt.xlim(cnt-40,cnt)

        plt.ticklabel_format(useOffset=False)  
#        green_line = mlines.Line2D([], [], color='green',
#                              markersize=10, label='X')
#        blue_line = mlines.Line2D([], [], color='blue',
#                              markersize=10, label='Y')
#        red_line = mlines.Line2D([], [], color='red',
#                              markersize=10, label='Z')
#        plt.legend(handles=[green_line, blue_line,red_line],loc=2)
        
              
        plt.plot(Clist,XVals, 'g-')
        plt.plot(Clist,YVals, 'b-')       
        plt.plot(Clist,ZVals, 'r-')
    
        
        plt.draw()
    
    

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
            time.sleep(.05)  
            dataArray = data.next().split('\t')
            Xcal.append(int(dataArray[0]) )
            Ycal.append(int(dataArray[1]) )          
            Zcal.append(int(dataArray[2]) ) 
        except ValueError:
            print "Value Error:" % dataArray
                  
        
    Xoff =  sum(Xcal)/len(Xcal)
    Yoff =  sum(Ycal)/len(Ycal)          
    Zoff =  sum(Zcal)/len(Zcal)
  


def grab():
        
        global cnt
        global Clist
        global ZVals
        global YVals
        global XVals
        dataArray = data.next().split('\t')      
        try:
                     
            XVals.append(int(dataArray[0]) - Xoff)          
            YVals.append(int(dataArray[1]) - Yoff)
            ZVals.append(int(dataArray[2]) - Zoff)                 
    
            
                               
            cnt=cnt+1
            Clist.append(cnt)
#            if(cnt>50):                                         

#                
            if cnt > 200:
                global a
                a = False
#                data.__del__()
#                exit()
            
        except Exception as e:
            print e, dataArray

def clear():
    
    while True:
        time.sleep(3)
        plt.clf()
        
    
def main():
    
    from threading import Thread
    timer = []
    a= True
    cal()
    global XVals
    global YVals
    global ZVals
    global Clist
    
    Thread(target=clear).start()

    while a:
        start = time.time()
        grab()
        
        makeFig()
        end = time.time()

        timer.append(end-start)
        if cnt > 150:
            a = False
        
            

            
            
    plt.clf()
    plt.plot(timer)
    plt.grid(True)
    plt.title('ave time: %s' % (sum(timer)/len(timer)))
    plt.show()
        
        
main()
        
