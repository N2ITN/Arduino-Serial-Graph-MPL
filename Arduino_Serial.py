
from threading import Thread
import serial

last_received = ''
def receiving(ser):
    global last_received
    buffer = ''
    while True:
        buffer = buffer + ser.read(ser.inWaiting())
        
        
        if '\n' in buffer:
            lines = buffer.split('\n') # Guaranteed to have at least 2 entries
            last_received = lines[-2]
            #If the Arduino sends lots of empty lines, you'll lose the
            #last filled line, so you could make the above statement conditional
            #like so: if lines[-2]: last_received = lines[-2]
            buffer = lines[-1]
        


class SerialData(object):
    def __init__(self, init=0):
        try:
            self.ser = ser = serial.Serial(
                port='COM2',
                baudrate=38400,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=0.1,
                xonxoff=0,
                rtscts=0,
                interCharTimeout=None
            )
        except serial.serialutil.SerialException:
            #no serial connection
            self.ser = None
        else:
            
            Thread(target=receiving, args=(self.ser,)).start()
        
        
    def next(self):
        
        return last_received
                
                
        
    def __del__(self):
        if self.ser:
            self.ser.close()

								
