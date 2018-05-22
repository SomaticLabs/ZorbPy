import logging, time
import zorb

# Configure logging to print out info messages
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def mainloop():
    # perform initial connection to Zorb device
    zorb.connect()

    # trigger series of 3 pre-programmed effects
    zorb.triggerPattern(zorb.POINT_LEFT)
    time.sleep(2.5) # wait for 2.5 seconds
    zorb.triggerPattern(zorb.POINT_RIGHT)
    time.sleep(2.5) # wait for 2.5 seconds
    zorb.triggerPattern(zorb.HANDS_RAISED)

    # turn each actuator on
    zorb.writeActuators(1000, 100, 0, 0, 0)
    time.sleep(1) # wait for 1000 milliseconds
    zorb.writeActuators(1000, 0, 100, 0, 0)
    time.sleep(1) # wait for 1000 milliseconds
    zorb.writeActuators(1000, 0, 0, 100, 0)
    time.sleep(1) # wait for 1000 milliseconds
    zorb.writeActuators(1000, 0, 0, 0, 100)
    time.sleep(1) # wait for 1000 milliseconds

    # turn off all actuators
    zorb.writeActuators(100, 0, 0, 0, 0)


def main():
    zorb.run(mainloop)


if __name__ == '__main__':
    main()
