import time, struct, queue
import Adafruit_BluefruitLE
from Adafruit_BluefruitLE.services import UART

import identifiers

# Name used to recognize a Zorb device
DEVICE_NAME = "Moment"

# Web address for the Somatic Labs Javascript compiler API
JAVASCRIPT_COMPILER_URL = "https://firmware.wearmoment.com/compile"


# Get the BLE provider for the current platform.
ble = Adafruit_BluefruitLE.get_provider()

# Queue for message passing to the BLE loop
bleQueue = queue.Queue()


# Connect call
def connect():
    bleQueue.put("connect")


# Main loop for processing BLE queue
def main():
    # Connect function
    def _connect():
        # Scan for devices.
        print('Searching for device...')
        try:
            self.adapter.start_scan()
            # Search for the first Moment device found (will time out after 60 seconds, but you can specify an optional timeout_sec parameter to change it).
            # self.device = self.ble.find_device(service_uuids=[self.HAPTIC_TIMELINE_SERVICE_UUID])
            devices = set(self.ble.find_devices([self.HAPTIC_TIMELINE_SERVICE_UUID]))
            import time
            while len(devices) == 0:
                print "scanning..."
                time.sleep(1)
                devices = set(self.ble.find_devices([self.HAPTIC_TIMELINE_SERVICE_UUID]))
            device_list = []
            for i, d in enumerate(devices):
                device_list.append(d)
                print i, "\t", d.id
            self.device = device_list[int(raw_input("Enter a number to select device: "))]
        finally:
            # Make sure scanning is stopped before exiting.
            self.adapter.stop_scan()

        # Connect to device. Will time out after 60 seconds, specify timeout_sec parameter to change the timeout.
        print('Connecting to device...')
        self.device.connect()

        # Wait for service discovery to complete for at least the specified service and characteristic UUID lists. Will time out after 60 seconds (specify timeout_sec parameter to override).
        print('Discovering services...')
        self.device.discover([self.HAPTIC_TIMELINE_SERVICE_UUID], [self.ACTUATOR_CHARACTERISTIC_UUID])

        # Find the Haptic Timeline service and its characteristics.
        self.timeline_service = self.device.find_service(self.HAPTIC_TIMELINE_SERVICE_UUID)
        self.actuator_characteristic = self.timeline_service.find_characteristic(self.ACTUATOR_CHARACTERISTIC_UUID)

    # Clear any cached data because both bluez and CoreBluetooth have issues with
    # caching data and it going stale.
    ble.clear_cached_data()

    # Get the first available BLE network adapter and make sure it's powered on.
    adapter = ble.get_default_adapter()
    adapter.power_on()
    print('Using adapter: {0}'.format(adapter.name))

    # Disconnect any currently connected UART devices.  Good for cleaning up and
    # starting from a fresh state.
    print('Disconnecting any connected UART devices...')
    UART.disconnect_devices()

    # Continually check bleQueue
    while True:
        if not bleQueue.empty():
            event = bleQueue.get()
            print("Triggering event: " + event)

            if event == "connect":
                _connect()

# Setup ble runloop
def init():
    # Initialize the BLE system.  MUST be called before other BLE calls!
    ble.initialize()

    # Start the mainloop to process BLE events, and run the provided function in
    # a background thread.  When the provided main function stops running, returns
    # an integer status code, or throws an error the program will exit.
    ble.run_mainloop_with(main)
