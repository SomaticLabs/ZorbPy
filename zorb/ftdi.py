import sys
import serial
from struct import pack
from zorb_protocol.source import zorb_pb2
import time

timeline = zorb_pb2.Timeline()

#accepts a specified COM port string (e.g. 'COM5' for COM port #5)
#uses serial communication to write the length and timeline message to FTDI, then resets the timeline
def send_timeline(com_port_str):
    global timeline

    msg1 = timeline.SerializeToString()
    size1 = bytearray([timeline.ByteSize()])

    ser = serial.Serial(com_port_str, 9600, timeout=2)

    ser.write(size1)
    ser.write(msg1)

    timeline = zorb_pb2.Timeline()

#Channels is an 8 bit unsigned, where each bit represents a different actuator channel.
#This function accepts all the parameters for a vibration and adds that vibration to the current timeline
def add_vibration(channels, delay, duration, position, start, end, easing):
    vibration1 = timeline.vibrations.add()
    vibration1.channels = channels
    vibration1.delay = delay
    vibration1.duration = duration
    vibration1.position = position
    vibration1.start = start
    vibration1.end = end
    vibration1.easing = easing
    


