# Safecast

from ... import nmea

class Safecast(nmea.ProprietarySentence):
    sentence_types = {}
    def __new__(_cls, manufacturer, data):
        name = manufacturer + data[0]
        cls = _cls.sentence_types.get(name, _cls)
        return super(Safecast, cls).__new__(cls)


class BNRDD(Safecast):
    """ Safecast BNRDD
    """
    fields = (
        ("Device ID", "device_id"),
        ("date", "date"),
        ("Radiation 1 Minute", "rad_1_min"),
        ("Radiation 5 Seconds", "rad_5_secs"),
        ("Radiation Total Count", "rad_total_count"),
        ("Radiation Count Validity Flag", "rad_valid"),
        ("Latitude", "latitude"),
        ("Hemisphere", "hemisphere"),
        ("Longitude", "longitude"),
        ("East/West", "east_west"),
        ("Altitude", "altitude"),
        ("GPS validity", "gps_valid"),
        ("HDOP", "hdop"),
        #("Checksum", "checksum")
    )


class BNXSTS(Safecast):
    """ Safecast BNXSTS
    """
    fields = (
        ("Device ID", "device_id"),
        ("Temperature", "temperature"),
        ("Humidity", "humidity"),
        ("CO", "CO"),
        ("NOX", "nox")
    )
