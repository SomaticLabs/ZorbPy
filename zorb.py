# Library for interacting with Zorb devices over BLE
# Copyright Somatic Technologies, Inc. 2018

# Import necessary Python modules
import logging, struct, time

# Import Adafruit BLE Library
import Adafruit_BluefruitLE

# Import relevant custom declarations
import identifiers, constants


# Get the BLE provider for the current platform.
ble = Adafruit_BluefruitLE.get_provider()

# Global variable for accessing Bluetooth adapter
adapter = None

# Global variable for accessing Zorb device
device = None


# Initializer for Zorb module
#
# Parameter mainloop: The function to run within the BLE event loop
def run(mainloop):
    # Initialize the BLE system. MUST be called before other BLE calls!
    ble.initialize()

    # Start the mainloop to process BLE events, and run the provided
    # function in a background thread. When the provided main function stops
    # running, returns an integer status code, or throws an error the
    ble.run_mainloop_with(mainloop)


# Initiates a connection to an advertising Zorb device
#
# Parameter timeout: The timeout for connecting to an advertising device.
def connect(timeout=60):
    global device
    global adapter

    # Clear any cached data because both bluez and CoreBluetooth have issues with
    # caching data and it going stale.
    ble.clear_cached_data()

    # Get the first available BLE network adapter and make sure it's powered on.
    adapter = ble.get_default_adapter()
    adapter.power_on()
    logging.info('Using adapter: {0}'.format(adapter.name))

    # Disconnect any currently connected Zorb devices.
    # Good for cleaning up and starting from a fresh state.
    logging.info('Disconnecting any connected Zorb devices...')
    ble.disconnect_devices(identifiers.ADVERTISED_SERVICES)

    # Scan for Zorb devices.
    start = time.clock()
    logging.info('Searching for Zorb device...')
    try:
        adapter.start_scan()

        # Search for the first Zorb device found (will time out after 60 seconds
        # but you can specify an optional timeout_sec parameter to change it).
        while (time.clock() - start < timeout):
            devices = set(ble.find_devices(service_uuids=identifiers.ADVERTISED_SERVICES))
            for d in devices:
                if d.name == constants.DEVICE_NAME:
                    device = d
                    break
            if device is not None:
                break
    finally:
        # Make sure scanning is stopped before exiting.
        adapter.stop_scan()

    # Check for device discovery completing successfully
    if device is None:
        raise RuntimeError('Failed to find Zorb device!')

    # Connect to device with timeout specified (default 60 seconds)
    logging.info('Connecting to Zorb device...')
    device.connect(timeout_sec=timeout)

    # Wait for service discovery to complete for at least the specified
    # service and characteristic UUID lists.
    # Will time out after 60 seconds (specify timeout_sec parameter to override).
    logging.info('Discovering services...')
    device.discover([identifiers.HAPTIC_TIMELINE_SERVICE_UUID], [identifiers.ACTUATOR_CHARACTERISTIC_UUID, identifiers.PATTERN_TRIGGER_CHARACTERISTIC_UUID])


# Writes desired actuator data to Zorb device.
#
# Parameter duration: The total duration, in milliseconds for the given set of vibrations to last.
#
# Parameter top_left: Intensity, in a range from 0 to 100, for the top left actuator to be set at.
#
# Parameter top_right: Intensity, in a range from 0 to 100, for the top right actuator to be set at.
#
# Parameter bottom_left: Intensity, in a range from 0 to 100, for the bottom left actuator to be set at.
#
# Parameter bottom_right: Intensity, in a range from 0 to 100, for the bottom right actuator to be set at.
def writeActuators(duration, top_left, top_right, bottom_left, bottom_right):
    # Perform input checking
    if duration < 0:
        raise ValueError("Duration must be non-negative (milliseconds).")
    for actuator in [top_left, top_right, bottom_left, bottom_right]:
        if actuator < 0 or actuator > 100:
            raise ValueError("Actuator intensity must be in range 0 to 100.")

    # Find the haptic timeline service and its actuator characteristic.
    timeline_service = device.find_service(identifiers.HAPTIC_TIMELINE_SERVICE_UUID)
    actuator_characteristic = timeline_service.find_characteristic(identifiers.ACTUATOR_CHARACTERISTIC_UUID)

    # Create data packet from pattern character
    actuator_bytes = struct.pack("<HBBBB", duration, top_left, top_right, bottom_left, bottom_right)
    data_packet = bytearray(actuator_bytes)

    # Write data
    logging.info('Writing %s to actuator characteristic.' % data_packet)
    actuator_characteristic.write_value(data_packet)


# Triggers a given pre-loaded pattern on the connected Zorb device
#
# Parameter pattern: The desired pattern to trigger (see options below)
CONFETTI = "p"
POINT_LEFT = "l"
POINT_RIGHT = "r"
SMASH_LEFT = "s"
SMASH_RIGHT = "t"
SKIP_LEFT = "b"
SKIP_RIGHT = "c"
HANDS_RAISED = "u"
WAIVING_HAND = "a"
HUSHED = "q"
FLUSHED = "w"
GRIMACING = "f"
SMILING = "d"
GRINNING = "m"
LAUGHING = "k"
def triggerPattern(pattern):
    # Perform input checking
    patterns = [
        CONFETTI,
        POINT_LEFT,
        POINT_RIGHT,
        SMASH_LEFT,
        SMASH_RIGHT,
        SKIP_LEFT,
        SKIP_RIGHT,
        HANDS_RAISED,
        WAIVING_HAND,
        HUSHED,
        FLUSHED,
        GRIMACING,
        SMILING,
        GRINNING,
        LAUGHING
    ]
    if pattern not in patterns:
        raise ValueError("Trigger pattern must be one of the following: %s" % patterns)

    # Find the haptic timeline service and its pattern characteristic.
    timeline_service = device.find_service(identifiers.HAPTIC_TIMELINE_SERVICE_UUID)
    pattern_trigger_characteristic = timeline_service.find_characteristic(identifiers.PATTERN_TRIGGER_CHARACTERISTIC_UUID)

    # Get data packet from pattern character
    data_packet = bytearray(pattern)

    # Write data
    logging.info('Writing %s to pattern trigger characteristic.' % data_packet)
    pattern_trigger_characteristic.write_value(data_packet)
