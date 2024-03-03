import serial # import Serial Library
import string

import numpy # Import numpy
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt #import matplotlib library

from drawnow import *

arduinoData = serial.Serial('/dev/ttyUSB0', 115200) #Creating our serial object named
# arduinoData = serial.Serial('com3', 115200) #Creating our serial object named


tempF= []
plt.ion() #Tell matplotlib you want interactive mode to plot live data
cnt=0

def makeFig(): #Create a function that makes our desired plot
    plt.title('Time') #Plot the title
    plt.grid(True) #Turn the grid on
    plt.ylabel(f'$l, мм$') #Set ylabels
    plt.plot(tempF, 'ro-', label='l, mm') #plot the temperature
    plt.legend(loc='upper left') #plot the legend
    plt.ylim(0, 250) #Set limits of second y axis- adjust to readings you are getting
    

makeFig()
while True: # While loop that loops forever
    while (arduinoData.inWaiting()==0): #Wait here until there is data
        pass #do nothing

    arduinoString = str(arduinoData.readline()) #read the line of text from the serial port

    dataArray = arduinoString.split(' ') #Split it into an array called dataArray
    print(dataArray)

    temp = int(dataArray[0].strip(string.ascii_letters+string.punctuation)) #Convert first element to floating number and put in temp

    if temp < 2100:
        tempF.append(temp)                     #Build our tempF array by appending temp readings
        drawnow(makeFig)                       #Call drawnow to update our live graph
        plt.pause(.000001)                     #Pause Briefly. Important to keep drawnow from crashing
        cnt=cnt+1
        if(cnt>50):                            #If you have 50 or more points, delete the first one from the array
            tempF.pop(0)                       #This allows us to just see the last 50 data points