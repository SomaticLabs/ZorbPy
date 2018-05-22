# ZorbPy

*Python library for integrating with the [Somatic Zorb Engine](https://zorbtouch.com)*

[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/SomaticLabs/ZorbPy/blob/master/LICENSE)
[![Twitter](https://img.shields.io/badge/twitter-@SomaticLabs-orange.svg?style=flat)](http://twitter.com/SomaticLabs)

## Installation

First install the [Adafruit BluefruitLE library](https://github.com/adafruit/Adafruit_Python_BluefruitLE).

Please note that this library only currently supports macOS and Linux, as Windows is not currently supported by the [underlying BLE](https://github.com/adafruit/Adafruit_Python_BluefruitLE) package used for this library.

After installing the BluefruitLE library, installation of ZorbPy using [pip](https://pypi.org/project/pip/) is simple:

```sh
pip install zorb
```


## Library Usage

For a quick example on how to use the ZorbPy library, please reference [example.py](https://github.com/SomaticLabs/ZorbPy/blob/master/example.py).

To use the ZorbPy library, you must wrap the functionality of your program in a function that is passed to the `zorb.run()` function call.

Any usage of the functions provided by this library outside of the process started by `zorb.run()` will produce error behavior.


The ZorbPy library provides three main functionalities:

- connecting to advertising Zorb devices

- triggering presets on the Zorb device

- directly controlling actuator intensity on the Zorb device


To connect to an advertising Zorb device:
```python
zorb.connect()
```


To trigger one of the available presets:
```python
zorb.triggerPattern(zorb.POINT_LEFT)
```

*Note that preset haptic emojis are exist for the following emojis:*

🎊, 👈, 👉, 🤛, 🤜, ⏮️, ⏭️, 🙌, 👋, 😯, 😳, 😬, 😊, 😄, 🤣


To directly set the actuator values:
```python
duration = 100
top_left = 0
top_right = 0
bottom_left = 25
bottom_right = 25

zorb.writeActuators(duration, top_left, top_right, bottom_left, bottom_right)
```


Below is a more comprehensive example of a simple program that connects to a Zorb device, plays a confetti pattern upon successful connection, and then updates actuator values based on some hypothetical sensor output.
```python
import zorb

def mainloop():
    # perform initial connection to Zorb device
    zorb.connect()

    # trigger confetti effect upon successful connection
    zorb.triggerPattern(zorb.CONFETTI)

    # enter infinte loop for updating Zorb device
    while True:
        top_left = hypothetical_sensor_1.val()
        top_right = hypothetical_sensor_2.val()
        bottom_left = hypothetical_sensor_3.val()
        bottom_right = hypothetical_sensor_4.val()
        zorb.writeActuators(10, top_left, top_right, bottom_left, bottom_right)
        time.sleep(0.01)


def main():
    zorb.run(mainloop)


if __name__ == '__main__':
    main()
```

## Style Guide

Contributions to this project should conform to this [Python Style Guide](https://www.python.org/dev/peps/pep-0008/).

## License

ZorbPy is released under the [MIT license](https://github.com/SomaticLabs/ZorbPy/blob/master/LICENSE).
