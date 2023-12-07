"""Constants for the ephember integration."""

class EPHBoilerStates(IntEnum):
    """
    Boiler states for a zone given by the api
    """
    FIXME = 0
    OFF = 1
    ON = 2

class EPHDeviceType(IntEnum):
    """
    DeviceType numbers returned by API
    """
    IMMERSION = 4     # device type for immersions returned by EPH