import lightkurve as lk
from astropy.coordinates import SkyCoord
import astropy.units as u

class MelbourneProtocol:
    """
    Data Ingestion (Melbourne Protocol)
    Pulls TESS/Hubble FITS data for resonant planetary chains.
    """
    def __init__(self):
        self.targets = ["TOI-178", "TRAPPIST-1"]

    def fetch_tess_data(self, target_name):
        """
        Fetches TESS lightcurve data for a given target.
        """
        print(f"Searching for {target_name} in TESS archives...")
        search_result = lk.search_lightcurve(target_name, mission='TESS')
        if not search_result:
            print(f"No lightcurve found for {target_name}")
            return None
        
        # Download the first available lightcurve
        lc = search_result[0].download()
        return lc

    def get_resonant_chains(self):
        data = {}
        for target in self.targets:
            lc = self.fetch_tess_data(target)
            if lc:
                data[target] = {
                    "time": lc.time.value,
                    "flux": lc.flux.value,
                    "meta": lc.meta
                }
        return data

if __name__ == "__main__":
    protocol = MelbourneProtocol()
    # This might take time and requires internet access
    # results = protocol.get_resonant_chains()
    # print(results.keys())
    print("Melbourne Protocol initialized. Targets: TOI-178, TRAPPIST-1")
