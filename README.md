# Arduino-Serial-Graph-MPL
Tools for plotting accelerometer data in real time.

Requirements:
Hardware: Arduino Uno R3, MPU 6050

Software: Arduino IDE, IC2DevLib for Arduino IDE, SciPy stack, Python 2.7.9, drawnow Python module

Credits:
Code is based on snippets from several sources which have been modified by me, in some cases extensively, for the purposes of displaying unaltered Accelerometer data in real time with my particular set up.

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
