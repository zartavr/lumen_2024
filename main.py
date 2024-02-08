import serial # import Serial Library
import string

import numpy # Import numpy

import matplotlib.pyplot as plt #import matplotlib library

from drawnow import *

arduinoData = serial.Serial('com4', 115200) #Creating our serial object named

plt.ion() #Tell matplotlib you want interactive mode to plot live data
cnt=0

def makeFig(): #Create a function that makes our desired plot
    plt.ylim(80,90) #Set y min and max values
    plt.title('My Live Streaming Sensor Data') #Plot the title
    plt.grid(True) #Turn the grid on
    plt.ylabel('Temp F') #Set ylabels
    plt.plot(temp, 'ro-', label='Degrees F') #plot the temperature
    plt.legend(loc='upper left') #plot the legend
    # plt.ylim(93450,93525) #Set limits of second y axis- adjust to readings you are getting
    

makeFig()
while True: # While loop that loops forever
    while (arduinoData.inWaiting()==0): #Wait here until there is data

        pass #do nothing

    arduinoString = str(arduinoData.readline()) #read the line of text from the serial port

    dataArray = arduinoString.split(' ') #Split it into an array called dataArray

    temp = int(dataArray[0].strip(string.ascii_letters+string.punctuation)) #Convert first element to floating number and put in temp

    plt.pause(.000001) #Pause Briefly. Important to keep drawnow from crashing

    cnt=cnt+1

    # if(cnt>50): #If you have 50 or more points, delete the first one from the array 
    #     temp.pop(0) #This allows us to just see the last 50 data points