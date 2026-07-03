from astropy.coordinates import EarthLocation, AltAz, get_sun
from astropy.time import Time
import astropy.units as u
import datetime
import numpy as np


class SolarMidnightScheduler:
    """
    Scheduling trigger for 'High-Precision Listen' during the Melbourne refractory period (Solar Midnight).
    """
    def __init__(self, lat=-37.8136, lon=144.9631):
        self.location = EarthLocation(lat=lat*u.deg, lon=lon*u.deg)

    def get_next_solar_midnight(self):
        """
        Calculates the next Solar Midnight for the current location.
        """
        now = Time.now()
        # Search over the next 24 hours
        times = now + np.linspace(0, 24, 1000) * u.hour
        sun_coords = get_sun(times)
        altaz_frame = AltAz(obstime=times, location=self.location)
        sun_altaz = sun_coords.transform_to(altaz_frame)
        
        # Solar Midnight is when the Sun's altitude is at its minimum
        midnight_idx = np.argmin(sun_altaz.alt)
        next_midnight = times[midnight_idx]
        
        return next_midnight

    def schedule_listen(self):
        next_midnight = self.get_next_solar_midnight()
        print(f"Next High-Precision Listen scheduled for: {next_midnight.iso} (Solar Midnight)")
        return next_midnight

if __name__ == "__main__":
    scheduler = SolarMidnightScheduler()
    scheduler.schedule_listen()
