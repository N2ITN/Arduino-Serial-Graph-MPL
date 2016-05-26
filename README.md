# Arduino-Serial-Graph-MPL
Real time plotting of serialized accelerometer data (MPU6050 IMU on Arduino) using matplotlib.

Requirements:

Hardware: Arduino Uno R3, MPU 6050

Software / Libraries: Arduino IDE, IC2DevLib for Arduino IDE, SciPy, Python 2.7.9, drawnow.py 


#Arduino_Serial_Input.py

  Reads serial data streaming from Arduino
  
  Modified from: https://github.com/gregpinero/ArduinoPlot. 

#MPU6050_raw.ino

  Sets up streaming data from Arduino
  
  Based on: http://github.com/jrowberg/i2cdevlib.  

#PlotNow.py
  Calibrates sensors. Plots incoming Serial data in real time using matplotlib. Threading used to clear plotting buffer periodically.
  
  TODO: Implement FIFO buffer in place of threading solution
  
  Based on http://www.toptechboy.com/tutorial/python-with-arduino-lesson-11-plotting-and-graphing-live-data-from-arduino-with-matplotlib/
