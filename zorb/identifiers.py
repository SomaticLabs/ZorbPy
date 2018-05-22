# Copyright Somatic Technologies, Inc. 2018

import uuid

#################################################################################
# General Bluetooth Service UUIDs
#################################################################################

# `UUID` for identifying the standard device information service
DEVICE_INFORMATION_SERVICE_UUID = uuid.UUID("0000180A-0000-1000-8000-00805F9B34FB")

# `UUID` for identifying the firmware revision string characteristic
FIRMWARE_REVISION_STRING_CHARACTERISTIC_UUID = uuid.UUID("00002A26-0000-1000-8000-00805F9B34FB")

# `UUID` for identifying the serial number string characteristic
SERIAL_NUMBER_STRING_CHARACTERISTIC_UUID = uuid.UUID("00002A25-0000-1000-8000-00805F9B34FB")

#################################################################################
# Zorb Specific Bluetooth Service UUIDs
#################################################################################

# `UUID` that advertises the haptic timeline service
HAPTIC_TIMELINE_SERVICE_UUID = uuid.UUID("A28E9217-E9B5-4C0A-9217-1C64D051D762")

# `UUID` that advertises the settings characteristic
SETTINGS_CHARACTERISTIC_UUID = uuid.UUID("A28EFC07-E9B5-4C0A-9217-1C64D051D762")

# `UUID` for identifying the basic actuator control characteristic
ACTUATOR_CHARACTERISTIC_UUID = uuid.UUID("A28EFC05-E9B5-4C0A-9217-1C64D051D762")

# `UUID` for identifying the pattern trigger characteristic
PATTERN_TRIGGER_CHARACTERISTIC_UUID = uuid.UUID("A28EFC08-E9B5-4C0A-9217-1C64D051D762")

# `UUID` for identifying the Nordic UART service
NORDIC_UART_SERVICE_UUID = uuid.UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")

# `UUID` for identifying the Nordic UART TX characteristic
NORDIC_UART_TX_CHARCTERISTIC_UUID = uuid.UUID("6E400003-B5A3-F393-E0A9-E50E24DCCA9E")

# `UUID` for identifying the Nordic UART RX characteristic
NORDIC_UART_RX_CHARCTERISTIC_UUID = uuid.UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E")

# `UUID` of current advertising packet for available services
ADVERTISING_UUID = uuid.UUID("8E409217-F315-4F60-9FB8-838830DAEA50") # FIXME Eventually this can be removed (see relevant comment for ADVERTISED_SERVICES)

# Array of `UUID`s representing all services that Zorb device should advertise
ADVERTISED_SERVICES = [ADVERTISING_UUID] # FIXME: THIS MUST BE replaced with [HapticTimelineServiceUUID]
