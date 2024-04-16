The Arduino code (radiometro.ino) reads ten samples (Ts=100ms) from the analog inputs A0 and A1, where the RF and LNAs temperature sensor are connected to, respectively, and puts the average of each data samples on the serial port.
The main1 Python code reads data from the serial port at a settable sampling period, and puts the data, including linux time stamp into a file, named after the current date (eg. 2024-05-25.txt). 
The main2 Python code enables real-live visualization of the RF data being read from the serial port. 
